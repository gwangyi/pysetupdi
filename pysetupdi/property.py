# noinspection SpellCheckingInspection
"""mod:`pysetupdi.property` - DEVPROP parser

Parsing given devprop buffer and type and return python object
"""
from .constants import *
from .structures import GUID, DevicePropertyKey

import typing
import array
import struct
import ctypes
import datetime

# noinspection SpellCheckingInspection
_oleaut32 = ctypes.WinDLL('oleaut32')
_kernel32 = ctypes.WinDLL('kernel32')


class Property(object):
    """Property parser class"""
    _property_type = dict()  # type: typing.Dict[int, (bytes,) -> object]
    """Property parser objects are placed in this class property"""

    def __new__(cls, buffer, prop_type):
        # noinspection SpellCheckingInspection
        """
        Parse devprop property

        :param buffer: given byte buffer
        :type buffer: bytes
        :param prop_type: DEVPROP_TYPE_xxx type
        :type prop_type: int | DevicePropertyType
        :return: python object
        """
        return Property._property_type[prop_type](buffer)

    @classmethod
    def add_parser(cls, prop_type, length=None, func=None):
        # noinspection SpellCheckingInspection
        """
        Add DEVPROP_TYPE_xxx handler

        :param prop_type: DEVPROP_TYPE_xxx type
        :type prop_type: int | DevicePropertyType
        :param length: If specified, given prop_type support DEVPROP_TYPEMOD_ARRAY modifier and
            unit size is given value
        :type length: None | int
        :param func: real parser
        :type func: (bytes,) -> object
        """
        def decorator(f):
            cls._property_type[prop_type] = f
            if length is not None:
                def array_parser(buffer):
                    return list(f(buffer[i:i+length] for i in range(0, len(buffer), length)))

                cls._property_type[prop_type | DEVPROP_TYPEMOD_ARRAY] = array_parser

            return f

        if func is None:
            return decorator
        else:
            return decorator(func)


def _add_parsers():
    """Add default parsers
    To make each parser be hidden to other modules, each parsers are defined as local function of this function"""

    # noinspection PyUnusedLocal
    @Property.add_parser(DEVPROP_TYPE_EMPTY)
    def empty_parser(buffer):
        # noinspection SpellCheckingInspection
        """DEVPROP_TYPE_EMPTY parser

        Actually, in this case, the attribute does not exists, so it raises `AttributeError`"""
        raise AttributeError("Empty property")

    # noinspection PyUnusedLocal
    @Property.add_parser(DEVPROP_TYPE_NULL)
    def null_parser(buffer):
        # noinspection SpellCheckingInspection
        """DEVPROP_TYPE_NULL parser"""
        return None

    # noinspection SpellCheckingInspection
    @Property.add_parser(DEVPROP_TYPE_SBYTE)
    def sbyte_parser(buffer):
        """DEVPROP_TYPE_SBYTE parser

        Every element of default python byte array is signed byte, so just return first element"""
        return buffer[0]

    # noinspection SpellCheckingInspection
    @Property.add_parser(DEVPROP_TYPE_SBYTE | DEVPROP_TYPEMOD_ARRAY)
    @Property.add_parser(DEVPROP_TYPE_SECURITY_DESCRIPTOR)
    def sbyte_array_parser(buffer):
        """DEVPROP_TYPE_BINARY parser

        Although SECURITY_DESCRIPTOR need to its own parser, the structure of it varies to windows versions and it is
        not used so frequently. So, it handles same as bytes
        """
        return buffer

    @Property.add_parser(DEVPROP_TYPE_BYTE)
    def byte_parser(buffer):
        # noinspection SpellCheckingInspection
        """DEVPROP_TYPE_BYTE parser

        Default python bytes is signed, so to use given bytes as an unsigned byte value, truncate bits above 8th."""
        return buffer[0] & 255

    # noinspection SpellCheckingInspection
    @Property.add_parser(DEVPROP_TYPE_BYTE | DEVPROP_TYPEMOD_ARRAY)
    def sbyte_array_parser(buffer):
        """DEVPROP_TYPE_BYTE | DEVPROP_TYPEMOD_ARRAY parser

        Default python bytes is signed, so to use given bytes as an unsigned byte value, truncate bits above 8th."""
        return tuple(n & 255 for n in buffer)

    def add_simple_type_parser(prop_type, fmt):
        def simple_parser(buffer):
            return array.array(fmt, buffer)[0]

        def array_parser(buffer):
            return list(array.array(fmt, buffer))

        Property.add_parser(prop_type)(simple_parser)
        Property.add_parser(prop_type | DEVPROP_TYPEMOD_ARRAY)(array_parser)

    def add_simple_type_parsers(fmt_map):
        for prop_type in fmt_map:
            fmt = fmt_map[prop_type]
            add_simple_type_parser(prop_type, fmt)

    add_simple_type_parsers({
        DEVPROP_TYPE_INT16: 'h',
        DEVPROP_TYPE_UINT16: 'H',
        DEVPROP_TYPE_INT32: 'l',
        DEVPROP_TYPE_UINT32: 'L',
        DEVPROP_TYPE_INT64: 'q',
        DEVPROP_TYPE_UINT64: 'Q',
        DEVPROP_TYPE_FLOAT: 'f',
        DEVPROP_TYPE_DOUBLE: 'd',
        DEVPROP_TYPE_DEVPROPKEY: 'L',
    })

    @Property.add_parser(DEVPROP_TYPE_DECIMAL, length=16)
    def decimal_parser(buffer):
        # noinspection SpellCheckingInspection
        scale, sign, hi, lo = struct.unpack("xxBBHQ", buffer[:16])
        val = (hi << 64) | lo
        val *= 1 if sign & 0x80 == 0 else -1
        return val / (10 ** scale)

    @Property.add_parser(DEVPROP_TYPE_GUID, length=16)
    def guid_parser(buffer):
        return GUID(buffer[:16])

    @Property.add_parser(DEVPROP_TYPE_CURRENCY, length=8)
    def currency_parser(buffer):
        return struct.unpack('Q', buffer[:8])[0] / 10000

    @Property.add_parser(DEVPROP_TYPE_DATE, length=8)
    def date_parser(buffer):
        t = struct.unpack('d', buffer[:8])[0]
        buf = ctypes.create_string_buffer(16)
        _oleaut32.VartiantTimeToSystemTime(t, ctypes.byref(buf))
        y, m, _, d, hh, mm, ss, ms = struct.unpack("8H", bytes(buf))
        return datetime.datetime(y, m, d, hh, mm, ss, ms * 1000)

    @Property.add_parser(DEVPROP_TYPE_FILETIME, length=8)
    def filetime_parser(buffer):
        buf = ctypes.create_string_buffer(16)
        _kernel32.FileTimeToSystemTime(buffer[:8], ctypes.byref(buf))
        y, m, _, d, hh, mm, ss, ms = struct.unpack("8H", bytes(buf))
        return datetime.datetime(y, m, d, hh, mm, ss, ms * 1000)

    @Property.add_parser(DEVPROP_TYPE_BOOLEAN, length=1)
    def boolean_parser(buffer):
        return buffer[0] != 0

    @Property.add_parser(DEVPROP_TYPE_STRING)
    @Property.add_parser(DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING)
    @Property.add_parser(DEVPROP_TYPE_STRING_INDIRECT)
    def string_parser(buffer):
        return buffer.decode('utf-16').split('\0', 1)[0]

    @Property.add_parser(DEVPROP_TYPE_STRING_LIST)
    @Property.add_parser(DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING | DEVPROP_TYPEMOD_LIST)
    def string_list_parser(buffer):
        return buffer.decode('utf-16').strip('\0\0').split('\0')

    # noinspection SpellCheckingInspection
    @Property.add_parser(DEVPROP_TYPE_DEVPROPKEY, length=ctypes.sizeof(DevicePropertyKey))
    def devpropkey_parser(buffer):
        return DevicePropertyKey.from_buffer(bytearray(buffer))

    @Property.add_parser(DEVPROP_TYPE_ERROR)
    def error_parser(buffer):
        err_no = struct.unpack("l", buffer[:4])
        return err_no, ctypes.FormatError(err_no)

    @Property.add_parser(DEVPROP_TYPE_ERROR | DEVPROP_TYPEMOD_ARRAY)
    def error_array_parser(buffer):
        return list((err_no, ctypes.FormatError(err_no)) for err_no in array.array('l', buffer))

    # noinspection SpellCheckingInspection
    def _ntstatus_format_error(ntstatus):
        if ntstatus > 0x80000000:
            ntstatus -= 0x100000000
        msg_ptr = ctypes.c_wchar_p()
        ntdll = _kernel32.LoadLibraryW('NTDLL.DLL')
        try:
            _kernel32.FormatMessageW(FORMAT_MESSAGE_ALLOCATE_BUFFER |
                                     FORMAT_MESSAGE_FROM_SYSTEM |
                                     FORMAT_MESSAGE_FROM_HMODULE,
                                     ntdll, ntstatus, 0x0400,  # LANG_NEUTRAL, SUBLANG_DEFAULT
                                     ctypes.byref(msg_ptr), 0, None)
            return msg_ptr.value.replace("\r\n", "\n").strip("\n")
        finally:
            if msg_ptr.value is not None:
                _kernel32.LocalFree(msg_ptr)
            _kernel32.FreeLibrary(ntdll)

    # noinspection SpellCheckingInspection
    @Property.add_parser(DEVPROP_TYPE_NTSTATUS)
    def ntstatus_parser(buffer):
        err_no = struct.unpack("l", buffer[:4])[0]
        return err_no, _ntstatus_format_error(err_no)

    # noinspection SpellCheckingInspection
    @Property.add_parser(DEVPROP_TYPE_NTSTATUS | DEVPROP_TYPEMOD_ARRAY)
    def ntstatus_array_parser(buffer):
        return list((err_no, _ntstatus_format_error(err_no)) for err_no in array.array('l', buffer))

_add_parsers()
