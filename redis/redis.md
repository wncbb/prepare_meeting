## Remote Dictionary Server。

#### 数据持久化方式

1. rdb

2. aof

#### 缓存逐出策略

| 数据集 | 方式 |
|-------|-----|
| allkeys | lru |
| volatile | random |
| - | ttl |
| - | lfu |

* noeviction: return errors when the memory limit was reached and the client is trying to execute commands that could result in more memory to be used (most write commands, but DEL and a few more exceptions).

* allkeys-lru: evict keys by trying to remove the less recently used (LRU) keys first, in order to make space for the new data added.

* volatile-lru: evict keys by trying to remove the less recently used (LRU) keys first, but only among keys that have an expire set, in order to make space for the new data added.

* allkeys-random: evict keys randomly in order to make space for the new data added.

* volatile-random: evict keys randomly in order to make space for the new data added, but only evict keys with an expire set.

* volatile-ttl: evict keys with an expire set, and try to evict keys with a shorter time to live (TTL) first, in order to make space for the new data added.

* volatile-lfu Evict using approximated LFU among the keys with an expire set.

* allkeys-lfu Evict any key using approximated LFU.

#### 数据结构

* key

* list

* hash

* set

* zset

* hyperloglog

* pub/sub

* geo

* BloomFilter

* RedisSearch

* Redis-ML

 