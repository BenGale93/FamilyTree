"""This module contains the Person class used to represent a single person."""
from __future__ import annotations

from datetime import datetime
from typing import Optional, Union, List

import pandas as pd  # type: ignore


class Person:
    """Represents a single person."""

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
    def dob(self, value: object) -> None:  # type: ignore
        self._dob: pd.Timestamp = pd.to_datetime(value)  # type: ignore

    @property
    def dod(self) -> pd.Timestamp:
        return self._dod

    @dod.setter
    def dod(self, value: object) -> None:  # type: ignore
        self._dod: pd.Timestamp = pd.to_datetime(value)  # type: ignore

    def dob_string(self) -> str:
        """Returns the date of birth as a formatted string."""
        return f"b. {str(self.dob.date())}"

    def dod_string(self) -> str:
        """Returns the date of death as a formatted string."""
        return f"d. {str(self.dod.date())}"

    def to_html(self) -> str:
        """Renders the person's information in html format.

        Returns:
            html string.
        """
        lines = []

        if len(names := self.name.split(" ")) > 2:
            if len(names) >= 4:
                start_name = " ".join(names[:-2])
                end_name = " ".join(names[-2:])
            else:
                start_name = " ".join(names[:-1])
                end_name = names[-1]

            start = f"<b>{start_name}"
            end = f"{end_name}</b>"

            lines.extend([start, end])
        else:
            lines.append(f"<b>{self.name}</b>")

        if self.dob:
            lines.append(self.dob_string())

        if self.dod:
            lines.append(self.dod_string())

        if self.birth_place:
            lines.append(self.birth_place)

        return "<br/>".join(lines)
