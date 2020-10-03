EXPECTED_KEYS = set(
    ["birth_place", "dob", "dod", "identifier", "name", "parents", "spouses"]
)

RELATION_MATRIX = [
    ["Siblings", "Nephew/Niece", "Grand-Nephew/Niece"],
    ["Aunt/Uncle", "First cousin", "First cousin once removed"],
    ["Grand-Aunt/Uncle", "First cousin once removed", "Second cousin"],
]
