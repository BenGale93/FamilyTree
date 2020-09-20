from datetime import datetime

import pytest

import family_tree


@pytest.fixture
def john_doe_data() -> dict:
    return {
        "first_name": "John",
        "last_name": "Doe",
        "dob": datetime(1990, 1, 1),
        "dod": datetime(2020, 1, 1),
    }


def test_person_create(john_doe_data):
    john_doe = family_tree.Person(**john_doe_data)
    assert john_doe.__dict__ == john_doe_data


@pytest.fixture
def john_doe(john_doe_data) -> family_tree.Person:
    return family_tree.Person(**john_doe_data)


def test_only_name():
    person_data = {
        "first_name": "John",
        "last_name": "Doe",
    }

    john_doe = family_tree.Person(**person_data)
    assert (john_doe.first_name == person_data["first_name"]) & (
        john_doe.last_name == person_data["last_name"]
    )


def test_equality(john_doe_data):
    john_first = family_tree.Person(**john_doe_data)
    john_second = family_tree.Person(**john_doe_data)
    assert john_first == john_second


def test_inequality(john_doe_data):
    john_first = family_tree.Person(**john_doe_data)
    john_second = family_tree.Person(
        john_doe_data["first_name"], john_doe_data["last_name"]
    )
    assert john_first != john_second


def test_person_string(john_doe):
    assert isinstance(str(john_doe), str)


def test_person_repr(john_doe):
    assert isinstance(repr(john_doe), str)