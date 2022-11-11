from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Column:
    object_id: int
    name: str | None
    column_id: int
    system_type_id: int
    user_type_id: int
    max_length: str
    precision: int
    scale: int
    collation_name: str | None
    is_nullable: bool | None
    is_ansi_padded: bool
    is_rowguidcol: bool
    is_identity: bool
    is_computed: bool
    is_filestream: bool
    is_replicated: bool | None
    is_non_sql_subscribed: bool | None
    is_merge_published: bool | None
    is_dts_replicated: bool | None
    is_xml_document: bool
    xml_collection_id: int
    default_object_id: int
    rule_object_id: int
    is_sparse: bool | None
    is_column_set: bool | None
    generated_always_type: int | None
    generated_always_type_desc: str | None
    encryption_type: int | None
    encryption_type_desc: str | None
    encryption_algorithm_name: str | None
    column_encryption_key_id: int | None
    column_encryption_key_database_name: str | None
    is_hidden: bool | None
    is_masked: bool
    graph_type: int | None = None # SQL 2019
    graph_type_desc: str | None = None # SQL 2019

    table: "Table" = None

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash((self.object_id, self.column_id))
