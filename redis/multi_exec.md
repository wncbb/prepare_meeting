#### References

[https://redis.io/topics/transactions](https://redis.io/topics/transactions)


#### redis 事务

`multi/exec` 

`discard`会放弃事务里的所有命令

但是exec开始后，如果某条命令失败，其他命令照常执行.

在exec时，事务涉及到的key如果处于watch状态，且有其他人修改，整个事务都不会执行。



```