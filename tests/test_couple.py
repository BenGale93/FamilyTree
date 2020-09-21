from datetime import datetime

import pytest

import family_tree


@pytest.fixture
def john_doe() -> family_tree.Person:
    john_doe_data = {
        "name": "John Doe",
        "dob": datetime(1990, 1, 1),
        "dod": datetime(2020, 1, 1),
    }
    return family_tree.Person(**john_doe_data)


@pytest.fixture
def jane_doe() -> family_tree.Person:
    jane_doe_data = {"name": "Jane Doe", "dob": datetime(1992, 2, 19), "dod": None}
    return family_tree.Person(**jane_doe_data)


def test_equality(john_doe, jane_doe):
    couple = family_tree.Couple(john_doe, jane_doe)
    new_couple = family_tree.Couple(jane_doe, john_doe)
    assert couple == new_couple


def test_inequality(john_doe, jane_doe):
    couple = family_tree.Couple(john_doe, jane_doe)
    john_doe_new = family_tree.Person("John Doe", datetime(1995, 6, 20))
    new_couple = family_tree.Couple(jane_doe, john_doe_new)
    assert couple != new_couple


@pytest.fixture
def example_couple(john_doe, jane_doe) -> family_tree.Couple:
    return family_tree.Couple(john_doe, jane_doe)


@pytest.fixture
def second_couple(john_doe) -> family_tree.Couple:
    emily_doe_data = {"name": "Emily Doe", "dob": datetime(1990, 2, 28), "dod": None}
    emily_doe = family_tree.Person(**emily_doe_data)
    return family_tree.Couple(john_doe, emily_doe)


def test_couple_string(example_couple):
    assert isinstance(str(example_couple), str)
