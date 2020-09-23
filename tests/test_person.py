from datetime import datetime

import pytest

import family_tree
from . import LOCATION


@pytest.fixture
def my_test_fam() -> family_tree.Family:
    return family_tree.Family.from_json(f"{LOCATION}test_family.json")


@pytest.fixture
def john_doe_data() -> dict:
    return {
        "identifier": "JD1990",
        "name": "John Doe",
        "dob": datetime(1990, 1, 1),
        "dod": datetime(2020, 1, 1),
    }


@pytest.fixture
def jane_doe_data() -> dict:
    return {
        "identifier": "JD21990",
        "name": "Jane Doe",
        "dob": datetime(1990, 1, 1),
        "dod": datetime(2020, 1, 1),
    }


def test_person_create(john_doe_data):
    john_doe = family_tree.Person(**john_doe_data)
    assert isinstance(john_doe, family_tree.Person)


@pytest.fixture
def jane_doe(jane_doe_data) -> family_tree.Person:
    return family_tree.Person(**jane_doe_data)


@pytest.fixture
def john_doe(john_doe_data) -> family_tree.Person:
    return family_tree.Person(**john_doe_data)


def test_only_name():
    person_data = {"identifier": "JD", "name": "John Doe"}

    john_doe = family_tree.Person(**person_data)
    assert john_doe.name == person_data["name"]


def test_equality(john_doe_data):
    john_first = family_tree.Person(**john_doe_data)
    john_second = family_tree.Person(**john_doe_data)
    assert john_first == john_second


def test_inequality(john_doe_data):
    john_first = family_tree.Person(**john_doe_data)
    john_second = family_tree.Person("JD2", john_doe_data["name"])
    assert john_first != john_second


def test_person_string(john_doe):
    assert isinstance(str(john_doe), str)


def test_person_repr(john_doe):
    assert isinstance(repr(john_doe), str)


def test_dob_is_date(john_doe):
    assert isinstance(john_doe.dob, datetime)


def test_hash_same(john_doe):
    person_set = {john_doe}
    person_set.add(john_doe)
    assert len(person_set) == 1


def test_hash_diff(john_doe, jane_doe):
    person_set = {john_doe}
    person_set.add(jane_doe)
    assert len(person_set) == 2


def test_hash_no_dob():
    james_doe = family_tree.Person("JD1", "James Doe")
    person_set = {james_doe}
    person_set.add(james_doe)
    assert len(person_set) == 1


def test_set_membership_false(john_doe, jane_doe):
    person_set = {john_doe}
    assert (jane_doe in person_set) is False


def test_set_membership_true(john_doe, jane_doe):
    person_set = {john_doe}
    person_set.add(jane_doe)
    assert (jane_doe in person_set) is True


def test_shape(my_test_fam):
    assert my_test_fam.members["JD1993"].shape() == (7, 11)
