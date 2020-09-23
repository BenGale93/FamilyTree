from __future__ import annotations

from datetime import datetime
from typing import Optional, Union, List, Tuple

import pandas as pd  # type: ignore


class Person:
    def __init__(
        self,
        identifier: str,
        name: str,
        dob: Optional[Union[datetime, str]] = None,
        dod: Optional[Union[datetime, str]] = None,
        parents: Optional[List[str]] = None,
        spouses: Optional[List[str]] = None,
        birth_place: Optional[str] = None,
    ) -> None:
        """Creates a Person instance.

        Args:
            identifier (str): Unique identifier.
            name (str): Full name.
            dob (Optional[Union[datetime, str]]): Date of Birth. Defaults to None.
            dod (Optional[Union[datetime, str]]): Date of Death. Defaults to None.
            parents (Optional[List[str]]): List of parental names. Defaults to None.
            spouses (Optional[List[str]]): List of spousal names. Defaults to None.
            birth_place (Optional[str]). Defaults to None.
        """
        self.identifier = identifier
        self.name = name
        self.dob = dob
        self.dod = dod
        self.parents: List[str] = parents if parents else []
        self.spouses: List[str] = spouses if spouses else []
        self.birth_place = birth_place

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return False
        return self.identifier == o.identifier

    def __str__(self) -> str:
        return f"Name: {self.name}, DoB: {self.dob}."

    def __repr__(self) -> str:
        return f"{self.identifier}"

    def __hash__(self) -> int:
        return hash(self.identifier)

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

    def shape(self) -> Tuple:
        widths = []
        height = 0
        for key, attribute in self.__dict__.items():
            if isinstance(attribute, str):
                widths.append(len(str(key) + str(attribute)))
                height += 1
            elif isinstance(attribute, pd.Timestamp):
                widths.append(len(str(key).lstrip("_") + str(attribute.date())))
                height += 1
            elif isinstance(attribute, list):
                if attribute:
                    widths.append(max(len(name) for name in attribute))
                    # + 1 for string of "parents" or "spouses"
                    height += len(attribute) + 1

        width = max(widths)
        return (height, width)
