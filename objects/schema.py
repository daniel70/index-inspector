from dataclasses import dataclass


@dataclass()
class Schema:
    name: str
    schema_id: int
    principal_id: int
