# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MapTest(BaseModel):
    """
    MapTest
    """
    map_map_of_string: Optional[Dict[str, Dict[str, StrictStr]]] = None
    map_of_enum_string: Optional[Dict[str, StrictStr]] = None
    direct_map: Optional[Dict[str, StrictBool]] = None
    indirect_map: Optional[Dict[str, StrictBool]] = None
    __properties: ClassVar[List[str]] = ["map_map_of_string", "map_of_enum_string", "direct_map", "indirect_map"]

    @field_validator('map_of_enum_string')
    def map_of_enum_string_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('UPPER', 'lower'):
            raise ValueError("must be one of enum values ('UPPER', 'lower')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MapTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of MapTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "map_map_of_string": obj.get("map_map_of_string"),
            "map_of_enum_string": obj.get("map_of_enum_string"),
            "direct_map": obj.get("direct_map"),
            "indirect_map": obj.get("indirect_map")
        })
        return _obj


