#### References

[https://dev.mysql.com/doc/refman/8.0/en/explain-output.html](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html)

#### explain

```sql
explain <sql>;
```

* id
  
    The `SELECT` identifier.    
    执行编号，标识select所在行。
* select_type
  
    The `SELECT` type.

    select查询类型
    * simple
  
        > Simple `SELECT`(not using `UNION` or subqueries.)

    * primary
  
        > Outermost `SELECT`.
    
    * union
    
        > Second or later `SELECT` statement in a `UNION`.

        表示此查询是union的第二或随后的查询

    * depend union

        > Second or later `SELECT` statement in a `UNION`, dependent on outer query.

        union中的第二个或者后面的查询，取决于外面的查询

    * union result

        Result of a `UNION`.

        union的结果

    * subquery

        > First `SELECT` in subqeury.
     
        子查询中的第一个select

    * dependent subquery

        > First`SELECT` in subquery, dependent on outer query. 
    
    * derived
  
        > Derived table.
    
    * materialized
  
        > Materialized subquery.
    
    * uncacheable subquery
  
        > A subquery for which the result cannot be cached and must be re-evaluated for each row of the outer query.
    
    * uncacheable union
 
        > The second or later select in a `UNION` that belongs to an uncacheable subquyery.

* table
  
    The table for the output row.

    查询的表名
* partitions
  
    The matching partitions.

    匹配的分区
* type
  
    The join type.

    join类型(重要)
    
    
    system > const > eq_ref > ref > range~index_merge > index > All 

    * system
        > The table has only one row(=system table). This is a special case of the `const` join type.

        表示表中只有一条数据，是特殊的cosnt类型。

    * const
        > The table has at most one matching row, which is read at the start of the query. Because there is only one row, values from the column in this row can be regarded as constants by the rest of the optimizer. Const tables are very fast because they are read only once.
        
        > `const` is used when you compare all parts of a `PRIMARY KEY` or `UNIQUE` index to constant values.

    * eq_ref
        > One row is read from this table for each combination of rows from the previous tables. Other than the system and const types, this is the best possilbe join type. It is used when all parts of an index are used by the join and the index is a `PRIMARY KEY` or `UNIQUE NOT NULL` index.

    * ref
        > All rows with matching index values are read from this table for each combination of rows from the previous tables. ref is used if the join uses only a leftmost prefix of the key is not a `PRIMARY KEY` or `UNIQUE` index (in other words, if the join cannot select a single row based on the key value). If the key that is used matches only a few rows, this is a good join type.
        触发时机: 触发联合索引最左原则，或者这个索引不是主键，也不是唯一索引 (换句话说，如果这个索引基础之上查询的结果多于一行)。
    * fulltext
        > The join is performed using a FULLTEXT index.
    * ref_or_null
        > This join type is like ref, but with the addition that MYSQL does an extra search for rows that contain NULL values. This join type optimization is used most often in resolving subqueries. In the following examples, MYSQL can use a  ref_or_null join to process ref_table.
    * index_merge
        > This join type indicates that the index Merge optimization is used. In this case, the key column in the output row contains a list of indexes used, and key_len contains a list of the longest key parts for the indexes used.
    * unique_subquery
        > This type replaces eq_ref for some IN subqueries of the following from.

    * index_subquery
        > This join type is similar to unique_subquery. It replaces IN subqueries, but it works for nonunique indexes in subqueries of the following form.
    * range
        > Only rows that are in a given range are retrieved, using an index to select the rows. The key column in the output row indicates which index is used. The key_len contains the longest key part that was used. The ref column is NULL for this type.
    * index
        > The index join type is the same as ALL, except the index tree is scanned. This occurs two ways: 1. If the index is a covering index for the queries and can be used to satisfy all data required from the table, only the index tree is scanned. In this case, the Extra column says Using index. An index-only scan usually is faster than ALL because the size of the index usually is smaller than the table data. 2. A full table scan is performed using reads from the index to look up data rows in index order. Uses index does not appear in the Extra column.

    * ALL
        > A full table scan is done for each combination of rows from the previous tables. This is normally not good if the table is the first table not marked const, and usually very bad in all other cases. Normally, you can avoid ALL by adding indexes that enable row retrieval from the table based on constant values or column values from earlier tables.

* possible_keys
  
    The possible indexes to choose.

    此次查询中，可能用到的索引

* key
    
    The index actually chosen.

    此次查询中，确切使用到的索引

* key_len
    
    The length of the chosen key.

* ref
    
    The columns compared to the index.

    哪个字段或常数与key一起使用

* rows
  
    Estimate of rows to be examined.
  
    此次查询一共扫描了多少行(估值)

* filtered
    
    Percentage of rows filtered by table condition.

    此次查询过滤的数据的百分比

* Extra
    
    Additional information.

    额外的信息
