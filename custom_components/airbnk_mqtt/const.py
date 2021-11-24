"""Constants for Daikin MQTT integration."""

from homeassistant.const import (
    CONF_DEVICE_CLASS,
    CONF_TOKEN,
    CONF_ICON,
    CONF_NAME,
    CONF_TYPE,
    CONF_UNIT_OF_MEASUREMENT,
    DEVICE_CLASS_VOLTAGE,
    PERCENTAGE,
)

DOMAIN = "airbnk_mqtt"

CONF_USERID = "userId"
CONF_TOKENSET = CONF_TOKEN + "set"
CONF_UUID = "uuid"
CONF_DEVICE_CONFIGS = "device_configs"
CONF_LOCKSTATUS = "lockStatus"
CONF_MQTT_TOPIC = "mqtt_topic"
CONF_MAC_ADDRESS = "mac_address"

AIRBNK_DATA = "airbnk_data"
AIRBNK_API = "airbnk_api"
AIRBNK_DEVICES = "airbnk_devices"
AIRBNK_DISCOVERY_NEW = "airbnk_discovery_new_{}"

TIMEOUT = 60

LOCK_STATE_LOCKED = 0
LOCK_STATE_UNLOCKED = 1
LOCK_STATE_JAMMED = 2
LOCK_STATE_OPERATING = 3
LOCK_STATE_FAILED = 4

LOCK_STATE_STRINGS = { 
    LOCK_STATE_LOCKED: "Locked",
    LOCK_STATE_UNLOCKED: "Unlocked",
    LOCK_STATE_JAMMED: "Jammed",
    LOCK_STATE_OPERATING: "Operating",
    LOCK_STATE_FAILED: "Failed",
 }

SENSOR_TYPE_STATE = "state"
SENSOR_TYPE_BATTERY = "battery"
SENSOR_TYPE_EVENTS = "lock_events"
SENSOR_TYPE_LAST_ADVERT = "last_advert"

SENSOR_TYPES = {
    SENSOR_TYPE_STATE: {
        CONF_NAME: "status",
        CONF_TYPE: SENSOR_TYPE_STATE,
    },
    SENSOR_TYPE_BATTERY: {
        CONF_NAME: "battery",
        CONF_TYPE: SENSOR_TYPE_BATTERY,
        CONF_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
        CONF_UNIT_OF_MEASUREMENT: PERCENTAGE,
    },
    SENSOR_TYPE_EVENTS: {
        CONF_NAME: "events",
        CONF_TYPE: SENSOR_TYPE_EVENTS,
    },
    # SENSOR_TYPE_LAST_ADVERT: {
    #     CONF_NAME: "last advert",
    #     CONF_TYPE: SENSOR_TYPE_LAST_ADVERT,
    # },
}