from graphviz import Graph  # type: ignore

from family_tree import Family, cmd_viewer


def render_family(family: Family) -> None:
    dot = Graph(
        name="My Family",
        graph_attr={"splines": "ortho"},
        strict=True,
    )  # type: ignore

    for identifier, person in family.items():
        dot.node(
            identifier,
            label="<" + cmd_viewer.person_box(person) + ">",
            shape="rectangle",
            color="black",
        )  # type: ignore
        if person.parents:
            if len(person.parents) == 1:
                comb_id = f"{person.parents[0]}&"
            else:
                comb_id = "".join(person.parents)
            dot.node(comb_id, shape="point")  # type: ignore
            dot.edge(comb_id, identifier)  # type: ignore

            for parent in person.parents:
                dot.edge(parent, comb_id)  # type: ignore

    for couple in family.couples.values():
        dot.edge(
            couple.left.identifier,
            couple.right.identifier,
            constraint="false",
            color="red",
        )  # type: ignore

    dot.render(view=True)  # type: ignore
