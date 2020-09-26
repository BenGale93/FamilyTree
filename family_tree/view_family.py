from graphviz import Graph  # type: ignore

from family_tree import Family, cmd_viewer


def render_family(family: Family) -> None:
    dot = Graph(
        name="My Family",
        node_attr={"shape": "rectangle", "color": "black"},
        graph_attr={"splines": "ortho"},
    )  # type: ignore

    for identifier, person in family.items():
        dot.node(
            identifier, label="<" + cmd_viewer.person_box(person) + ">"
        )  # type: ignore
        if person.parents:
            for new_person in family.values():
                if new_person.name in person.parents:
                    dot.edge(new_person.identifier, identifier)  # type: ignore

    for couple in family.couples.values():
        dot.edge(
            couple.left.identifier,
            couple.right.identifier,
            constraint="false",
            arrowhead="none",
        )  # type: ignore

    dot.render(view=True)  # type: ignore
