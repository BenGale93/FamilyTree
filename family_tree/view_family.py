from graphviz import Graph  # type: ignore

from family_tree import Family, Person, Couple


class FamilyGraph:
    def __init__(self, family: Family, layout: str) -> None:
        self.family = family
        self.dot = Graph(  # type: ignore
            name="My Family",
            graph_attr={"layout": layout, "overlap": "scale"},
            strict=True,
        )

    def render_family(self) -> None:
        for person in self.family.values():
            self._person_node(person)

        for couple in self.family.couples.values():
            self._couple_connection(couple)

        for person in self.family.values():
            if person.parents:
                self._link_parents(person)

        self.dot.render(view=True)  # type: ignore

    def _person_node(self, person: Person) -> None:
        self.dot.node(  # type: ignore
            person.identifier,
            label="<" + person.to_html() + ">",
            shape="rectangle",
            color="black",
        )

    def _dummy_node(self, combined_id: str) -> None:
        self.dot.node(  # type: ignore
            combined_id,
            shape="point",
            style="invis",
            height="0",
            width="0",
            margin="0",
        )

    def _couple_connection(self, couple: Couple) -> None:
        self._dummy_node(str(couple))
        for person in [couple.left, couple.right]:
            self.dot.edge(person.identifier, str(couple), color="red")  # type: ignore

    def _relative_edge(self, tail: str, head: str) -> None:
        self.dot.edge(tail, head)  # type: ignore

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
