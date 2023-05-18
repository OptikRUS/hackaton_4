import os
from typing import Any

from config.settings import (
    SiteSettings,
    ApplicationSettings,
    DataBaseCredentials,
    DataBaseSettings,
    TortoiseSettings
)

base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app_config: dict[str, Any] = ApplicationSettings().dict()
site_config: dict[str, Any] = SiteSettings().dict()
database_config: dict[str, Any] = DataBaseSettings().dict()
tortoise_config: dict[str, Any] = TortoiseSettings().dict()
