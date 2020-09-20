from datetime import datetime

import pytest

import family_tree


@pytest.fixture
def john_doe_data() -> dict:
    return {
        "name": "John Doe",
        "dob": datetime(1990, 1, 1),
        "dod": datetime(2020, 1, 1),
    }


def test_person_create(john_doe_data):
    john_doe = family_tree.Person(**john_doe_data)
    assert isinstance(john_doe, family_tree.Person)


@pytest.fixture
def john_doe(john_doe_data) -> family_tree.Person:
    return family_tree.Person(**john_doe_data)


def test_only_name():
    person_data = {"name": "John Doe"}

    john_doe = family_tree.Person(**person_data)
    assert john_doe.name == person_data["name"]


def test_equality(john_doe_data):
    john_first = family_tree.Person(**john_doe_data)
    john_second = family_tree.Person(**john_doe_data)
    assert john_first == john_second


def test_inequality(john_doe_data):
    john_first = family_tree.Person(**john_doe_data)
    john_second = family_tree.Person(john_doe_data["name"])
    assert john_first != john_second


def test_person_string(john_doe):
    assert isinstance(str(john_doe), str)


def test_person_repr(john_doe):
    assert isinstance(repr(john_doe), str)


def test_dob_is_date(john_doe):
    assert isinstance(john_doe.dob, datetime)
