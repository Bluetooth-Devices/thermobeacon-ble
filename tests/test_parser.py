from bluetooth_sensor_state_data import BluetoothServiceInfo, SensorUpdate
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


def test_can_create():
    ThermoBeaconBluetoothDeviceData()


MFR_20 = BluetoothServiceInfo(
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

MFR_22 = BluetoothServiceInfo(
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


BAD_DATA = BluetoothServiceInfo(
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


def test_with_22_byte_update():
    parser = ThermoBeaconBluetoothDeviceData()
    parser.supported(MFR_22) is True
    assert parser.title == "Smart hygrometer EEFF"


def test_supported_set_the_title():
    parser = ThermoBeaconBluetoothDeviceData()
    parser.supported(MFR_20) is True
    assert parser.title == "Lanyard/mini hygrometer EEFF"


def test_20_byte_update():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(MFR_20)
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


def test_bad_data_ignored():
    parser = ThermoBeaconBluetoothDeviceData()
    update = parser.update(BAD_DATA)
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
