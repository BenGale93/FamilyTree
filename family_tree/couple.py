"""This module contains the couple class for linking two spouses together."""
from typing import Union

from family_tree import Person


class Couple:
    """This class is for linking two people together as a couple. Used for current
    and former spouses.

    Attributes:
        left: The lefthand person in the couple.
        right: The righthand person in the couple.

    Note:
        The lefthand/righthand ordering is arbitrary and gender neutral.
    """

    def __init__(self, left: Person, right: Person) -> None:
        """Creates a couple instance.

        Args:
            left (Person): One of the people in the relationship.
            right (Person): The other person in the relationship.
        """
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Couple):
            return False
        return ((self.left == o.left) & (self.right == o.right)) | (
            (self.left == o.right) & (self.right == o.left)
        )

    def __repr__(self) -> str:
        output = [self.left.identifier, self.right.identifier]
        output.sort()
        return " ".join(output)

    def __contains__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return False
        return (other == self.left) | (other == self.right)

    def __hash__(self) -> int:
        return hash(self.left) + hash(self.right)

    def return_other(self, target: Person) -> Union[Person, None]:
        """Given a Person in the couple, returns the other Person.

        Args:
            target: A Person in the couple

        Returns:
            If the target is in the couple, returns the other person.
            Otherwise, returns None.
        """
        if target not in self:
            return None
        return self.left if target == self.right else self.right
