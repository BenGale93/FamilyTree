from datetime import datetime

import pytest  # type: ignore

import family_tree


@pytest.fixture
def john_doe() -> family_tree.Person:
    return family_tree.Person(
        "JD1990", "John Doe", datetime(1990, 1, 1), datetime(2020, 1, 1)
    )


@pytest.fixture
def jane_doe() -> family_tree.Person:
    return family_tree.Person("JD1992", "Jane Doe", datetime(1992, 2, 19), None)


def test_equality(john_doe: family_tree.Person, jane_doe: family_tree.Person):
    couple = family_tree.Couple(john_doe, jane_doe)
    new_couple = family_tree.Couple(jane_doe, john_doe)
    assert couple == new_couple


def test_inequality(john_doe: family_tree.Person, jane_doe: family_tree.Person):
    couple = family_tree.Couple(john_doe, jane_doe)
    john_doe_new = family_tree.Person("JD1995", "John Doe", datetime(1995, 6, 20))
    new_couple = family_tree.Couple(jane_doe, john_doe_new)
    assert couple != new_couple


@pytest.fixture
def example_couple(
    john_doe: family_tree.Person, jane_doe: family_tree.Person
) -> family_tree.Couple:
    return family_tree.Couple(john_doe, jane_doe)


@pytest.fixture
def emily_doe() -> family_tree.Person:
    return family_tree.Person("ED1990", "Emily Doe", datetime(1992, 2, 28), None)


@pytest.fixture
def second_couple(
    john_doe: family_tree.Person, emily_doe: family_tree.Person
) -> family_tree.Couple:
    return family_tree.Couple(john_doe, emily_doe)


def test_couple_string(example_couple: family_tree.Couple):
    assert isinstance(str(example_couple), str)


def test_contains_true(
    example_couple: family_tree.Couple, john_doe: family_tree.Person
):
    assert john_doe in example_couple


def test_contains_false(
    example_couple: family_tree.Couple, emily_doe: family_tree.Person
):
    assert emily_doe not in example_couple


def test_hash_same_couple_same(example_couple: family_tree.Couple):
    couple_set = {example_couple}
    couple_set.add(example_couple)
    assert len(couple_set) == 1


def test_hash_same_couple_swap(
    example_couple: family_tree.Couple,
    john_doe: family_tree.Person,
    jane_doe: family_tree.Person,
):
    couple_set = {example_couple}
    new_couple = family_tree.Couple(jane_doe, john_doe)
    couple_set.add(new_couple)
    assert len(couple_set) == 1


def test_hash_diff(
    example_couple: family_tree.Couple, second_couple: family_tree.Couple
):
    couple_set = {example_couple}
    couple_set.add(second_couple)
    assert len(couple_set) == 2


def test_set_membership_false(
    example_couple: family_tree.Couple, second_couple: family_tree.Couple
):
    couple_set = {example_couple}
    assert (second_couple in couple_set) is False


def test_set_membership_true(
    example_couple: family_tree.Couple, second_couple: family_tree.Couple
):
    couple_set = {example_couple}
    couple_set.add(second_couple)
    assert (second_couple in couple_set) is True


def test_return_other(
    example_couple: family_tree.Couple,
    jane_doe: family_tree.Person,
    john_doe: family_tree.Person,
):
    assert example_couple.return_other(jane_doe) == john_doe


def test_failed_to_return(
    example_couple: family_tree.Couple, emily_doe: family_tree.Person
):
    assert example_couple.return_other(emily_doe) is None
