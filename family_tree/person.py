from __future__ import annotations

from datetime import datetime
from typing import Optional


class Person:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        dob: Optional[datetime] = None,
        dod: Optional[datetime] = None,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.dod = dod

    def __eq__(self, o: object) -> bool:
        return self.__dict__ == o.__dict__

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"Person({self.__dict__})"

    @classmethod
    def from_dict(cls, in_dict: dict) -> Person:
        return cls(
            in_dict["first_name"], in_dict["last_name"], in_dict["dob"], in_dict["dod"]
        )
