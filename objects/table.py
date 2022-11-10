from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Table:
    name: str
    object_id: int
    principal_id: int | None
    schema_id: int
    parent_object_id: int
    type: str
    type_desc: str
    create_date: datetime
    modify_date: datetime
    is_ms_shipped: bool
    is_published: bool
    is_schema_published: bool
    lob_data_space_id: int
    filestream_data_space_id: int | None
    max_column_id_used: int
    lock_on_bulk_load: bool
    uses_ansi_nulls: bool
    is_replicated: bool
    has_replication_filter: bool
    is_merge_published: bool
