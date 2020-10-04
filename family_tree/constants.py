EXPECTED_KEYS = set(
    ["birth_place", "dob", "dod", "identifier", "name", "parents", "spouses"]
)


RELATION_MATRIX = [
    [
        "Siblings",
        "Nephew/Niece",
        "Grand-Nephew/Niece",
        "Great Grand-Nephew/Niece",
        "Great Great Grand-Nephew/Niece",
    ],
    [
        "Aunt/Uncle",
        "First cousin",
        "First cousin once removed",
        "First cousin twice removed",
        "First cousin thrice removed",
    ],
    [
        "Grand-Aunt/Uncle",
        "First cousin once removed",
        "Second cousin",
        "Second cousin once removed",
        "Second cousin twice removed",
    ],
    [
        "Great Grand-Aunt/Uncle",
        "First cousin twice removed",
        "Second cousin once removed",
        "Third cousin",
        "Third cousin once removed",
    ],
    [
        "Great Great Grand-Aunt/Uncle",
        "First cousin thrice removed",
        "Second cousin twice removed",
        "Third cousin once removed",
        "Fourth cousin",
    ],
]
