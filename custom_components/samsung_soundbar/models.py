from dataclasses import dataclass

from .pysmartthings_0_7_8 import SmartThings

from .api_extension.SoundbarDevice import SoundbarDevice


@dataclass
class DeviceConfig:
    config: dict
    device: SoundbarDevice


@dataclass
class SoundbarConfig:
    api: SmartThings
    devices: dict
