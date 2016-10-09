# pysetupdi
Python SetupAPI Wrapper

`devices` function generates iterable of Devices which is selected by given parameters. The parameters of `devices`
is similar to SetupDiGetClassDevs. Properties of each device can be accessed by accessing pre-defined properties or
giving DevicePropertyKey object as an index to device object.

~~~python
hard_disk_drives = devices('{4d36e967-e325-11ce-bfc1-08002be10318}')
for hard_disk_drive in hard_disk_drives:
    print(hard_disk_drive.device_desc)
~~~

You can also query information about devices by console command

~~~
C:\> pysetupdi -g {4d36e967-e325-11ce-bfc1-08002be10318} list
C:\> pysetupdi -i "SCSI\DISK&VEN_SAMSUN_&PROD_MZNTE256HMHP-000\4&103D1686&0&000000" get pdo_name
~~~
