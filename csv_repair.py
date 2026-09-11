"""Small demonstration used as proof for the automation-rescue offer."""


def legacy_parse_rows(text: str) -> list[int]:
    """Original behavior: a blank row raises ValueError."""
    return [int(row) for row in text.splitlines()]


def parse_rows(text: str) -> list[int]:
    """Ignore blank rows while keeping non-empty invalid input visible."""
    values: list[int] = []
    for row in text.splitlines():
        value = row.strip()
        if not value:
            continue
        values.append(int(value))
    return values
