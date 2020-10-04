# FamilyTree
Uses Graphviz to create a family tree. Input is a json with the following fields:
* identifier: a unique identifier for that person. Recommendation is to use initials followed by year of birth.
* name: full birth name of the person.
* dob: date of birth if know. Otherwise null.
* dod: date of death if know. Otherwise null.
* parents: a list containing the corresponding unique identifiers of the persons parents. Maximum length of 2.
* spouses: a list containing the corresponding unique identifiers of the persons spouses.
* birth_place: place of birth if known. Otherwise null.

# Example Usage
```python
from family_tree import Family, FamilyGraph

my_family = Family.from_json("family.json")
family_graph = FamilyGraph(my_family, "dot")
family_graph.render_family()
```

# Things to note
Order is generally not important. However, if a person has had multiple spouses, putting that person between their spouses in the json is recommended.
