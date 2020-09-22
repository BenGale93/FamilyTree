import family_tree

my_family = family_tree.Family.from_json("family.json")

print(my_family.to_graph_dict())
