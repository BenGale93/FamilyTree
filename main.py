"""Example usage of the Family and FamilyGraph classes."""
from family_tree import Family, FamilyGraph

my_family = Family.from_json("family.json")
family_graph = FamilyGraph(my_family, "dot")
family_graph.render_family()
