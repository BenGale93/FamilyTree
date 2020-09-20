from __future__ import annotations

from datetime import datetime
from typing import Optional


class Person:
    def __init__(
        self, name: str, dob: Optional[datetime] = None, dod: Optional[datetime] = None
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

    @classmethod
    def from_dict(cls, in_dict: dict) -> Person:
        return cls(in_dict["name"], in_dict["dob"], in_dict["dod"])
