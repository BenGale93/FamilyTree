from __future__ import annotations

import json
from typing import Dict

from family_tree import Person, Couple


class Family:
    members = {}
    _couples = {}

    def __len__(self) -> int:
        return len(self.members)

    def __getitem__(self, key) -> Person:
        return self.members[key]

    def __setitem__(self, key, item) -> Person:
        self.members[key] = item

    @property
    def couples(self) -> Dict[str:Couple]:
        return self._couples

    def add_person(self, new_person: Person) -> None:
        """Adds a new person to the family. Also checks if they are in a couple.

        Args:
            new_person (Person): Person to be added to the family.
        """
        if new_person.name not in self.members.keys():
            self._update_couples(new_person)
            self.members[new_person.name] = new_person

    def _update_couples(self, new_person) -> None:
        for person in self.members.values():
            if new_person.name in person.spouses:
                new_couple = Couple(person, new_person)
                self._couples[str(new_couple)] = new_couple

    @classmethod
    def from_json(cls, filepath: str) -> Family:
        """Creates a Family from a json file.

        Args:
            filepath (str): Location of the json.

        Returns:
            Family: An instance of Family.
        """
        family = cls()
        with open(filepath) as f:
            family_json = json.load(f)

        for person_json in family_json:
            person = Person(**person_json)
            family.add_person(person)

        return family
