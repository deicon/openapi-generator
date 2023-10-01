# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SingleRefType(str, Enum):
    """
    SingleRefType
    """

    """
    allowed enum values
    """
    ADMIN = 'admin'
    USER = 'user'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SingleRefType from a JSON string"""
        return cls(json.loads(json_str))


