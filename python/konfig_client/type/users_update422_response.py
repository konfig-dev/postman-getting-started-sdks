# coding: utf-8

"""
    Requests

    This API manages a simple User database

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal


class RequiredUsersUpdate422Response(TypedDict):
    pass

class OptionalUsersUpdate422Response(TypedDict, total=False):
    message: str

class UsersUpdate422Response(RequiredUsersUpdate422Response, OptionalUsersUpdate422Response):
    pass
