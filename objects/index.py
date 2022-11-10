from dataclasses import dataclass


@dataclass()
class Index:
    object_id: int
    name: str | None
    index_id: int
    type: int
    type_desc: str | None
    is_unique: bool | None
    data_space_id: int | None
    ignore_dup_key: bool | None
    is_primary_key: bool | None
    is_unique_constraint: bool | None
    fill_factor: int
    is_padded: bool | None
    is_disabled: bool | None
    is_hypothetical: bool | None
    allow_row_locks: bool | None
    allow_page_locks: bool | None
    has_filter: bool | None
    filter_definition: str | None
    compression_delay: int | None

    columns: list["IndexColumn"] = None
    includes: set["IndexColumn"] = None

    def __post_init__(self):
        self.columns = list()
        self.includes = set()

    def __hash__(self):
        return hash((self.object_id, self.index_id))

    def __str__(self):
        return self.name


@dataclass()
class IndexColumn:
    object_id: int
    index_id: int
    index_column_id: int
    column_id: int
    key_ordinal: int
    partition_ordinal: int
    is_descending_key: bool | None
    is_included_column: bool | None

    name: str = None

    def __hash__(self):
        return hash((self.object_id, self.index_id, self.index_column_id))

    def __str__(self):
        return self.name
