from family_tree import Person


def person_box(person: Person) -> str:
    lines = ["<b>Name</b>"]

    if len(names := person.name.split(" ")) == 4:
        lines.append(" ".join(names[:2]))
        lines.append(" ".join(names[2:]))
    elif len(names) == 3:
        lines.append(" ".join(names[:-1]))
        lines.append(names[-1])
    else:
        lines.append(person.name)

    if person.dob:
        lines.append("<b>DoB</b>")
        lines.append(str(person.dob.date()))

    if person.dod:
        lines.append("<b>DoD</b>")
        lines.append(str(person.dod.date()))

    if person.birth_place:
        lines.append("<b>Place of Birth</b>")
        lines.append(person.birth_place)

    return "<br/>".join(lines)
