from family_tree import Person


class Couple:
    def __init__(self, left: Person, right: Person) -> None:
        """Creates a couple instance.

        Args:
            left (Person): One of the people in the relationship.
            right (Person): The other person in the relationship.
        """
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        return ((self.left == o.left) & (self.right == o.right)) | (
            (self.left == o.right) & (self.right == o.left)
        )

    def __hash__(self) -> int:
        return hash(self.left) + hash(self.right)

    def __str__(self) -> str:
        return f"{self.left} & {self.right}"

    def __repr__(self) -> str:
        return repr(self.left) + repr(self.right)
