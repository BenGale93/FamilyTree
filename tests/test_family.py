from datetime import datetime

import pytest

import family_tree

LOCATION = "tests/data/"


@pytest.fixture
def my_test_fam() -> family_tree.Family:
    return family_tree.Family.from_json(f"{LOCATION}test_family.json")


def test_family_from_json(my_test_fam):
    assert len(my_test_fam) == 2


def test_no_duplicates(my_test_fam):
    my_test_fam.add_person(my_test_fam["JJ1996"])
    assert len(my_test_fam) == 2


def test_person_addition(my_test_fam):
    test_person = family_tree.Person("JD21990", "James Doe", datetime(1990, 1, 1))
    my_test_fam.add_person(test_person)
    assert len(my_test_fam) == 3


def test_members_are_persons(my_test_fam):
    assert all(
        [isinstance(v, family_tree.Person) for _, v in my_test_fam.members.items()]
    )


def test_couple_added(my_test_fam):
    assert len(my_test_fam.couples) == 1


def test_couple_membership(my_test_fam):
    couple = my_test_fam.couples["JD1993 JJ1996"]
    new_couple = family_tree.Couple(couple.left, couple.right)
    assert couple == new_couple


def test_iterate_over_family(my_test_fam):
    for _, person in my_test_fam.members.items():
        assert isinstance(person, family_tree.Person)


def test_json_validate_fail_keys():
    with pytest.raises(KeyError):
        family_tree.Family.from_json(f"{LOCATION}invalid_fields.json")


def test_json_validate_fail_identifier():
    with pytest.raises(KeyError):
        family_tree.Family.from_json(f"{LOCATION}invalid_id.json")
