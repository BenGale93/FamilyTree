import itertools
import math

from family_tree import Person, Couple


def person_box(person: Person) -> str:
    _, width = person.shape()

    top_bottom = "-" * (width + 4) + "\n"
    blank_line = surround_bars(" " * width, width)
    lines = [top_bottom, blank_line]

    for key, value in person.info().items():
        if key == "parents" or key == "spouses":
            if value:
                lines.append(surround_bars(f"{key}: ", width))
                for relative in value.split("\n"):
                    lines.append(surround_bars(relative, width))
        else:
            lines.append(surround_bars(f"{key}: {value}", width))

    lines.extend([blank_line, top_bottom])

    return "".join(lines)


def surround_bars(string: str, width: int) -> str:
    space_needed = width - len(string)

    left_whitespace = " " * math.floor((space_needed / 2))
    right_whitespace = " " * math.ceil((space_needed / 2))

    return "| " + left_whitespace + string + right_whitespace + " |\n"


def couple_box(couple: Couple) -> str:
    boxes = [person_box(couple.left), person_box(couple.right)]
    split_boxes = [box.split("\n") for box in boxes]
    split_boxes.sort(key=len, reverse=True)

    output = []
    for left, right in itertools.zip_longest(*split_boxes):
        if not right:
            right = ""
        output.extend([left, "  ", right, "\n"])

    return "".join(output)
