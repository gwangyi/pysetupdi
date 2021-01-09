from .constants import DevicePropertyKeys, DIOD_INHERIT_CLASSDRVS, DIGCF_PRESENT, DEVPKEY, DIGCF_ALLCLASSES
from .structures import GUID, DeviceInfoData, DevicePropertyKey
from .property import Property

import ctypes
import contextlib

# noinspection SpellCheckingInspection
_setupapi = ctypes.WinDLL('setupapi')
_kernel32 = ctypes.WinDLL('kernel32')

"""
WINSETUPAPI HDEVINFO SetupDiGetClassDevsW(
  const GUID *ClassGuid,
  PCWSTR     Enumerator,
  HWND       hwndParent,
  DWORD      Flags
);
"""
_setupapi.SetupDiGetClassDevsW.restype = ctypes.c_void_p
"""
WINSETUPAPI BOOL SetupDiDestroyDeviceInfoList(
  HDEVINFO DeviceInfoSet
);
"""
_setupapi.SetupDiDestroyDeviceInfoList.argtypes = [ctypes.c_void_p]
"""
WINSETUPAPI BOOL SetupDiEnumDeviceInfo(
  HDEVINFO         DeviceInfoSet,
  DWORD            MemberIndex,
  PSP_DEVINFO_DATA DeviceInfoData
);
"""
_setupapi.SetupDiEnumDeviceInfo.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p]
"""
WINSETUPAPI BOOL SetupDiGetDevicePropertyW(
  HDEVINFO         DeviceInfoSet,
  PSP_DEVINFO_DATA DeviceInfoData,
  const DEVPROPKEY *PropertyKey,
  DEVPROPTYPE      *PropertyType,
  PBYTE            PropertyBuffer,
  DWORD            PropertyBufferSize,
  PDWORD           RequiredSize,
  DWORD            Flags
);
"""
_setupapi.SetupDiGetDevicePropertyW.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]
"""
WINSETUPAPI HDEVINFO SetupDiCreateDeviceInfoList(
  const GUID *ClassGuid,
  HWND       hwndParent
);
"""
_setupapi.SetupDiCreateDeviceInfoList.restype = ctypes.c_void_p
"""
WINSETUPAPI BOOL SetupDiOpenDeviceInfoW(
  HDEVINFO         DeviceInfoSet,
  PCWSTR           DeviceInstanceId,
  HWND             hwndParent,
  DWORD            OpenFlags,
  PSP_DEVINFO_DATA DeviceInfoData
);
"""
_setupapi.SetupDiOpenDeviceInfoW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p]
"""
WINSETUPAPI BOOL SetupDiGetDevicePropertyKeys(
  HDEVINFO         DeviceInfoSet,
  PSP_DEVINFO_DATA DeviceInfoData,
  DEVPROPKEY       *PropertyKeyArray,
  DWORD            PropertyKeyCount,
  PDWORD           RequiredPropertyKeyCount,
  DWORD            Flags
);
"""
_setupapi.SetupDiGetDevicePropertyKeys.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint]

class DeviceType(type):
    def __new__(mcs, what, bases, member):
        properties = member.get('_properties_', [])
        for pair in properties:
            name, prop_key = pair
            if not isinstance(prop_key, DevicePropertyKey):
                prop_key = DevicePropertyKey(*str(prop_key).split(' '))

            def getter_closer(prop_key_, name_):
                def getter(self):
                    if name_ not in self.__dict__:
                        self.__dict__[name_] = self.get_property(prop_key_)
                    return self.__dict__[name_]
                return getter
            member[name] = property(getter_closer(prop_key, name))
        return type.__new__(mcs, what, bases, member)


class Device(metaclass=DeviceType):
    pdo_name = ""

    """A class of device"""
    def __init__(self, instance_id):
        """
        Create python Device instance that is associated to device which is specified by given instance id

        :param instance_id: Instance Id of device
        """
        self._handle = None  # SetupDi Device Info List handle and SP_DEVINFO_DATA pair
        self._instance_id = instance_id

    @contextlib.contextmanager
    def open(self):
        """
        Open device to query properties

        :return: context
        """
        handle = _setupapi.SetupDiCreateDeviceInfoList(None, None)
        if handle == -1:
            err_no = ctypes.GetLastError()
            raise WindowsError(err_no, ctypes.FormatError(err_no))
        try:
            dev_info = DeviceInfoData()
            if not _setupapi.SetupDiOpenDeviceInfoW(handle, ctypes.create_unicode_buffer(self._instance_id), None,
                                                    DIOD_INHERIT_CLASSDRVS, ctypes.byref(dev_info)):
                err_no = ctypes.GetLastError()
                raise WindowsError(err_no, ctypes.FormatError(err_no))
            self._handle = (handle, dev_info, self._handle)  # Stack
            yield self
        finally:
            if self._handle is not None and \
                            self._handle[0] == handle:  # If last handle is opened in this function, pop it
                self._handle = self._handle[2]
            _setupapi.SetupDiDestroyDeviceInfoList(handle)  # Close handle

    def get_property(self, key):
        """
        Get device property. See SetupDiGetDeviceProperty from MSDN

        :param key: Key of property
        :return: Property value
        """
        if self._handle is None:  # If the device is not opened yet,
            with self.open():  # Open and retry
                return self.get_property(key)

        handle, dev_info, _ = self._handle
        prop_type = ctypes.c_ulong()
        required_size = ctypes.c_ulong()
        value = None

        if isinstance(key, DevicePropertyKey):  # If given key is an instance of DEVPROPKEY
            key_ = ctypes.byref(key)

            # Property query function is SetupDiGetDeviceProperty
            get_property_ = _setupapi.SetupDiGetDevicePropertyW
        else:
            raise TypeError("Key must be DevPropKey instance, but {} given".format(key))

        # To retrieve buffer size.
        if not get_property_(handle, ctypes.byref(dev_info),
                             key_,
                             ctypes.byref(prop_type),
                             None, 0, ctypes.byref(required_size), 0):
            err_no = ctypes.GetLastError()
            if err_no == 122:  # ERROR_INSUFFICIENT_BUFFER
                value_buffer = ctypes.create_string_buffer(required_size.value)
                if get_property_(handle, ctypes.byref(dev_info),
                                 key_,
                                 ctypes.byref(prop_type),
                                 ctypes.byref(value_buffer),
                                 required_size.value, ctypes.byref(required_size), 0):
                    # Parse property value with retrieved property type
                    value = Property(bytes(value_buffer), prop_type.value)
                err_no = ctypes.GetLastError()

            if err_no == 1168:  # ERROR_NOT_FOUND: Attribute is not exist
                raise AttributeError(key)
            if err_no != 0:
                raise WindowsError(err_no, ctypes.FormatError(err_no))
        return value

    def __getitem__(self, prop_key):
        """
        Alias of get_property

        :param prop_key: Key of property
        :return: Property value
        """
        return self.get_property(prop_key)

    def get_property_keys(self):
        """
        Get all device property keys

        :return: Iterable of device property keys
        """
        if self._handle is None:
            with self.open():
                return self.get_property_keys()

        handle, dev_info, _ = self._handle
        required_size = ctypes.c_ulong()
        if not _setupapi.SetupDiGetDevicePropertyKeys(handle, ctypes.byref(dev_info), None, 0,
                                                      ctypes.byref(required_size), 0):
            err_no = ctypes.GetLastError()
            if err_no == 122:  # ERROR_INSUFFICIENT_BUFFER
                # noinspection SpellCheckingInspection
                devpkeys = (DevicePropertyKey * required_size.value)()
                if _setupapi.SetupDiGetDevicePropertyKeys(handle, ctypes.byref(dev_info), ctypes.byref(devpkeys),
                                                          required_size.value, None, 0):
                    return list(devpkeys)
                err_no = ctypes.GetLastError()

            raise WindowsError(err_no, ctypes.FormatError(err_no))
        return []

    @property
    def path(self):
        """
        Return device file path with PDO name

        :return: file path that can be opened by CreateFile
        """
        # noinspection SpellCheckingInspection
        return r'\\?\GLOBALROOT' + self.pdo_name

    @property
    def parent(self):
        """
        Parent device of this device on device tree

        :return: Parent device
        """
        return Device(self.get_property(DevicePropertyKeys.Device.Parent))

    @property
    def children(self):
        """
        Child devices of this device on device tree

        :return: List of child devices
        """
        return list(Device(child_id) for child_id in self.get_property(DevicePropertyKeys.Device.Children))

    @property
    def siblings(self):
        """
        Sibling devices of this device on device tree

        :return: List of sibling devices
        """
        return list(Device(sibling_id) for sibling_id in self.get_property(DevicePropertyKeys.Device.Siblings))

    # noinspection SpellCheckingInspection
    _properties_ = [
        ('device_desc', DevicePropertyKeys.Device.DeviceDesc),
        ('hardware_id', DevicePropertyKeys.Device.HardwareIds),
        ('compatible_ids', DevicePropertyKeys.Device.CompatibleIds),
        ('service', DevicePropertyKeys.Device.Service),
        ('device_class', DevicePropertyKeys.Device.Class),
        ('class_guid', DevicePropertyKeys.Device.ClassGuid),
        ('driver', DevicePropertyKeys.Device.Driver),
        ('config_flags', DevicePropertyKeys.Device.ConfigFlags),
        ('manufacturer', DevicePropertyKeys.Device.Manufacturer),
        ('friendly_name', DevicePropertyKeys.Device.FriendlyName),
        ('location_info', DevicePropertyKeys.Device.LocationInfo),
        ('pdo_name', DevicePropertyKeys.Device.PDOName),
        ('capabilities', DevicePropertyKeys.Device.Capabilities),
        ('ui_number', DevicePropertyKeys.Device.UINumber),
        ('upper_filters', DevicePropertyKeys.Device.UpperFilters),
        ('lower_filters', DevicePropertyKeys.Device.LowerFilters),
        ('bus_type_guid', DevicePropertyKeys.Device.BusTypeGuid),
        ('legacy_bus_type', DevicePropertyKeys.Device.LegacyBusType),
        ('bus_number', DevicePropertyKeys.Device.BusNumber),
        ('enumerator_name', DevicePropertyKeys.Device.EnumeratorName),
        ('security', DevicePropertyKeys.Device.Security),
        ('security_sds', DevicePropertyKeys.Device.SecuritySDS),
        ('dev_type', DevicePropertyKeys.Device.DevType),
        ('exclusive', DevicePropertyKeys.Device.Exclusive),
        ('characteristics', DevicePropertyKeys.Device.Characteristics),
        ('address', DevicePropertyKeys.Device.Address),
        ('ui_number_desc_format', DevicePropertyKeys.Device.UINumberDescFormat),
        ('power_data', DevicePropertyKeys.Device.PowerData),
        ('removal_policy', DevicePropertyKeys.Device.RemovalPolicy),
        ('removal_policy_default', DevicePropertyKeys.Device.RemovalPolicyDefault),
        ('removal_policy_override', DevicePropertyKeys.Device.RemovalPolicyOverride),
        ('install_state', DevicePropertyKeys.Device.InstallState),
        ('location_paths', DevicePropertyKeys.Device.LocationPaths),
        ('base_container_id', DevicePropertyKeys.Device.BaseContainerId),
        ('dev_node_status', DevicePropertyKeys.Device.DevNodeStatus),
        ('problem_code', DevicePropertyKeys.Device.ProblemCode),
        ('ejection_relations', DevicePropertyKeys.Device.EjectionRelations),
        ('removal_relations', DevicePropertyKeys.Device.RemovalRelations),
        ('power_relations', DevicePropertyKeys.Device.PowerRelations),
        ('bus_relations', DevicePropertyKeys.Device.BusRelations),
        # ('parent', DevicePropertyKeys.Device.Parent),
        # ('children', DevicePropertyKeys.Device.Children),
        # ('siblings', DevicePropertyKeys.Device.Siblings),
        ('transport_relations', DevicePropertyKeys.Device.TransportRelations),
        ('reported', DevicePropertyKeys.Device.Reported),
        ('legacy', DevicePropertyKeys.Device.Legacy),
        ('instance_id', DevicePropertyKeys.Device.InstanceId),
        ('container_id', DevicePropertyKeys.Device.ContainerId),
        ('model_id', DevicePropertyKeys.Device.ModelId),
        ('friendly_name_attributes', DevicePropertyKeys.Device.FriendlyNameAttributes),
        ('manufacturer_attributes', DevicePropertyKeys.Device.ManufacturerAttributes),
        ('presence_not_for_device', DevicePropertyKeys.Device.PresenceNotForDevice),
        ('dhp_rebalance_policy', DevicePropertyKeys.Device.DHP_Rebalance_Policy),
        ('numa_node', DevicePropertyKeys.Device.Numa_Node),
        ('bus_reported_device_desc', DevicePropertyKeys.Device.BusReportedDeviceDesc),
        ('session_id', DevicePropertyKeys.Device.SessionId),
        ('install_date', DevicePropertyKeys.Device.InstallDate),
        ('first_install_date', DevicePropertyKeys.Device.FirstInstallDate),
        ('driver_date', DevicePropertyKeys.Device.DriverDate),
        ('driver_version', DevicePropertyKeys.Device.DriverVersion),
        ('driver_desc', DevicePropertyKeys.Device.DriverDesc),
        ('driver_inf_path', DevicePropertyKeys.Device.DriverInfPath),
        ('driver_inf_section', DevicePropertyKeys.Device.DriverInfSection),
        ('driver_inf_section_ext', DevicePropertyKeys.Device.DriverInfSectionExt),
        ('matching_device_id', DevicePropertyKeys.Device.MatchingDeviceId),
        ('driver_provider', DevicePropertyKeys.Device.DriverProvider),
        ('driver_prop_page_provider', DevicePropertyKeys.Device.DriverPropPageProvider),
        ('driver_co_installers', DevicePropertyKeys.Device.DriverCoInstallers),
        ('resource_picker_tags', DevicePropertyKeys.Device.ResourcePickerTags),
        ('resource_picker_exceptions', DevicePropertyKeys.Device.ResourcePickerExceptions),
        ('driver_rank', DevicePropertyKeys.Device.DriverRank),
        ('driver_logo_level', DevicePropertyKeys.Device.DriverLogoLevel),
        ('no_connect_sound', DevicePropertyKeys.Device.NoConnectSound),
        ('generic_driver_installed', DevicePropertyKeys.Device.GenericDriverInstalled),
        ('additional_software_requested', DevicePropertyKeys.Device.AdditionalSoftwareRequested),
        ('safe_removal_required', DevicePropertyKeys.Device.SafeRemovalRequired),
        ('safe_removal_required_override', DevicePropertyKeys.Device.SafeRemovalRequiredOverride),
    ]

    def __str__(self):
        """
        Device name

        :return: Friendly name or device description of instance id of device
        """
        try:
            return self.friendly_name
        except AttributeError:
            try:
                return self.device_desc
            except AttributeError:
                return self._instance_id

    def __repr__(self):
        return "<pysetupdi.Device: {}>".format(str(self))


def devices(guid=None, enumerator=None, hwnd_parent=None, flags=DIGCF_PRESENT):
    """
    Return generator of `Device` objects which is specified by given parameters
    Parameters are almost same to SetupDiGetClassDev's

    :param guid: A string that describes the GUID for a device setup class or a device interface class.
        The format of GUID string is same to CLSIDFromString.
    :param enumerator: An ID of a PnP enumerator.
    :param hwnd_parent: A handle to the top-level window. This handle is optional and can be None
    :param flags: A variable of type DWORD that specifies control options.
    :return: Iterable of Device objects
    """
    if guid is None:
        guid_ = None
        flags |= DIGCF_ALLCLASSES
    elif isinstance(guid, GUID):
        guid_ = bytes(guid)
    else:
        guid_ = bytes(GUID(str(guid)))

    if enumerator is None:
        enumerator_ = None
    else:
        enumerator_ = ctypes.create_unicode_buffer(enumerator)

    handle = _setupapi.SetupDiGetClassDevsW(guid_, enumerator_, hwnd_parent, flags)
    if handle == -1:
        err_no = ctypes.GetLastError()
        raise WindowsError(err_no, ctypes.FormatError(err_no), (guid, enumerator, flags))

    try:
        idx = 0
        dev_info = DeviceInfoData()
        while _setupapi.SetupDiEnumDeviceInfo(handle, idx, ctypes.byref(dev_info)):
            idx += 1
            prop_type = ctypes.c_ulong()
            required_size = ctypes.c_ulong()
            instance_id = None
            if not _setupapi.SetupDiGetDevicePropertyW(handle, ctypes.byref(dev_info),
                                                       ctypes.byref(DEVPKEY.Device.InstanceId),
                                                       ctypes.byref(prop_type),
                                                       None, 0, ctypes.byref(required_size), 0):
                err_no = ctypes.GetLastError()
                if err_no == 122:  # ERROR_INSUFFICIENT_BUFFER
                    instance_id_buffer = ctypes.create_string_buffer(required_size.value)
                    if _setupapi.SetupDiGetDevicePropertyW(handle, ctypes.byref(dev_info),
                                                           ctypes.byref(DEVPKEY.Device.InstanceId),
                                                           ctypes.byref(prop_type),
                                                           ctypes.byref(instance_id_buffer),
                                                           required_size.value, ctypes.byref(required_size), 0):
                        instance_id = Property(bytes(instance_id_buffer), prop_type.value)
                    err_no = ctypes.GetLastError()
                if err_no != 0:
                    raise WindowsError(err_no, ctypes.FormatError(err_no))
            yield Device(instance_id)

        err_no = ctypes.GetLastError()
        if err_no != 259:
            raise WindowsError(err_no, ctypes.FormatError(err_no), (guid, enumerator, flags))

    finally:
        _setupapi.SetupDiDestroyDeviceInfoList(handle)
