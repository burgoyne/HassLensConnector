import logging
import aiohttp
import voluptuous as vol

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    hasslens_url = entry.data["hasslens_url"]
    api_key = entry.data["api_key"]

    async def post_yaml(yaml_type: str, file_name: str):
        session = async_get_clientsession(hass)
        try:
            yaml_path = hass.config.path(file_name)
            with open(yaml_path, "r") as file:
                yaml_data = file.read()

            payload = {
                "type": yaml_type,
                "api_key": api_key,
                "data": yaml_data
            }

            async with session.post(hasslens_url, json=payload) as resp:
                if resp.status != 200:
                    _LOGGER.error("HassLens POST failed: %s", await resp.text())
                else:
                    _LOGGER.info("HassLens %s sync successful.", yaml_type)

        except FileNotFoundError:
            _LOGGER.warning("YAML file not found: %s", file_name)
        except Exception as e:
            _LOGGER.exception("Failed to send %s config to HassLens: %s", yaml_type, e)

    async def send_automation(call: ServiceCall):
        await post_yaml("automation", "automations.yaml")

    async def send_script(call: ServiceCall):
        await post_yaml("script", "scripts.yaml")

    async def send_device(call: ServiceCall):
        await post_yaml("device", "devices.yaml")

    hass.services.async_register(DOMAIN, "send_automation", send_automation)
    hass.services.async_register(DOMAIN, "send_script", send_script)
    hass.services.async_register(DOMAIN, "send_device", send_device)

    return True
