-- helper code to generate the object classes
select name + ': ' + case sc.system_type_id
when 231 then 'str'
when 52 then 'str'
when 56 then 'int'
when 175 then 'str'
when 61 then 'datetime'
when 104 then 'bool'
when 48 then 'int'
else 'unk'
end + case sc.is_nullable
when 0 then ''
when 1 then ' | None'
end as code
--, *
from sys.system_columns sc
--where sc.object_id = object_id('sys.schemas')
--where sc.object_id = object_id('sys.tables')
--where sc.object_id = object_id('sys.columns')
--where sc.object_id = object_id('sys.indexes')
where sc.object_id = object_id('sys.index_columns')

order by sc.column_id

select * from sys.indexes
select * from sys.index_columns

