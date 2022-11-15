drop table if exists dbo.t1;
create table t1 (
	pk int identity not null constraint t1pk primary key,
	c1 varchar(20) null,
	c2 varchar(20) null,
	c3 varchar(20) null,
	c4 varchar(20) null,
	c5 varchar(20) null,
	c6 varchar(20) null,
	c7 varchar(20) null,
	c8 varchar(20) null,
	c9 varchar(20) null)

create index c1 on t1 (c1);
create index d1 on t1 (c1);
create index c1c2 on t1 (c1, c2);
create index c1c2_c3 on t1 (c1, c2) include (c3);
-- UNIQUE
create unique index c4c5 on t1 (c4, c5);
create index c5c6c4 on t1 (c5, c6, c4);
create index pkc1 on t1 (pk, c1);