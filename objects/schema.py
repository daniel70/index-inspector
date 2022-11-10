from dataclasses import dataclass


@dataclass()
class Schema:
    name: str
    schema_id: int
    principal_id: int | None

    def __post_init__(self):
        self.tables = set()

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.schema_id)
