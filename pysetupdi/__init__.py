# noinspection SpellCheckingInspection
"""pysetupdi: SetupDi API wrapper for python

``devices`` function generates iterable of Devices which is selected by given parameters. The parameters of ``devices``
is similar to SetupDiGetClassDevs. Properties of each device can be accessed by accessing pre-defined properties or
giving DevicePropertyKey object as an index to device object.

>>> hard_disk_drives = devices('{4d36e967-e325-11ce-bfc1-08002be10318}')
>>> for hard_disk_drive in hard_disk_drives:
...     print(hard_disk_drive.device_desc)
"""

from .setupdi import devices, Device
