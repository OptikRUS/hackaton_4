from enum import Enum


class UserRole(str, Enum):
    CLIENT: str = "client"
    INSPECTOR: str = "inspector"
