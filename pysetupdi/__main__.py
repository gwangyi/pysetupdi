from pysetupdi import devices, Device
from pysetupdi.constants import DevicePropertyKeys, DiGetClassDevsFlags
from pysetupdi.structures import DevicePropertyKey
from optparse import OptionParser
import re


class ArgumentLengthNotMatchedError(RuntimeError):
    pass


def convert(name):
    s1 = re.sub('(?<=[0-9A-Z])([A-Z][a-z]+)', r'_\1', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# noinspection SpellCheckingInspection
def main():
    parser = OptionParser(usage="Usage: {}".format("\n       ".join(
        ["%prog [options] list",
         "%prog [options] keys",
         "%prog [options] print",
         "%prog [options] get predefined-key-name",
         "%prog [options] get propkey-fmtid propkey-pid"])))
    parser.add_option("-g", "--class-guid", dest="class_guid",
                      help="Specify class guid ({xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}). "
                           "Ignored when get command")
    parser.add_option("-e", "--enumerator", dest="enumerator",
                      help="Specify enumerator. Ignored when get command")
    parser.add_option("-i", "--instance-id", dest="instance_id",
                      help="Specify device by instance id. Valid when get command only")
    parser.add_option("-d", "--default", dest="default", action="store_true",
                      help="Return only the device that is associated with the system default device "
                           "interface, if one is set, for the specified device interface classes. (DIGCF_DEFAULT)")
    parser.add_option('-D', '--no-default', dest="default", action="store_false")
    parser.add_option("-p", "--present", dest="present", action="store_true", default=True,
                      help="Return only devices that are currently present in a system. (DIGCF_PRESENT)")
    parser.add_option('-P', '--no-present', dest="present")
    parser.add_option("-a", "--all-classes", dest="all_classes", action="store_true",
                      help="Return a list of installed devices for all device setup classes or all device "
                           "interface classes. (DIGCF_ALLCLASSES)")
    parser.add_option("-f", "--profile", dest="profile", action="store_true",
                      help="Return only devices that are a part of the current hardware profile. "
                           "(DIGCF_PROFILE)")
    parser.add_option("-n", "--device-interface", dest="device_interface", action="store_true",
                      help="Return devices that support device interfaces for the specified device "
                           "interface classes. This flag must be set in the Flags parameter if the"
                           "Enumerator parameter specifies a device instance ID. (DIGCF_DEVICEINTERFACE)")
    parser.add_option("-1", dest="just_one", action="store_true",
                      help="Handle first device only")

    (options, args) = parser.parse_args()

    try:
        if len(args) == 0:
            raise ArgumentLengthNotMatchedError()

        flag = 0
        if options.default:
            flag |= DiGetClassDevsFlags.Default
        if options.present:
            flag |= DiGetClassDevsFlags.Present
        if options.all_classes:
            flag |= DiGetClassDevsFlags.AllClasses
        if options.profile:
            flag |= DiGetClassDevsFlags.Profile
        if options.device_interface:
            flag |= DiGetClassDevsFlags.DeviceInterface

        if args[0] == 'list':
            for dev in devices(guid=options.class_guid, enumerator=options.enumerator, flags=flag):
                print("{}: {}".format(str(dev), dev.instance_id))
                if options.just_one:
                    break

        elif args[0] == 'keys':
            if len(args) != 1:
                raise ArgumentLengthNotMatchedError()

            dev = Device(options.instance_id)
            for key in dev.get_property_keys():
                is_predefined = False
                for predefined_name in dir(DevicePropertyKeys.Device):
                    predefined = getattr(DevicePropertyKeys.Device, predefined_name, None)
                    if isinstance(predefined, DevicePropertyKey):
                        if key == predefined:
                            is_predefined = True
                            print("{}".format(convert(predefined.name.split('_', 2)[-1])))
                if not is_predefined:
                    print("{}".format(str(key)))
        elif args[0] == 'print':
            if len(args) != 1:
                raise ArgumentLengthNotMatchedError()

            for dev in devices(guid=options.class_guid, enumerator=options.enumerator, flags=flag):
                print("Device: {}".format(str(dev)))
                for key in dev.get_property_keys():
                    is_predefined = False
                    key_name = None
                    for predefined_name in dir(DevicePropertyKeys.Device):
                        predefined = getattr(DevicePropertyKeys.Device, predefined_name, None)
                        if isinstance(predefined, DevicePropertyKey):
                            if key == predefined:
                                is_predefined = True
                                key_name = convert(predefined.name.split('_', 2)[-1])
                    if not is_predefined:
                        key_name = str(key)

                    if key == DevicePropertyKeys.Device.Parent:
                        print("  {}: {}".format(key_name, repr(dev.parent)))
                    elif key in (DevicePropertyKeys.Device.Children, DevicePropertyKeys.Device.Siblings):
                        print("  {}:".format(key_name))
                        for subdev in dev.get_property(key):
                            print("    - {}".format(repr(Device(subdev))))
                    else:
                        prop = dev.get_property(key)
                        if hasattr(prop, '__iter__') and not isinstance(prop, (str, bytes)):
                            print("  {}:".format(key_name))
                            for item in prop:
                                if isinstance(item, (str, bytes)):
                                    print("    - {}".format(item))
                                else:
                                    print("    - {}".format(repr(item)))
                        elif isinstance(prop, (str, bytes)):
                            print("  {}: {}".format(key_name, prop))
                        else:
                            print("  {}: {}".format(key_name, repr(prop)))
                if options.just_one:
                    break
        elif args[0] == 'get':
            key = None
            if len(args) == 2:
                for predefined_name in dir(DevicePropertyKeys.Device):
                    predefined = getattr(DevicePropertyKeys.Device, predefined_name, None)
                    if isinstance(predefined, DevicePropertyKey):
                        key_name = convert(predefined.name.split('_', 2)[-1])
                        if args[1] == key_name:
                            key = predefined
                            break
                if key is None:
                    raise AttributeError("Given key {} is unknown".format(args[1]))
            elif len(args) == 3:
                key = DevicePropertyKey(args[1], args[2])
            else:
                raise ArgumentLengthNotMatchedError

            device = Device(options.instance_id)
            print(device.get_property(key))

    except ArgumentLengthNotMatchedError:
        parser.print_help()
        exit(2)


if __name__ == "__main__":
    main()
