from family_tree.person import Person


class Couple:
    def __init__(self, left: Person, right: Person) -> None:
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        return ((self.left == o.left) & (self.right == o.right)) | (
            (self.left == o.right) & (self.right == o.left)
        )

    def __str__(self) -> str:
        return f"{self.left} & {self.right}"
