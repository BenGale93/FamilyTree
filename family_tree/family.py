from __future__ import annotations

import json
from typing import List

from family_tree import Person, Couple


class Family:
    members = []
    _couples = []

    def __len__(self) -> int:
        return len(self.members)

    def __getitem__(self, key) -> Person:
        return self.members[key]

    @property
    def couples(self) -> List[Couple]:
        return self._couples

    def add_person(self, new_person: Person) -> None:
        if new_person not in self.members:
            self._update_couples(new_person)
            self.members.append(new_person)

    def _update_couples(self, new_person) -> None:
        for person in self.members:
            if new_person.name in person.spouses:
                new_couple = Couple(person, new_person)
                self._couples.append(new_couple)

    @classmethod
    def from_json(cls, filepath: str) -> Family:
        family = cls()
        with open(filepath) as f:
            family_json = json.load(f)

        for person_json in family_json:
            person = Person(**person_json)
            family.add_person(person)

        return family
