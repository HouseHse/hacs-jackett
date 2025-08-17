from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from . import docker_manager
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: ConfigType):
    async def handle_start(call):
        docker_manager.start_jackett()
        docker_manager.add_default_indexers()

    async def handle_stop(call):
        docker_manager.stop_jackett()

    hass.services.async_register(DOMAIN, "start", handle_start)
    hass.services.async_register(DOMAIN, "stop", handle_stop)

    return True
