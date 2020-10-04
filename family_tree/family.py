"""This module contains the Family class and helper functions."""
from __future__ import annotations

import json
from itertools import zip_longest
from typing import (
    Dict,
    ItemsView,
    Iterator,
    KeysView,
    List,
    Set,
    Tuple,
    Union,
    ValuesView,
)

from family_tree import Couple, Person, constants


class Family:
    """This class is used to store and process the family information.

    Attributes:
        members: Dict of all family members currently added.
        couples: Dict of all the couples in the family.

    Note:
        Iterating over the instance actually iterates over the members dict.
    """

    members: Dict[str, Person] = {}
    _couples: Dict[str, Couple] = {}

    def __len__(self) -> int:
        return len(self.members)

    def __getitem__(self, key: str) -> Person:
        return self.members[key]

    def __setitem__(self, key: str, item: Person) -> None:
        self.members[key] = item

    def __iter__(self) -> Iterator[str]:
        return iter(self.members)

    def keys(self) -> KeysView[str]:
        return self.members.keys()

    def items(self) -> ItemsView[str, Person]:
        return self.members.items()

    def values(self) -> ValuesView[Person]:
        return self.members.values()

    @property
    def couples(self) -> Dict[str, Couple]:
        return self._couples

    def add_person(self, new_person: Person) -> None:
        """Adds a new person to the family. Also checks if they are in a couple.

        Args:
            new_person (Person): Person to be added to the family.
        """
        if new_person.identifier not in self.members.keys():
            self._update_couples(new_person)
            self.members[new_person.identifier] = new_person

    def _update_couples(self, new_person: Person) -> None:
        """Helper function for updating the couples dict."""
        for person in self.members.values():
            if new_person.identifier in person.spouses:
                new_couple = Couple(person, new_person)
                self._couples[str(new_couple)] = new_couple

    def to_graph_dict(self) -> Dict[Person, List[Tuple[Person, str]]]:
        """Returns a dictionary of direct family connections."""
        return {
            person: self._add_to_graph_dict(person) for person in self.members.values()
        }

    def _add_to_graph_dict(self, focus: Person) -> List[Tuple[Person, str]]:
        """Helper function for to_graph_dict."""
        links = []
        for couple in self.couples.values():
            spouse = couple.return_other(focus)
            if spouse:
                links.append((spouse, "spouse"))

        for person in self.members.values():
            if person.name in focus.parents:
                links.append((person, "parent"))

        return links

    @classmethod
    def from_json(cls, filepath: str) -> Family:
        """Creates a Family from a json file.

        Args:
            filepath (str): Location of the json.

        Returns:
            Family: An instance of Family.
        """
        family = cls()
        with open(filepath, encoding="utf-8") as f:
            family_json = json.load(f)

        _validate_json(family_json)

        for person_json in family_json:
            person = Person(**person_json)
            family.add_person(person)

        return family

    def relationship(self, first_id: str, second_id: str) -> str:
        """Computes whether the two given identifiers are related by blood.
        If they are related by blood, returns the specific relationship, up to
        a point.

        Args:
            first_id
            second_id

        Returns:
            How second_id is related to first_id.
        """
        first_person = self.members[first_id]
        second_person = self.members[second_id]

        first_ancestors = self.list_ancestors(first_person)
        second_ancestors = self.list_ancestors(second_person)

        if result := self._parental_check(first_ancestors, second_id, "Parent"):
            return result

        if result := self._parental_check(second_ancestors, first_id, "Child"):
            return result

        for index_f, gen_f in enumerate(first_ancestors):
            for index_s, gen_s in enumerate(second_ancestors):
                common = gen_f.intersection(gen_s)
                if common:
                    return constants.RELATION_MATRIX[index_f][index_s]

        return "Not related by blood"

    def list_ancestors(self, person: Person) -> List[Set[Union[str]]]:
        """List the ancestors of the given person.

        Args:
            person: Person to list the ancestors for.

        Returns:
            List of sets where each set is a generation. First set are the parents etc.
        """
        return [set(gen) for gen in self._ancestors(person)]

    def _ancestors(self, person: Person) -> List[List[Union[str]]]:
        """Recursive function for listing ancestors."""
        ancestors = []
        if not person.parents:
            # Base case
            return []
        else:
            # Add parents to the start of the ancestor list
            ancestors.append(person.parents)
            for count, parent in enumerate(person.parents):
                # If more ancestors exist, continue
                if result := self._ancestors(self.members[parent]):
                    # If we are on the second parent, continue
                    if count == 1:
                        final_result = []  # Empty list for parents ancestors
                        # Blends the two ancestor lists together
                        for side1, side2 in zip_longest(
                            ancestors[1:], result, fillvalue=[]
                        ):
                            final_result.append(side1 + side2)
                        # Take only the parents
                        ancestors = [ancestors[0]]
                        # Extend parents by new ancestor list
                        ancestors.extend(final_result)
                    else:
                        # If on first parent, just extend by their ancestors
                        ancestors.extend(result)

        return ancestors

    def _parental_check(
        self, ancestors: List[Set[Union[str]]], identifier: str, relation: str
    ) -> Union[str, None]:
        """Checks if the identified person is in the list of ancestors.

        Args:
            ancestors: List of sets where each set is a generation of ancestors.
            identifier: Unique identifier of person being checked.
            relation: Either "Child" or "Parent".

        Returns:
            relationship string or None.
        """
        for gen_i, people in enumerate(ancestors):
            if identifier in people:
                if gen_i == 0:
                    return relation
                elif gen_i == 1:
                    return "Grand-" + relation
                else:
                    return "Great " * (gen_i - 1) + "Grand-" + relation

        else:
            return None


def _validate_json(json: List[Dict[str, str]]) -> None:
    """Helper function for from_json."""
    identifiers = set()
    for item in json:
        if item.keys() != constants.EXPECTED_KEYS:
            raise KeyError("JSON Keys do not match expected keys.")
        identifiers.add(item["identifier"])

    if len(identifiers) != len(json):
        raise KeyError("Not all identifier values in the JSON are unique.")
