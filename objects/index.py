from dataclasses import dataclass, field
from datetime import datetime
from . import quote

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
    is_ignored_in_optimization: bool | None = None  # SQL 2019
    suppress_dup_key_messages: bool | None = None  # SQL 2019
    auto_created: bool | None = None # SQL 2019
    optimize_for_sequential_key: bool | None = None  # SQL 2019

    table: "Table" = None
    columns: list["IndexColumn"] = None
    includes: set["IndexColumn"] = None
    usage: "IndexUsage" = None

    def __post_init__(self):
        self.columns = list()
        self.includes = set()

    def __hash__(self):
        return hash((self.object_id, self.index_id))

    def __str__(self):
        return quote(self.name)

    def create(self) -> str:
        columns = ", ".join(str(x) for x in self.columns)
        includes = ", ".join(str(x) for x in self.includes)
        sql = f"CREATE INDEX {self.name} ({columns})"
        if self.includes:
            sql += f" INCLUDE ({includes})"
        return sql

    def drop(self) -> str:
        return f"DROP INDEX {self.name} ON {self.table.schema}.{self.table}"


@dataclass()
class IndexColumn:
    object_id: int
    index_id: int = field(compare=False)
    index_column_id: int
    column_id: int
    key_ordinal: int
    partition_ordinal: int
    is_descending_key: bool | None
    is_included_column: bool | None
    column_store_order_ordinal: int = None # SQL 2019

    name: str = None

    def __hash__(self):
        return hash((self.object_id, self.index_column_id)) # for equality we removed self.index_id

    def __str__(self):
        return quote(self.name)


# select * from sys.dm_db_index_operational_stats(DB_ID(), NULL, NULL, NULL);
# select * from sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, NULL);
# select * from sys.dm_db_index_usage_stats;

@dataclass()
class IndexUsage:
    database_id: str
    object_id: int
    index_id: int
    user_seeks: int
    user_scans: int
    user_lookups: int
    user_updates: int
    last_user_seek: datetime | None
    last_user_scan: datetime | None
    last_user_lookup: datetime | None
    last_user_update: datetime | None
    system_seeks: int
    system_scans: int
    system_lookups: int
    system_updates: int
    last_system_seek: datetime | None
    last_system_scan: datetime | None
    last_system_lookup: datetime | None
    last_system_update: datetime | None
