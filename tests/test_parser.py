from uuid import UUID

import pytest
from bleak.backends.device import BLEDevice
from bluetooth_data_tools import monotonic_time_coarse
from bluetooth_sensor_state_data import SensorUpdate
from habluetooth import BluetoothServiceInfoBleak
from sensor_state_data import (
    BinarySensorDescription,
    BinarySensorDeviceClass,
    BinarySensorValue,
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from thermobeacon_ble.parser import ThermoBeaconBluetoothDeviceData


def make_bluetooth_service_info(  # noqa: PLR0913
    name: str,
    manufacturer_data: dict[int, bytes],
    service_uuids: list[str],
    address: str,
    rssi: int,
    service_data: dict[UUID, bytes],
    source: str,
    tx_power: int = 0,
    raw: bytes | None = None,
) -> BluetoothServiceInfoBleak:
    return BluetoothServiceInfoBleak(
        name=name,
        manufacturer_data=manufacturer_data,
        service_uuids=service_uuids,
        address=address,
        rssi=rssi,
        service_data=service_data,
        source=source,
        device=BLEDevice(
            name=name,
            address=address,
            details={},
            rssi=rssi,
        ),
        time=monotonic_time_coarse(),
        advertisement=None,
        connectable=True,
        tx_power=tx_power,
        raw=raw,
    )


def test_can_create():
    ThermoBeaconBluetoothDeviceData()


MFR_16_LEN_18 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        16: b"\x00\x00\x9c\r\x00\x00\xfeDE\x0c\xc5\x01\x87\x02\x17\x00\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)

MFR_16_LEN_20 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        16: b"\x00\x00\xb0\x02\x00\x00G\xa4\xe2\x0c\x80\x01\xb6\x02J\x00\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)

MFR_48 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        48: b"\x00\x00\x8b\x01\x00\x00]D\xd6\x0bY\x01Y\x03D\x00\x0c\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)
MFR_48_RAW = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={48: b""},
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
    raw=b"\x15\xff\x30\x00\x00\x00\x8b\x01\x00\x00\x5d\x44\xd6\x0b\x59\x01\x59\x03\x44\x00\x0c\x00",
)

MFR_20 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        20: b"\x00\x00\x05\x03\x00\x00\xf5\xeb3\rV\x01<\x03L\x03\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)

MFR_22 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        21: b"\x00\x00\xf0\x05\x00\x00\xd7n\xbe\x01e\x00\x00\x00\xa7\x01\x00\x00\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)

MFR_24 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        24: b"\x00\x00\xf0\x05\x00\x00\xd7n\xbe\x01e\x00\x00\x00\xa7\x01\x00\x00\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)

MFR_27 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    service_data={},
    manufacturer_data={
        27: b"\x00\x00\x83,\x00\x00\xd0c\x82\x0co\x01s\x02\x05#\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    rssi=-44,
    source="local",
)

BAD_DATA = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        16: b"a\x00\x16\x00\x00\xac\xfa/\x0b&\x01G\x03\xa7\xe7\x12\x00\xc0"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)
BAD_DATA_2 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        16: b"\x00\x00\x16\x00\x00\xac\xfa/\x0b&\x01G\x03\xa7\xe7\x12\x00\xc0"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)
BAD_DATA_3 = make_bluetooth_service_info(
    name="ThermoBeacon",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    manufacturer_data={
        16: b"\x00\x00)\x06\x00\x00Eo\xab\x01\n\x00\x00\x00\xa2\x01\x98\x00\x00\x00"
    },
    service_uuids=["0000fff0-0000-1000-8000-00805f9b34fb"],
    source="local",
)


def test_with_22_byte_update():
    parser = ThermoBeaconBluetoothDeviceData()
    assert parser.supported(MFR_22) is True
    assert parser.title == "Smart hygrometer EEFF"


def test_supported_set_the_title():
    parser = ThermoBeaconBluetoothDeviceData()
    assert parser.supported(MFR_16_LEN_20) is True
    assert parser.title == "Lanyard/mini hygrometer EEFF"


def test_supported_set_the_title_18_bytes():
    parser = ThermoBeaconBluetoothDeviceData()
    assert parser.supported(MFR_16_LEN_18) is True
    assert parser.title == "Lanyard/mini hygrometer EEFF"


def test_20_byte_update():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_16_LEN_20)
    assert update == SensorUpdate(
        title="Lanyard/mini hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Lanyard/mini hygrometer EEFF",
                model=16,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="voltage", device_id=None): SensorDescription(
                device_key=DeviceKey(key="voltage", device_id=None),
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=43.38,
            ),
            DeviceKey(key="voltage", device_id=None): SensorValue(
                device_key=DeviceKey(key="voltage", device_id=None),
                name="Voltage",
                native_value=3.3,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=24.0,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="occupancy", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="occupancy", device_id=None),
                device_class=BinarySensorDeviceClass.OCCUPANCY,
            )
        },
        binary_entity_values={
            DeviceKey(key="occupancy", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="occupancy", device_id=None),
                name="Occupancy",
                native_value=False,
            )
        },
    )


def test_18_byte_update():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_16_LEN_18)
    assert update == SensorUpdate(
        title="Lanyard/mini hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Lanyard/mini hygrometer EEFF",
                model=16,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="voltage", device_id=None): SensorDescription(
                device_key=DeviceKey(key="voltage", device_id=None),
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=40.44,
            ),
            DeviceKey(key="voltage", device_id=None): SensorValue(
                device_key=DeviceKey(key="voltage", device_id=None),
                name="Voltage",
                native_value=3.14,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=28.31,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="occupancy", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="occupancy", device_id=None),
                device_class=BinarySensorDeviceClass.OCCUPANCY,
            )
        },
        binary_entity_values={
            DeviceKey(key="occupancy", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="occupancy", device_id=None),
                name="Occupancy",
                native_value=False,
            )
        },
    )


def test_mfr_27():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_27)
    assert update == SensorUpdate(
        title="Smart hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Smart hygrometer EEFF",
                model=27,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="voltage", device_id=None): SensorDescription(
                device_key=DeviceKey(key="voltage", device_id=None),
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=22.94,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=39.19,
            ),
            DeviceKey(key="voltage", device_id=None): SensorValue(
                device_key=DeviceKey(key="voltage", device_id=None),
                name="Voltage",
                native_value=3.2,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-44,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="occupancy", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="occupancy", device_id=None),
                device_class=BinarySensorDeviceClass.OCCUPANCY,
            )
        },
        binary_entity_values={
            DeviceKey(key="occupancy", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="occupancy", device_id=None),
                name="Occupancy",
                native_value=False,
            )
        },
        events={},
    )


def test_mfr_48():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_48)
    assert update == SensorUpdate(
        title="Smart hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Smart hygrometer EEFF",
                model=48,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="voltage", device_id=None): SensorDescription(
                device_key=DeviceKey(key="voltage", device_id=None),
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=21.56,
            ),
            DeviceKey(key="voltage", device_id=None): SensorValue(
                device_key=DeviceKey(key="voltage", device_id=None),
                name="Voltage",
                native_value=3.03,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=53.56,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="occupancy", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="occupancy", device_id=None),
                device_class=BinarySensorDeviceClass.OCCUPANCY,
            )
        },
        binary_entity_values={
            DeviceKey(key="occupancy", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="occupancy", device_id=None),
                name="Occupancy",
                native_value=False,
            )
        },
        events={},
    )


def test_mfr_48_raw():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_48_RAW)
    assert update == SensorUpdate(
        title="Smart hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Smart hygrometer EEFF",
                model=48,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="voltage", device_id=None): SensorDescription(
                device_key=DeviceKey(key="voltage", device_id=None),
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=21.56,
            ),
            DeviceKey(key="voltage", device_id=None): SensorValue(
                device_key=DeviceKey(key="voltage", device_id=None),
                name="Voltage",
                native_value=3.03,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=53.56,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="occupancy", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="occupancy", device_id=None),
                device_class=BinarySensorDeviceClass.OCCUPANCY,
            )
        },
        binary_entity_values={
            DeviceKey(key="occupancy", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="occupancy", device_id=None),
                name="Occupancy",
                native_value=False,
            )
        },
        events={},
    )


def test_mfr_20():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_20)
    assert update == SensorUpdate(
        title="Smart hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Smart hygrometer EEFF",
                model=20,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="voltage", device_id=None): SensorDescription(
                device_key=DeviceKey(key="voltage", device_id=None),
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=21.38,
            ),
            DeviceKey(key="voltage", device_id=None): SensorValue(
                device_key=DeviceKey(key="voltage", device_id=None),
                name="Voltage",
                native_value=3.38,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=51.75,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="occupancy", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="occupancy", device_id=None),
                device_class=BinarySensorDeviceClass.OCCUPANCY,
            )
        },
        binary_entity_values={
            DeviceKey(key="occupancy", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="occupancy", device_id=None),
                name="Occupancy",
                native_value=False,
            )
        },
        events={},
    )


@pytest.mark.parametrize(
    "data",
    [
        BAD_DATA,
        BAD_DATA_2,
        BAD_DATA_3,
    ],
)
def test_bad_data_ignored(data: bytes) -> None:
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(data)
    assert update == SensorUpdate(
        title="Lanyard/mini hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Lanyard/mini hygrometer " "EEFF",
                model=16,
                manufacturer="ThermoBeacon",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_device_0x18():
    parser = ThermoBeaconBluetoothDeviceData()
    parser.supported(MFR_24) is True
    assert parser.title == "Smart hygrometer EEFF"
