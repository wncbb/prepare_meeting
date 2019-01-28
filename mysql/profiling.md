

```sql
show variables like '%profiling%';

set profiling=on;
show variables like 'profiling';

<sql statements>

show profiles;

-- ALL 显示所有的开销信息
-- BLOCK IO 显示IO相关开销
-- CONTEXT SWITCHES 上下文切换相关开销
-- CPU 显示CPU相关开销信息
-- IPC 显示发送和接收相关开销信息
-- MEMORY 显示内存相关开销信息
-- PAGE FAULTS 显示页面错误相关开销信息
-- SOURCE 显示与source_function, source_file, source_line相关的开销信息
-- SWAPS 显示交换次数相关开销的信息
SHOW PROFILE cpu, block io FOR QUERY id;
-- 当出现下面的内容时，最好需要优化:
-- converting HEAP to MyISAM 查询结果太大，内存不够用，需要使用磁盘
-- creating tmp table 创建临时表
-- copying to tmp table on disk 把内存中临时表复制到磁盘
```


