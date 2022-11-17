from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Table:
    name: str
    object_id: int
    principal_id: int | None
    schema_id: int
    parent_object_id: int
    type: str | None
    type_desc: str | None
    create_date: datetime
    modify_date: datetime
    is_ms_shipped: bool
    is_published: bool
    is_schema_published: bool
    lob_data_space_id: int
    filestream_data_space_id: int | None
    max_column_id_used: int
    lock_on_bulk_load: bool
    uses_ansi_nulls: bool | None
    is_replicated: bool | None
    has_replication_filter: bool | None
    is_merge_published: bool | None
    is_sync_tran_subscribed: bool | None
    has_unchecked_assembly_data: bool
    text_in_row_limit: int | None
    large_value_types_out_of_row: bool | None
    is_tracked_by_cdc: bool | None
    lock_escalation: int | None
    lock_escalation_desc: str | None
    is_filetable: bool | None
    is_memory_optimized: bool | None
    durability: int | None
    durability_desc: str | None
    temporal_type: int | None
    temporal_type_desc: str | None
    history_table_id: int | None
    is_remote_data_archive_enabled: bool | None
    is_external: bool
    history_retention_period: int | None = None  # SQL 2019
    history_retention_period_unit: int | None = None  # SQL 2019
    history_retention_period_unit_desc: str | None = None  # SQL 2019
    is_node: bool | None = None  # SQL 2019
    is_edge: bool | None = None  # SQL 2019
    data_retention_period: int | None = None  # SQL 2022
    data_retention_period_unit: int | None = None  # SQL 2022
    data_retention_period_unit_desc: str | None = None  # SQL 2022
    ledger_type: int | None = None  # SQL 2022
    ledger_type_desc: str | None = None  # SQL 2022
    ledger_view_id: int | None = None  # SQL 2022
    is_dropped_ledger_table: bool | None = None  # SQL 2022

    schema: "Schema" = None
    columns: list["Column"] = None
    indexes: set["Index"] = None

    def __post_init__(self):
        self.columns = list()
        self.indexes = set()

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.object_id)
