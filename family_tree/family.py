from __future__ import annotations

import json

from family_tree.person import Person


class Family:
    members = []

    def __len__(self) -> int:
        return len(self.members)

    def add_person(self, person: Person):
        if person not in self.members:
            self.members.append(person)

    @classmethod
    def from_json(cls, filepath: str) -> Family:
        family = cls()
        with open(filepath) as f:
            family_json = json.load(f)

        for person_json in family_json:
            person = Person.from_dict(person_json)
            family.add_person(person)

        return family
