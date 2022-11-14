def quote(name: str | None) -> str:
    """
    Mimic the SQL Server QUOTENAME function
    TODO: take care of []<>'"(){} characters in the string
    """
    if name is None:
        return ""
    if " " in name:
        return f"[{name}]"
    return name


from .schema import Schema
from .table import Table
from .column import Column
from .index import Index, IndexColumn, IndexUsage
