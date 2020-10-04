from datetime import datetime

import pytest  # type: ignore

import family_tree
from family_tree import constants
from . import LOCATION


@pytest.fixture
def my_test_fam() -> family_tree.Family:
    return family_tree.Family.from_json(f"{LOCATION}test_family.json")


def test_family_from_json(my_test_fam: family_tree.Family):
    assert len(my_test_fam) == 2


def test_no_duplicates(my_test_fam: family_tree.Family):
    my_test_fam.add_person(my_test_fam["JJ1996"])
    assert len(my_test_fam) == 2


def test_person_addition(my_test_fam: family_tree.Family):
    test_person = family_tree.Person("JD21990", "James Doe", datetime(1990, 1, 1))
    my_test_fam.add_person(test_person)
    assert len(my_test_fam) == 3


def test_members_are_persons(my_test_fam: family_tree.Family):
    assert all(
        [isinstance(v, family_tree.Person) for _, v in my_test_fam.members.items()]
    )


def test_couple_added(my_test_fam: family_tree.Family):
    assert len(my_test_fam.couples) == 1


def test_couple_membership(my_test_fam: family_tree.Family):
    couple = my_test_fam.couples["JD1993 JJ1996"]
    new_couple = family_tree.Couple(couple.left, couple.right)
    assert couple == new_couple


def test_iterate_over_family(my_test_fam: family_tree.Family):
    for _, person in my_test_fam.members.items():
        assert isinstance(person, family_tree.Person)


def test_json_validate_fail_keys():
    with pytest.raises(KeyError):  # type: ignore
        family_tree.Family.from_json(f"{LOCATION}invalid_fields.json")


def test_json_validate_fail_identifier():
    with pytest.raises(KeyError):  # type: ignore
        family_tree.Family.from_json(f"{LOCATION}invalid_id.json")


@pytest.fixture
def relation_test_fam() -> family_tree.Family:
    return family_tree.Family.from_json("tests\\data\\relationship_test.json")


def test_list_ancestors_layout(relation_test_fam: family_tree.Family):
    assert relation_test_fam.list_ancestors(relation_test_fam["G1A"]) == [
        {"G2B", "G2A"},
        {"G3B", "G3A", "G3C", "G3D"},
        {"G4A"},
    ]


def test_parental(relation_test_fam: family_tree.Family):
    assert relation_test_fam.relationship("G1A", "G2A") == "Parent"


def test_child(relation_test_fam: family_tree.Family):
    assert relation_test_fam.relationship("G2B", "G1A") == "Child"


def test_grandparent(relation_test_fam: family_tree.Family):
    assert relation_test_fam.relationship("G1A", "G3A") == "Grand-Parent"


def test_great_grandparent(relation_test_fam: family_tree.Family):
    assert relation_test_fam.relationship("G1A", "G4A") == "Great Grand-Parent"


def test_siblings(relation_test_fam: family_tree.Family):
    assert (
        relation_test_fam.relationship("G1A", "G1B") == constants.RELATION_MATRIX[0][0]
    )


def test_aunt_uncle(relation_test_fam: family_tree.Family):
    assert (
        relation_test_fam.relationship("G1A", "G2C") == constants.RELATION_MATRIX[1][0]
    )
