from __future__ import annotations

import json
from typing import Dict, List

from family_tree import Person, Couple


class Family:
    members: Dict[str, Person] = {}
    _couples: Dict[str, Couple] = {}

    def __len__(self) -> int:
        return len(self.members)

    def __getitem__(self, key) -> Person:
        return self.members[key]

    def __setitem__(self, key: str, item: Person) -> None:
        self.members[key] = item

    @property
    def couples(self) -> Dict[str, Couple]:
        return self._couples

    def add_person(self, new_person: Person) -> None:
        """Adds a new person to the family. Also checks if they are in a couple.

        Args:
            new_person (Person): Person to be added to the family.
        """
        if new_person.name not in self.members.keys():
            self._update_couples(new_person)
            self.members[new_person.identifier] = new_person

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

    def to_graph_dict(self) -> Dict[Person, List]:
        return {
            person: self._add_to_graph_dict(person) for person in self.members.values()
        }

    def _add_to_graph_dict(self, focus: Person) -> List:
        links = []
        for couple in self.couples.values():
            spouse = couple.return_other(focus)
            if spouse:
                links.append((spouse, "spouse"))

        for person in self.members.values():
            if person.name in focus.parents:
                links.append((person, "parent"))

        return links
