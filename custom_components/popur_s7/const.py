"""Constants for the Popur integration."""

from datetime import timedelta
from typing import Final

DOMAIN: Final = "popur_s7"

CONF_INSTALL_ID: Final = "install_id"
CONF_HOST: Final = "host"

# Live device state refresh over the local channel; MQTT pushes cover
# real-time changes, this catches anything that is never pushed.
LOCAL_REFRESH_INTERVAL: Final = timedelta(seconds=60)

# Cloud-side data (settings-DP shadow, pets, usage records) refreshes on a
# slower cadence — the LAN channel covers live device state between these.
CLOUD_REFRESH_INTERVAL: Final = timedelta(minutes=10)

PET_RECORDS_PAGE_SIZE: Final = 25
