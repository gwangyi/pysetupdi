""":mod:`pysetupdi.constants`

Pre-defined constants from windows SDK
"""
import enum
from .structures import DevicePropertyKey


# noinspection SpellCheckingInspection
class DiOpenDeviceInfo(enum.IntEnum):
    """DIOD_xxx constants
    """
    InheritClassDrvs = 2
    CancelRemove = 4


# noinspection SpellCheckingInspection
class DiGetClassDevsFlags(enum.IntEnum):
    """DIGCF_xxx constants
    """
    Default = 0x00000001
    Present = 0x00000002,
    AllClasses = 0x00000004,
    Profile = 0x00000008,
    DeviceInterface = 0x00000010,


# noinspection SpellCheckingInspection
class DevicePropertyKeys(object):
    """DEVPKEY_xxx constants"""
    NAME = DevicePropertyKey('{b725f130-47ef-101a-a5f1-02608c9eebac}', 10, 'DEVPKEY_NAME')
    Numa_Proximity_Domain = DevicePropertyKey('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}', 1,
                                              'DEVPKEY_Numa_Proximity_Domain')

    # noinspection SpellCheckingInspection
    class Device(object):
        """DEVPKEY_Device_xxx constants"""
        DeviceDesc = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 2,
                                       'DEVPKEY_Device_DeviceDesc')
        HardwareIds = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 3,
                                        'DEVPKEY_Device_HardwareIds')
        CompatibleIds = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 4,
                                          'DEVPKEY_Device_CompatibleIds')
        Service = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 6,
                                    'DEVPKEY_Device_Service')
        Class = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 9,
                                  'DEVPKEY_Device_Class')
        ClassGuid = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 10,
                                      'DEVPKEY_Device_ClassGuid')
        Driver = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 11,
                                   'DEVPKEY_Device_Driver')
        ConfigFlags = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 12,
                                        'DEVPKEY_Device_ConfigFlags')
        Manufacturer = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 13,
                                         'DEVPKEY_Device_Manufacturer')
        FriendlyName = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 14,
                                         'DEVPKEY_Device_FriendlyName')
        LocationInfo = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 15,
                                         'DEVPKEY_Device_LocationInfo')
        PDOName = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 16,
                                    'DEVPKEY_Device_PDOName')
        Capabilities = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 17,
                                         'DEVPKEY_Device_Capabilities')
        UINumber = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 18,
                                     'DEVPKEY_Device_UINumber')
        UpperFilters = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 19,
                                         'DEVPKEY_Device_UpperFilters')
        LowerFilters = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 20,
                                         'DEVPKEY_Device_LowerFilters')
        BusTypeGuid = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 21,
                                        'DEVPKEY_Device_BusTypeGuid')
        LegacyBusType = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 22,
                                          'DEVPKEY_Device_LegacyBusType')
        BusNumber = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 23,
                                      'DEVPKEY_Device_BusNumber')
        EnumeratorName = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 24,
                                           'DEVPKEY_Device_EnumeratorName')
        Security = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 25,
                                     'DEVPKEY_Device_Security')
        SecuritySDS = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 26,
                                        'DEVPKEY_Device_SecuritySDS')
        DevType = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 27,
                                    'DEVPKEY_Device_DevType')
        Exclusive = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 28,
                                      'DEVPKEY_Device_Exclusive')
        Characteristics = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 29,
                                            'DEVPKEY_Device_Characteristics')
        Address = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 30,
                                    'DEVPKEY_Device_Address')
        UINumberDescFormat = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 31,
                                               'DEVPKEY_Device_UINumberDescFormat')
        PowerData = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 32,
                                      'DEVPKEY_Device_PowerData')
        RemovalPolicy = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 33,
                                          'DEVPKEY_Device_RemovalPolicy')
        RemovalPolicyDefault = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 34,
                                                 'DEVPKEY_Device_RemovalPolicyDefault')
        RemovalPolicyOverride = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 35,
                                                  'DEVPKEY_Device_RemovalPolicyOverride')
        InstallState = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 36,
                                         'DEVPKEY_Device_InstallState')
        LocationPaths = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 37,
                                          'DEVPKEY_Device_LocationPaths')
        BaseContainerId = DevicePropertyKey('{a45c254e-df1c-4efd-8020-67d146a850e0}', 38,
                                            'DEVPKEY_Device_BaseContainerId')
        DevNodeStatus = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 2,
                                          'DEVPKEY_Device_DevNodeStatus')
        ProblemCode = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 3,
                                        'DEVPKEY_Device_ProblemCode')
        EjectionRelations = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 4,
                                              'DEVPKEY_Device_EjectionRelations')
        RemovalRelations = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 5,
                                             'DEVPKEY_Device_RemovalRelations')
        PowerRelations = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 6,
                                           'DEVPKEY_Device_PowerRelations')
        BusRelations = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 7,
                                         'DEVPKEY_Device_BusRelations')
        Parent = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 8,
                                   'DEVPKEY_Device_Parent')
        Children = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 9,
                                     'DEVPKEY_Device_Children')
        Siblings = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 10,
                                     'DEVPKEY_Device_Siblings')
        TransportRelations = DevicePropertyKey('{4340a6c5-93fa-4706-972c-7b648008a5a7}', 11,
                                               'DEVPKEY_Device_TransportRelations')
        Reported = DevicePropertyKey('{80497100-8c73-48b9-aad9-ce387e19c56e}', 2,
                                     'DEVPKEY_Device_Reported')
        Legacy = DevicePropertyKey('{80497100-8c73-48b9-aad9-ce387e19c56e}', 3,
                                   'DEVPKEY_Device_Legacy')
        InstanceId = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 256,
                                       'DEVPKEY_Device_InstanceId')
        ContainerId = DevicePropertyKey('{8c7ed206-3f8a-4827-b3ab-ae9e1faefc6c}', 2,
                                        'DEVPKEY_Device_ContainerId')
        ModelId = DevicePropertyKey('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}', 2,
                                    'DEVPKEY_Device_ModelId')
        FriendlyNameAttributes = DevicePropertyKey('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}', 3,
                                                   'DEVPKEY_Device_FriendlyNameAttributes')
        ManufacturerAttributes = DevicePropertyKey('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}', 4,
                                                   'DEVPKEY_Device_ManufacturerAttributes')
        PresenceNotForDevice = DevicePropertyKey('{80d81ea6-7473-4b0c-8216-efc11a2c4c8b}', 5,
                                                 'DEVPKEY_Device_PresenceNotForDevice')
        DHP_Rebalance_Policy = DevicePropertyKey('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}', 2,
                                                 'DEVPKEY_Device_DHP_Rebalance_Policy')
        Numa_Node = DevicePropertyKey('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}', 3,
                                      'DEVPKEY_Device_Numa_Node')
        BusReportedDeviceDesc = DevicePropertyKey('{540b947e-8b40-45bc-a8a2-6a0b894cbda2}', 4,
                                                  'DEVPKEY_Device_BusReportedDeviceDesc')
        SessionId = DevicePropertyKey('{83da6326-97a6-4088-9453-a1923f573b29}', 6,
                                      'DEVPKEY_Device_SessionId')
        InstallDate = DevicePropertyKey('{83da6326-97a6-4088-9453-a1923f573b29}', 100,
                                        'DEVPKEY_Device_InstallDate')
        FirstInstallDate = DevicePropertyKey('{83da6326-97a6-4088-9453-a1923f573b29}', 101,
                                             'DEVPKEY_Device_FirstInstallDate')
        DriverDate = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 2,
                                       'DEVPKEY_Device_DriverDate')
        DriverVersion = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 3,
                                          'DEVPKEY_Device_DriverVersion')
        DriverDesc = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 4,
                                       'DEVPKEY_Device_DriverDesc')
        DriverInfPath = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 5,
                                          'DEVPKEY_Device_DriverInfPath')
        DriverInfSection = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 6,
                                             'DEVPKEY_Device_DriverInfSection')
        DriverInfSectionExt = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 7,
                                                'DEVPKEY_Device_DriverInfSectionExt')
        MatchingDeviceId = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 8,
                                             'DEVPKEY_Device_MatchingDeviceId')
        DriverProvider = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 9,
                                           'DEVPKEY_Device_DriverProvider')
        DriverPropPageProvider = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 10,
                                                   'DEVPKEY_Device_DriverPropPageProvider')
        DriverCoInstallers = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 11,
                                               'DEVPKEY_Device_DriverCoInstallers')
        ResourcePickerTags = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 12,
                                               'DEVPKEY_Device_ResourcePickerTags')
        ResourcePickerExceptions = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 13,
                                                     'DEVPKEY_Device_ResourcePickerExceptions')
        DriverRank = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 14,
                                       'DEVPKEY_Device_DriverRank')
        DriverLogoLevel = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 15,
                                            'DEVPKEY_Device_DriverLogoLevel')
        NoConnectSound = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 17,
                                           'DEVPKEY_Device_NoConnectSound')
        GenericDriverInstalled = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 18,
                                                   'DEVPKEY_Device_GenericDriverInstalled')
        AdditionalSoftwareRequested = DevicePropertyKey('{a8b865dd-2e3d-4094-ad97-e593a70c75d6}', 19,
                                                        'DEVPKEY_Device_AdditionalSoftwareRequested')
        SafeRemovalRequired = DevicePropertyKey('{afd97640-86a3-4210-b67c-289c41aabe55}', 2,
                                                'DEVPKEY_Device_SafeRemovalRequired')
        SafeRemovalRequiredOverride = DevicePropertyKey('{afd97640-86a3-4210-b67c-289c41aabe55}', 3,
                                                        'DEVPKEY_Device_SafeRemovalRequiredOverride')

    class DriverPackage(object):
        """DEVPKEY_DriverPackage_xxx constants"""
        Model = DevicePropertyKey('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}', 2,
                                  'DEVPKEY_DriverPackage_Model')
        VendorWebSite = DevicePropertyKey('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}', 3,
                                          'DEVPKEY_DriverPackage_VendorWebSite')
        DetailedDescription = DevicePropertyKey('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}', 4,
                                                'DEVPKEY_DriverPackage_DetailedDescription')
        DocumentationLink = DevicePropertyKey('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}', 5,
                                              'DEVPKEY_DriverPackage_DocumentationLink')
        Icon = DevicePropertyKey('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}', 6,
                                 'DEVPKEY_DriverPackage_Icon')
        BrandingIcon = DevicePropertyKey('{cf73bb51-3abf-44a2-85e0-9a3dc7a12132}', 7,
                                         'DEVPKEY_DriverPackage_BrandingIcon')

    # noinspection SpellCheckingInspection
    class DeviceClass(object):
        """DEVPKEY_DeviceClass_xxx constants"""
        UpperFilters = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 19,
                                         'DEVPKEY_DeviceClass_UpperFilters')
        LowerFilters = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 20,
                                         'DEVPKEY_DeviceClass_LowerFilters')
        Security = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 25,
                                     'DEVPKEY_DeviceClass_Security')
        SecuritySDS = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 26,
                                        'DEVPKEY_DeviceClass_SecuritySDS')
        DevType = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 27,
                                    'DEVPKEY_DeviceClass_DevType')
        Exclusive = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 28,
                                      'DEVPKEY_DeviceClass_Exclusive')
        Characteristics = DevicePropertyKey('{4321918b-f69e-470d-a5de-4d88c75ad24b}', 29,
                                            'DEVPKEY_DeviceClass_Characteristics')
        Name = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 2,
                                 'DEVPKEY_DeviceClass_Name')
        ClassName = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 3,
                                      'DEVPKEY_DeviceClass_ClassName')
        Icon = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 4,
                                 'DEVPKEY_DeviceClass_Icon')
        ClassInstaller = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 5,
                                           'DEVPKEY_DeviceClass_ClassInstaller')
        PropPageProvider = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 6,
                                             'DEVPKEY_DeviceClass_PropPageProvider')
        NoInstallClass = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 7,
                                           'DEVPKEY_DeviceClass_NoInstallClass')
        NoDisplayClass = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 8,
                                           'DEVPKEY_DeviceClass_NoDisplayClass')
        SilentInstall = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 9,
                                          'DEVPKEY_DeviceClass_SilentInstall')
        NoUseClass = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 10,
                                       'DEVPKEY_DeviceClass_NoUseClass')
        DefaultService = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 11,
                                           'DEVPKEY_DeviceClass_DefaultService')
        IconPath = DevicePropertyKey('{259abffc-50a7-47ce-af08-68c9a7d73366}', 12,
                                     'DEVPKEY_DeviceClass_IconPath')
        DHPRebalanceOptOut = DevicePropertyKey('{d14d3ef3-66cf-4ba2-9d38-0ddb37ab4701}', 2,
                                               'DEVPKEY_DeviceClass_DHPRebalanceOptOut')
        ClassCoInstallers = DevicePropertyKey('{713d1703-a2e2-49f5-9214-56472ef3da5c}', 2,
                                              'DEVPKEY_DeviceClass_ClassCoInstallers')

    class DeviceInterface(object):
        """DEVPKEY_DeviceInterface_xxx constants"""
        FriendlyName = DevicePropertyKey('{026e516e-b814-414b-83cd-856d6fef4822}', 2,
                                         'DEVPKEY_DeviceInterface_FriendlyName')
        Enabled = DevicePropertyKey('{026e516e-b814-414b-83cd-856d6fef4822}', 3,
                                    'DEVPKEY_DeviceInterface_Enabled')
        ClassGuid = DevicePropertyKey('{026e516e-b814-414b-83cd-856d6fef4822}', 4,
                                      'DEVPKEY_DeviceInterface_ClassGuid')

    class DeviceInterfaceClass(object):
        """DEVPKEY_DeviceInterfaceClass_xxx constants"""
        DefaultInterface = DevicePropertyKey('{14c83a99-0b3f-44b7-be4c-a178d3990564}', 2,
                                             'DEVPKEY_DeviceInterfaceClass_DefaultInterface')

    # noinspection SpellCheckingInspection
    class DeviceDisplay(object):
        """DEVPKEY_DeviceDisplay_xxx constants"""
        IsShowInDisconnectedState = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 0x44,
                                                      'DEVPKEY_DeviceDisplay_IsShowInDisconnectedState')
        IsNotInterestingForDisplay = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 0x4a,
                                                       'DEVPKEY_DeviceDisplay_IsNotInterestingForDisplay')
        Category = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 0x5a,
                                     'DEVPKEY_DeviceDisplay_Category')
        UnpairUninstall = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 0x62,
                                            'DEVPKEY_DeviceDisplay_UnpairUninstall')
        RequiresUninstallElevation = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 0x63,
                                                       'DEVPKEY_DeviceDisplay_RequiresUninstallElevation')
        AlwaysShowDeviceAsConnected = DevicePropertyKey('{78c34fc8-104a-4aca-9ea4-524d52996e57}', 0x65,
                                                        'DEVPKEY_DeviceDisplay_AlwaysShowDeviceAsConnected')


# noinspection SpellCheckingInspection
class DevicePropertyType(enum.IntEnum):
    """DEVPROP_TYPE_xxx, DEVPROP_TYPEMOD_xxx constants"""
    ModArray = 0x00001000  # array of fixed - sized data elements
    ModList = 0x00002000  # list of variable - sized data elements

    Empty = 0x00000000  # nothing, no property data
    Null = 0x00000001  # null property data
    Sbyte = 0x00000002  # 8 - bit signed int (SBYTE)
    Byte = 0x00000003  # 8 - bit unsigned int (BYTE)
    Int16 = 0x00000004  # 16-bit signed int (SHORT)
    Uint16 = 0x00000005  # 16-bit unsigned int (USHORT)
    Int32 = 0x00000006  # 32-bit signed int (LONG)
    Uint32 = 0x00000007  # 32-bit unsigned int (ULONG)
    Int64 = 0x00000008  # 64-bit signed int (LONG64)
    Uint64 = 0x00000009  # 64-bit unsigned int (ULONG64)
    Float = 0x0000000A  # 32 - bit floating - point (FLOAT)
    Double = 0x0000000B  # 64 - bit floating - point (DOUBLE)
    Decimal = 0x0000000C  # 128 - bit data (DECIMAL)
    Guid = 0x0000000D  # 128 - bit unique identifier (GUID)
    Currency = 0x0000000E  # 64 bit signed int currency value (CURRENCY)
    Date = 0x0000000F  # date (DATE)
    Filetime = 0x00000010  # file time (FILETIME)
    Boolean = 0x00000011  # 8 - bit boolean (DEVPROP_BOOLEAN)
    String = 0x00000012  # null - terminated string
    StringList = String | ModList  # multi-sz string list
    SecurityDescriptor = 0x00000013  # self - relative binary SECURITY_DESCRIPTOR
    SecurityDescriptorString = 0x00000014  # security descriptor string (SDDL format)
    DevicePropertyKey = 0x00000015  # device property key (DEVPROPKEY)
    DevicePropertyType = 0x00000016  # device property type (DEVPROPTYPE)
    Binary = Byte | ModArray  # custom binary data
    Error = 0x00000017  # 32 - bit Win32 system error code
    NtStatus = 0x00000018  # 32 - bit NTSTATUS code
    StringIndirect = 0x00000019  # string resource (@[path\] < dllname > , -<strId >)

    MaskType = 0x00000FFF  # range for base DEVPROP_TYPE_ values
    MaskTypeMod = 0x0000F000  # mask for DEVPROP_TYPEMOD_ type modifiers

    # noinspection SpellCheckingInspection
    MaxType = StringIndirect  # max valid DEVPROP_TYPE_ value
    # noinspection SpellCheckingInspection
    MaxTypeMod = ModList  # max valid DEVPROP_TYPEMOD_ value


class FormatMessage(enum.IntEnum):
    """FORMAT_MESSAGE_xxx constants"""
    AllocateBuffer = 0x00000100
    IgnoreInserts = 0x00000200
    FromString = 0x00000400
    FromHmodule = 0x00000800
    FromSystem = 0x00001000
    ArgumentArray = 0x00002000
    MaxWidthMask = 0x000000FF


# Below declarations makes C-like synonym of declared constants

# noinspection SpellCheckingInspection
DIGCF_DEFAULT = DiGetClassDevsFlags.Default
# noinspection SpellCheckingInspection
DIGCF_PRESENT = DiGetClassDevsFlags.Present
# noinspection SpellCheckingInspection
DIGCF_ALLCLASSES = DiGetClassDevsFlags.AllClasses
# noinspection SpellCheckingInspection
DIGCF_PROFILE = DiGetClassDevsFlags.Profile
# noinspection SpellCheckingInspection
DIGCF_DEVICEINTERFACE = DiGetClassDevsFlags.DeviceInterface

# noinspection SpellCheckingInspection
DEVPROP_TYPE = DevicePropertyType

# noinspection SpellCheckingInspection
DEVPROP_TYPEMOD_ARRAY = DevicePropertyType.ModArray  # array of fixed - sized data elements
# noinspection SpellCheckingInspection
DEVPROP_TYPEMOD_LIST = DevicePropertyType.ModList  # list of variable - sized data elements

# noinspection SpellCheckingInspection
DEVPROP_TYPE_EMPTY = DevicePropertyType.Empty
# noinspection SpellCheckingInspection
DEVPROP_TYPE_NULL = DevicePropertyType.Null
# noinspection SpellCheckingInspection
DEVPROP_TYPE_SBYTE = DevicePropertyType.Sbyte
# noinspection SpellCheckingInspection
DEVPROP_TYPE_BYTE = DevicePropertyType.Byte
# noinspection SpellCheckingInspection
DEVPROP_TYPE_INT16 = DevicePropertyType.Int16
# noinspection SpellCheckingInspection
DEVPROP_TYPE_UINT16 = DevicePropertyType.Uint16
# noinspection SpellCheckingInspection
DEVPROP_TYPE_INT32 = DevicePropertyType.Int32
# noinspection SpellCheckingInspection
DEVPROP_TYPE_UINT32 = DevicePropertyType.Uint32
# noinspection SpellCheckingInspection
DEVPROP_TYPE_INT64 = DevicePropertyType.Int64
# noinspection SpellCheckingInspection
DEVPROP_TYPE_UINT64 = DevicePropertyType.Uint64
# noinspection SpellCheckingInspection
DEVPROP_TYPE_FLOAT = DevicePropertyType.Float
# noinspection SpellCheckingInspection
DEVPROP_TYPE_DOUBLE = DevicePropertyType.Double
# noinspection SpellCheckingInspection
DEVPROP_TYPE_DECIMAL = DevicePropertyType.Decimal
# noinspection SpellCheckingInspection
DEVPROP_TYPE_GUID = DevicePropertyType.Guid
# noinspection SpellCheckingInspection
DEVPROP_TYPE_CURRENCY = DevicePropertyType.Currency
# noinspection SpellCheckingInspection
DEVPROP_TYPE_DATE = DevicePropertyType.Date
# noinspection SpellCheckingInspection
DEVPROP_TYPE_FILETIME = DevicePropertyType.Filetime
# noinspection SpellCheckingInspection
DEVPROP_TYPE_BOOLEAN = DevicePropertyType.Boolean
# noinspection SpellCheckingInspection
DEVPROP_TYPE_STRING = DevicePropertyType.String
# noinspection SpellCheckingInspection
DEVPROP_TYPE_STRING_LIST = DevicePropertyType.StringList
# noinspection SpellCheckingInspection
DEVPROP_TYPE_SECURITY_DESCRIPTOR = DevicePropertyType.SecurityDescriptor
# noinspection SpellCheckingInspection
DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING = DevicePropertyType.SecurityDescriptorString
# noinspection SpellCheckingInspection
DEVPROP_TYPE_DEVPROPKEY = DevicePropertyType.DevicePropertyKey
# noinspection SpellCheckingInspection
DEVPROP_TYPE_DEVPROPTYPE = DevicePropertyType.DevicePropertyType
# noinspection SpellCheckingInspection
DEVPROP_TYPE_BINARY = DevicePropertyType.Binary
# noinspection SpellCheckingInspection
DEVPROP_TYPE_ERROR = DevicePropertyType.Error
# noinspection SpellCheckingInspection
DEVPROP_TYPE_NTSTATUS = DevicePropertyType.NtStatus
# noinspection SpellCheckingInspection
DEVPROP_TYPE_STRING_INDIRECT = DevicePropertyType.StringIndirect

# noinspection SpellCheckingInspection
MAX_DEVPROP_TYPE = DEVPROP_TYPE_STRING_INDIRECT  # max valid DEVPROP_TYPE_ value
# noinspection SpellCheckingInspection
MAX_DEVPROP_TYPEMOD = DEVPROP_TYPEMOD_LIST  # max valid DEVPROP_TYPEMOD_ value

# noinspection SpellCheckingInspection
DEVPROP_MASK_TYPE = DevicePropertyType.MaskType  # range for base DEVPROP_TYPE_ values
# noinspection SpellCheckingInspection
DEVPROP_MASK_TYPEMOD = DevicePropertyType.MaskTypeMod  # mask for DEVPROP_TYPEMOD_ type modifiers

FORMAT_MESSAGE_ALLOCATE_BUFFER = FormatMessage.AllocateBuffer
FORMAT_MESSAGE_IGNORE_INSERTS = FormatMessage.IgnoreInserts
FORMAT_MESSAGE_FROM_STRING = FormatMessage.FromString
FORMAT_MESSAGE_FROM_HMODULE = FormatMessage.FromHmodule
FORMAT_MESSAGE_FROM_SYSTEM = FormatMessage.FromSystem
FORMAT_MESSAGE_ARGUMENT_ARRAY = FormatMessage.ArgumentArray
FORMAT_MESSAGE_MAX_WIDTH_MASK = FormatMessage.MaxWidthMask

# noinspection SpellCheckingInspection
DIOD_INHERIT_CLASSDRVS = DiOpenDeviceInfo.InheritClassDrvs
# noinspection SpellCheckingInspection
DIOD_CANCEL_REMOVE = DiOpenDeviceInfo.CancelRemove

# noinspection SpellCheckingInspection
DEVPKEY = DevicePropertyKeys

# noinspection SpellCheckingInspection
DEVPKEY_NAME = DevicePropertyKeys.NAME
# noinspection SpellCheckingInspection
DEVPKEY_Numa_Proximity_Domain = DevicePropertyKeys.Numa_Proximity_Domain

DEVPKEY_Device_DeviceDesc = DevicePropertyKeys.Device.DeviceDesc
DEVPKEY_Device_HardwareIds = DevicePropertyKeys.Device.HardwareIds
DEVPKEY_Device_CompatibleIds = DevicePropertyKeys.Device.CompatibleIds
DEVPKEY_Device_Service = DevicePropertyKeys.Device.Service
DEVPKEY_Device_Class = DevicePropertyKeys.Device.Class
DEVPKEY_Device_ClassGuid = DevicePropertyKeys.Device.ClassGuid
DEVPKEY_Device_Driver = DevicePropertyKeys.Device.Driver
DEVPKEY_Device_ConfigFlags = DevicePropertyKeys.Device.ConfigFlags
DEVPKEY_Device_Manufacturer = DevicePropertyKeys.Device.Manufacturer
DEVPKEY_Device_FriendlyName = DevicePropertyKeys.Device.FriendlyName
DEVPKEY_Device_LocationInfo = DevicePropertyKeys.Device.LocationInfo
DEVPKEY_Device_PDOName = DevicePropertyKeys.Device.PDOName
DEVPKEY_Device_Capabilities = DevicePropertyKeys.Device.Capabilities
DEVPKEY_Device_UINumber = DevicePropertyKeys.Device.UINumber
DEVPKEY_Device_UpperFilters = DevicePropertyKeys.Device.UpperFilters
DEVPKEY_Device_LowerFilters = DevicePropertyKeys.Device.LowerFilters
DEVPKEY_Device_BusTypeGuid = DevicePropertyKeys.Device.BusTypeGuid
DEVPKEY_Device_LegacyBusType = DevicePropertyKeys.Device.LegacyBusType
DEVPKEY_Device_BusNumber = DevicePropertyKeys.Device.BusNumber
DEVPKEY_Device_EnumeratorName = DevicePropertyKeys.Device.EnumeratorName
DEVPKEY_Device_Security = DevicePropertyKeys.Device.Security
DEVPKEY_Device_SecuritySDS = DevicePropertyKeys.Device.SecuritySDS
DEVPKEY_Device_DevType = DevicePropertyKeys.Device.DevType
DEVPKEY_Device_Exclusive = DevicePropertyKeys.Device.Exclusive
DEVPKEY_Device_Characteristics = DevicePropertyKeys.Device.Characteristics
DEVPKEY_Device_Address = DevicePropertyKeys.Device.Address
DEVPKEY_Device_UINumberDescFormat = DevicePropertyKeys.Device.UINumberDescFormat
DEVPKEY_Device_PowerData = DevicePropertyKeys.Device.PowerData
DEVPKEY_Device_RemovalPolicy = DevicePropertyKeys.Device.RemovalPolicy
DEVPKEY_Device_RemovalPolicyDefault = DevicePropertyKeys.Device.RemovalPolicyDefault
DEVPKEY_Device_RemovalPolicyOverride = DevicePropertyKeys.Device.RemovalPolicyOverride
DEVPKEY_Device_InstallState = DevicePropertyKeys.Device.InstallState
DEVPKEY_Device_LocationPaths = DevicePropertyKeys.Device.LocationPaths
DEVPKEY_Device_BaseContainerId = DevicePropertyKeys.Device.BaseContainerId
DEVPKEY_Device_DevNodeStatus = DevicePropertyKeys.Device.DevNodeStatus
DEVPKEY_Device_ProblemCode = DevicePropertyKeys.Device.ProblemCode
DEVPKEY_Device_EjectionRelations = DevicePropertyKeys.Device.EjectionRelations
DEVPKEY_Device_RemovalRelations = DevicePropertyKeys.Device.RemovalRelations
DEVPKEY_Device_PowerRelations = DevicePropertyKeys.Device.PowerRelations
DEVPKEY_Device_BusRelations = DevicePropertyKeys.Device.BusRelations
DEVPKEY_Device_Parent = DevicePropertyKeys.Device.Parent
DEVPKEY_Device_Children = DevicePropertyKeys.Device.Children
DEVPKEY_Device_Siblings = DevicePropertyKeys.Device.Siblings
DEVPKEY_Device_TransportRelations = DevicePropertyKeys.Device.TransportRelations
DEVPKEY_Device_Reported = DevicePropertyKeys.Device.Reported
DEVPKEY_Device_Legacy = DevicePropertyKeys.Device.Legacy
DEVPKEY_Device_InstanceId = DevicePropertyKeys.Device.InstanceId
DEVPKEY_Device_ContainerId = DevicePropertyKeys.Device.ContainerId
DEVPKEY_Device_ModelId = DevicePropertyKeys.Device.ModelId
DEVPKEY_Device_FriendlyNameAttributes = DevicePropertyKeys.Device.FriendlyNameAttributes
DEVPKEY_Device_ManufacturerAttributes = DevicePropertyKeys.Device.ManufacturerAttributes
DEVPKEY_Device_PresenceNotForDevice = DevicePropertyKeys.Device.PresenceNotForDevice
# noinspection SpellCheckingInspection
DEVPKEY_Device_DHP_Rebalance_Policy = DevicePropertyKeys.Device.DHP_Rebalance_Policy
# noinspection SpellCheckingInspection
DEVPKEY_Device_Numa_Node = DevicePropertyKeys.Device.Numa_Node
DEVPKEY_Device_BusReportedDeviceDesc = DevicePropertyKeys.Device.BusReportedDeviceDesc
DEVPKEY_Device_SessionId = DevicePropertyKeys.Device.SessionId
DEVPKEY_Device_InstallDate = DevicePropertyKeys.Device.InstallDate
DEVPKEY_Device_FirstInstallDate = DevicePropertyKeys.Device.FirstInstallDate
DEVPKEY_Device_DriverDate = DevicePropertyKeys.Device.DriverDate
DEVPKEY_Device_DriverVersion = DevicePropertyKeys.Device.DriverVersion
DEVPKEY_Device_DriverDesc = DevicePropertyKeys.Device.DriverDesc
DEVPKEY_Device_DriverInfPath = DevicePropertyKeys.Device.DriverInfPath
DEVPKEY_Device_DriverInfSection = DevicePropertyKeys.Device.DriverInfSection
DEVPKEY_Device_DriverInfSectionExt = DevicePropertyKeys.Device.DriverInfSectionExt
DEVPKEY_Device_MatchingDeviceId = DevicePropertyKeys.Device.MatchingDeviceId
DEVPKEY_Device_DriverProvider = DevicePropertyKeys.Device.DriverProvider
DEVPKEY_Device_DriverPropPageProvider = DevicePropertyKeys.Device.DriverPropPageProvider
DEVPKEY_Device_DriverCoInstallers = DevicePropertyKeys.Device.DriverCoInstallers
DEVPKEY_Device_ResourcePickerTags = DevicePropertyKeys.Device.ResourcePickerTags
DEVPKEY_Device_ResourcePickerExceptions = DevicePropertyKeys.Device.ResourcePickerExceptions
DEVPKEY_Device_DriverRank = DevicePropertyKeys.Device.DriverRank
DEVPKEY_Device_DriverLogoLevel = DevicePropertyKeys.Device.DriverLogoLevel
DEVPKEY_Device_NoConnectSound = DevicePropertyKeys.Device.NoConnectSound
DEVPKEY_Device_GenericDriverInstalled = DevicePropertyKeys.Device.GenericDriverInstalled
DEVPKEY_Device_AdditionalSoftwareRequested = DevicePropertyKeys.Device.AdditionalSoftwareRequested
DEVPKEY_Device_SafeRemovalRequired = DevicePropertyKeys.Device.SafeRemovalRequired
DEVPKEY_Device_SafeRemovalRequiredOverride = DevicePropertyKeys.Device.SafeRemovalRequiredOverride

DEVPKEY_DriverPackage_Model = DevicePropertyKeys.DriverPackage.Model
DEVPKEY_DriverPackage_VendorWebSite = DevicePropertyKeys.DriverPackage.VendorWebSite
DEVPKEY_DriverPackage_DetailedDescription = DevicePropertyKeys.DriverPackage.DetailedDescription
DEVPKEY_DriverPackage_DocumentationLink = DevicePropertyKeys.DriverPackage.DocumentationLink
DEVPKEY_DriverPackage_Icon = DevicePropertyKeys.DriverPackage.Icon
DEVPKEY_DriverPackage_BrandingIcon = DevicePropertyKeys.DriverPackage.BrandingIcon

DEVPKEY_DeviceClass_UpperFilters = DevicePropertyKeys.DeviceClass.UpperFilters
DEVPKEY_DeviceClass_LowerFilters = DevicePropertyKeys.DeviceClass.LowerFilters
DEVPKEY_DeviceClass_Security = DevicePropertyKeys.DeviceClass.Security
DEVPKEY_DeviceClass_SecuritySDS = DevicePropertyKeys.DeviceClass.SecuritySDS
DEVPKEY_DeviceClass_DevType = DevicePropertyKeys.DeviceClass.DevType
DEVPKEY_DeviceClass_Exclusive = DevicePropertyKeys.DeviceClass.Exclusive
DEVPKEY_DeviceClass_Characteristics = DevicePropertyKeys.DeviceClass.Characteristics
DEVPKEY_DeviceClass_Name = DevicePropertyKeys.DeviceClass.Name
DEVPKEY_DeviceClass_ClassName = DevicePropertyKeys.DeviceClass.ClassName
DEVPKEY_DeviceClass_Icon = DevicePropertyKeys.DeviceClass.Icon
DEVPKEY_DeviceClass_ClassInstaller = DevicePropertyKeys.DeviceClass.ClassInstaller
DEVPKEY_DeviceClass_PropPageProvider = DevicePropertyKeys.DeviceClass.PropPageProvider
DEVPKEY_DeviceClass_NoInstallClass = DevicePropertyKeys.DeviceClass.NoInstallClass
DEVPKEY_DeviceClass_NoDisplayClass = DevicePropertyKeys.DeviceClass.NoDisplayClass
DEVPKEY_DeviceClass_SilentInstall = DevicePropertyKeys.DeviceClass.SilentInstall
DEVPKEY_DeviceClass_NoUseClass = DevicePropertyKeys.DeviceClass.NoUseClass
DEVPKEY_DeviceClass_DefaultService = DevicePropertyKeys.DeviceClass.DefaultService
DEVPKEY_DeviceClass_IconPath = DevicePropertyKeys.DeviceClass.IconPath
# noinspection SpellCheckingInspection
DEVPKEY_DeviceClass_DHPRebalanceOptOut = DevicePropertyKeys.DeviceClass.DHPRebalanceOptOut
DEVPKEY_DeviceClass_ClassCoInstallers = DevicePropertyKeys.DeviceClass.ClassCoInstallers

DEVPKEY_DeviceInterface_FriendlyName = DevicePropertyKeys.DeviceInterface.FriendlyName
DEVPKEY_DeviceInterface_Enabled = DevicePropertyKeys.DeviceInterface.Enabled
DEVPKEY_DeviceInterface_ClassGuid = DevicePropertyKeys.DeviceInterface.ClassGuid

DEVPKEY_DeviceInterfaceClass_DefaultInterface = DevicePropertyKeys.DeviceInterfaceClass.DefaultInterface

DEVPKEY_DeviceDisplay_IsShowInDisconnectedState = DevicePropertyKeys.DeviceDisplay.IsShowInDisconnectedState
DEVPKEY_DeviceDisplay_IsNotInterestingForDisplay = DevicePropertyKeys.DeviceDisplay.IsNotInterestingForDisplay
DEVPKEY_DeviceDisplay_Category = DevicePropertyKeys.DeviceDisplay.Category
# noinspection SpellCheckingInspection
DEVPKEY_DeviceDisplay_UnpairUninstall = DevicePropertyKeys.DeviceDisplay.UnpairUninstall
DEVPKEY_DeviceDisplay_RequiresUninstallElevation = DevicePropertyKeys.DeviceDisplay.RequiresUninstallElevation
DEVPKEY_DeviceDisplay_AlwaysShowDeviceAsConnected = DevicePropertyKeys.DeviceDisplay.AlwaysShowDeviceAsConnected
