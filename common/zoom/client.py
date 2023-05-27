from pyzoom import ZoomClient

from config import zoom_config

zoom_client: ZoomClient = ZoomClient(**zoom_config)
