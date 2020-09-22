from family_tree import Person


class FamilyList:
    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __contains__(self, target: Person):
        pass


class _FamilyListNode:
    def __init__(self, data: Person) -> None:
        self.data = data
        self.parents = self.data.parents
        self.spouses = self.data.spouses
