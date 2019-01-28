## 四种隔离级别

1. read uncommitted

2. read committed

3. repeatable read
   
4. serializable

| 隔离级别 | 脏读 | 不可重复读 | 幻读 |
|------|--|----------|---|
| read uncommitted | Yes | Yes | Yes |
| read committed | No | Yes | Yes |
| repeatable read | No | No | Yes |
| serializable | No | No | No |

```mysql
select @@tx_isolation;
```

## innodb与myisam区别

#### 存储类别
1. innodb
   存储在一个文件中
   

2. myisam
   * 数据文件扩展名: .MYD
   * 数据索引文件扩展名: .MYI
   * 表格式文件: .frm

#### 存储空间

1. innodb
    会消耗更多的存储空间。会在内存中建立专用的缓存池，用于高速缓存数据与索引。


2. myisam
    可以压缩，存储空间小。支持静态表(数据末尾不能有空格)、动态表、压缩表。

#### 事务

1. innodb
   支持

2. myisam
   不支持

#### 全文索引

1. innodb 
   原生不支持，但是可以使用sphinx插件支持

2. myisam
   支持FULLTEXT全文索引


#### 外键

1. innodb
   支持外键

2. myisam
   不支持外键

#### 获取表的行数

1. innodb
   扫全表

2. myisam
   会有专门的数据存储表的行数

#### 崩溃后恢复

1. innodb
   相对容易

2. myisam
   相对困难





