from typing import *
from .structures import GUID, DevicePropertyKey
from .constants import DiGetClassDevsFlags, DIGCF_PRESENT
from datetime import datetime

class Device(object):
    device_desc = ...  # type: str
    hardware_id = ...  # type: List[str]
    compatible_ids = ...  # type: List[str]
    service = ...  # type: str
    device_class = ...  # type: str
    class_guid = ...  # type: GUID
    driver = ...  # type: str
    config_flags = ...  # type: int
    manufacturer = ...  # type: str
    friendly_name = ...  # type: str
    location_info = ...  # type: str
    pdo_name = ...  # type: str
    capabilities = ...  # type: int
    ui_number = ...  # type: str
    upper_filters = ...  # type: List[str]
    lower_filters = ...  # type: List[str]
    bus_type_guid = ...  # type: GUID
    legacy_bus_type = ...  # type: int
    bus_number = ...  # type: int
    enumerator_name = ...  # type: str
    security = ...  # type: bytes
    security_sds = ...  # type: str
    dev_type = ...  # type: int
    exclusive = ...  # type: bool
    characteristics = ...  # type: int
    address = ...  # type: int
    ui_number_desc_format = ...  # type: str
    power_data = ...  # type: bytes
    removal_policy = ...  # type: int
    removal_policy_default = ...  # type: int
    removal_policy_override = ...  # type: int
    install_state = ...  # type: int
    location_paths = ...  # type: List[str]
    base_container_id = ...  # type: GUID
    dev_node_status = ...  # type: int
    problem_code = ...  # type: int
    ejection_relations = ...  # type: List[str]
    removal_relations = ...  # type: List[str]
    power_relations = ...  # type: List[str]
    bus_relations = ...  # type: List[str]
    parent = ...  # type: Device
    children = ...  # type: List[Device]
    siblings = ...  # type: List[Device]
    transport_relations = ...  # type: List[str]
    reported = ...  # type: bool
    legacy = ...  # type: bool
    instance_id = ...  # type: str
    container_id = ...  # type: GUID
    model_id = ...  # type: GUID
    friendly_name_attributes = ...  # type: int
    manufacturer_attributes = ...  # type: int
    presence_not_for_device = ...  # type: bool
    # noinspection SpellCheckingInspection
    dhp_rebalance_policy = ...  # type: int
    # noinspection SpellCheckingInspection
    numa_node = ...  # type: int
    bus_reported_device_desc = ...  # type: str
    session_id = ...  # type: int
    install_date = ...  # type: datetime
    first_install_date = ...  # type: datetime
    driver_date = ...  # type: datetime
    driver_version = ...  # type: str
    driver_desc = ...  # type: str
    driver_inf_path = ...  # type: str
    driver_inf_section = ...  # type: str
    driver_inf_section_ext = ...  # type: str
    matching_device_id = ...  # type: str
    driver_provider = ...  # type: str
    driver_prop_page_provider = ...  # type: str
    driver_co_installers = ...  # type: List[str]
    resource_picker_tags = ...  # type: str
    resource_picker_exceptions = ...  # type: str
    driver_rank = ...  # type: int
    driver_logo_level = ...  # type: int
    no_connect_sound = ...  # type: bool
    generic_driver_installed = ...  # type: bool
    additional_software_requested = ...  # type: bool
    safe_removal_required = ...  # type: bool
    safe_removal_required_override = ...  # type: bool
    path = ...  # type: str

    def __init__(self, instance_id: str):
        self._instance_id = instance_id
        self._handle = None

    def open(self):
        pass

    def get_property(self, key: DevicePropertyKey):
        pass

    def __getitem__(self, item:DevicePropertyKey):
        pass

    def get_property_keys(self) -> List[DevicePropertyKey]:
        pass

def devices(guid: str=None, enumerator: str=None, hwnd_parent: int=None,
            flags: Union[DiGetClassDevsFlags, int]=DIGCF_PRESENT) -> Iterable[Device]:
    ...