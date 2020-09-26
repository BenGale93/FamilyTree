from family_tree import Person


def person_box(person: Person) -> str:
    lines = []

    if len(names := person.name.split(" ")) > 2:
        if len(names) == 4:
            start_name = " ".join(names[:2])
            end_name = " ".join(names[2:])
        else:
            start_name = " ".join(names[:-1])
            end_name = names[-1]

        start = f"<b>{start_name}"
        end = f"{end_name}</b>"

        lines.extend([start, end])
    else:
        lines.append(f"<b>{person.name}</b>")

    if person.dob:
        lines.append(person.dob_string())

    if person.dod:
        lines.append(person.dod_string())

    if person.birth_place:
        lines.append(person.birth_place)

    return "<br/>".join(lines)
