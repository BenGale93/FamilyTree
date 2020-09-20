from __future__ import annotations

from datetime import datetime
from typing import Optional, Union

import pandas as pd


class Person:
    def __init__(
        self,
        name: str,
        dob: Optional[Union[datetime, str]] = None,
        dod: Optional[Union[datetime, str]] = None,
    ) -> None:
        self.name = name
        self.dob = dob
        self.dod = dod

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__

    def __str__(self) -> str:
        return f"{self.name}: {self.dob}"

    def __repr__(self) -> str:
        return f"Person({self.__dict__})"

    @property
    def dob(self) -> pd.Timestamp:
        return self._dob

    @dob.setter
    def dob(self, value: object) -> None:
        self._dob = pd.to_datetime(value)

    @property
    def dod(self) -> pd.Timestamp:
        return self._dod

    @dod.setter
    def dod(self, value: object) -> None:
        self._dod = pd.to_datetime(value)

    @classmethod
    def from_dict(cls, in_dict: dict) -> Person:
        return cls(in_dict["name"], in_dict["dob"], in_dict["dod"])
