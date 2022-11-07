select  t.name as table_name,
             i.name as index_name, -- can be null if heap
             t.object_id,
             i.index_id,
             i.type,
             i.type_desc,
             i.is_unique,
             i.ignore_dup_key,
             i.is_primary_key,
             i.is_unique_constraint,
             i.is_disabled,
             i.is_hypothetical,
             i.has_filter,
             ic.index_column_id,
             ic.column_id,
             ic.key_ordinal,
             ic.partition_ordinal,
             ic.is_descending_key,
             ic.is_included_column
from sys.indexes i
join sys.tables t on t.object_id = i.object_id
left join sys.index_columns ic on i.object_id = ic.object_id and i.index_id = ic.index_id
where t.is_ms_shipped = 0
and i.index_id <> 0 and i.index_id is not NULL --skip heaps for now
order by table_name, index_name, key_ordinal