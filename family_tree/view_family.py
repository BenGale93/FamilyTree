from graphviz import Graph  # type: ignore

from family_tree import Family, Person, Couple


class FamilyGraph:
    dummy_node_attrs = {
        "shape": "point",
        "style": "invis",
        "height": "0",
        "width": "0",
        "margin": "0",
    }

    def __init__(self, family: Family, layout: str) -> None:
        self.family = family
        self.graph = Graph(  # type: ignore
            name="My Family",
            graph_attr={
                "layout": layout,
                "concentrate": "true",
                "overlap": "scale",
            },
            strict=True,
        )
        self._link_family()

    def _link_family(self) -> None:
        for couple in self.family.couples.values():
            self._couple_connection(couple)

        for person in self.family.values():
            add_node = True
            for entry in self.graph.body:  # type: ignore
                if f"\t{person.identifier} [" in entry:
                    add_node = False
                    break
            if add_node:
                self._person_node(person)
            if person.parents:
                self._link_parents(person)

    def render_family(self) -> None:
        self.graph.render(view=True)  # type: ignore

    def _person_node(self, person: Person) -> None:
        self.graph.node(  # type: ignore
            person.identifier,
            label="<" + person.to_html() + ">",
            shape="rectangle",
            color="black",
        )

    def _dummy_node(self, combined_id: str) -> None:
        self.graph.node(combined_id, **self.dummy_node_attrs)  # type: ignore

    def _couple_connection(self, couple: Couple) -> None:
        with self.graph.subgraph() as c:  # type: ignore
            c.attr(rank="same")  # type: ignore
            c.node(str(couple), **self.dummy_node_attrs)  # type: ignore
            for person in [couple.left, couple.right]:
                c.node(  # type: ignore
                    person.identifier,
                    label="<" + person.to_html() + ">",
                    shape="rectangle",
                    color="black",
                )
            c.edge(couple.left.identifier, str(couple), color="red")  # type: ignore
            c.edge(str(couple), couple.right.identifier, color="red")  # type: ignore

    def _relative_edge(self, tail: str, head: str) -> None:
        self.graph.edge(tail, head)  # type: ignore

    def _link_parents(self, person: Person) -> None:
        num_parents = len(person.parents)
        if num_parents == 1:
            # & is arbitrary, used to make dummy node ID different to person node
            comb_id = f"{person.parents[0]}&"
            self._relative_edge(person.parents[0], comb_id)
        else:
            comb_id = "".join(sorted(person.parents))
            self._relative_edge(" ".join(sorted(person.parents)), comb_id)

        self._dummy_node(comb_id)
        self._relative_edge(comb_id, person.identifier)
