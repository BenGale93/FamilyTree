from __future__ import annotations

from datetime import datetime
from typing import Optional, Union, List

import pandas as pd


class Person:
    def __init__(
        self,
        name: str,
        dob: Optional[Union[datetime, str]] = None,
        dod: Optional[Union[datetime, str]] = None,
        parents: Optional[List[str]] = None,
        spouses: Optional[List[str]] = None,
        birth_place: Optional[str] = None,
    ) -> None:
        self.name = name
        self.dob = dob
        self.dod = dod
        self.parents = parents
        self.spouses = spouses
        self.birth_place = birth_place

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__

    def __str__(self) -> str:
        return f"Name: {self.name}, DoB: {self.dob}."

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
