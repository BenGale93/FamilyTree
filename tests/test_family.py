from datetime import datetime

import pytest

import family_tree

LOCATION = "tests/data/test_family.json"


def test_family_from_json():
    my_test_fam = family_tree.Family.from_json(LOCATION)
    assert len(my_test_fam) == 2


@pytest.fixture
def my_test_fam() -> family_tree.Family:
    return family_tree.Family.from_json(LOCATION)


def test_no_duplicates(my_test_fam):
    my_test_fam.add_person(my_test_fam.members[0])
    assert len(my_test_fam) == 2


def test_person_addition(my_test_fam):
    test_person = family_tree.Person("John Doe", datetime(1990, 1, 1))
    my_test_fam.add_person(test_person)
    assert len(my_test_fam) == 3


def test_members_are_persons(my_test_fam):
    assert all([isinstance(p, family_tree.Person) for p in my_test_fam.members])


def test_index_access(my_test_fam):
    assert isinstance(my_test_fam[0], family_tree.Person)


def test_couple_added(my_test_fam):
    assert len(my_test_fam.couples) == 1


def test_couple_membership(my_test_fam):
    new_couple = family_tree.Couple(my_test_fam[0], my_test_fam[1])
    assert my_test_fam.couples[0] == new_couple


def test_iterate_over_family(my_test_fam):
    for person in my_test_fam:
        assert isinstance(person, family_tree.Person)
