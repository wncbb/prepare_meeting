## http 2.0

#### 参考

[https://link.zhihu.com/?target=https%3A//www.mnot.net/talks/h2fe/](https://link.zhihu.com/?target=https%3A//www.mnot.net/talks/h2fe/)

[https://www.mnot.net/talks/h2fe/](https://www.mnot.net/talks/h2fe/)



#### 多路复用(Multiplexing)

1. http 1.1
   浏览器在同一时间，针对同一域名下的请求有一定的数量限制。

2. http 2.0
   实现多流并行而不用依赖建立多个 TCP 连接。HTTP/2把http协议通信的基本单位缩小为一个一个的帧，帧对应逻辑流中的消息，并行地在同一个TCP连接中双向交换消息。

通过二进制分帧，在HTTP/2.0与TCP之间，添加一个二进制分帧层

* 单连接多资源的方式，减少服务端的链接压力，内存占用更少，连接吞吐量更大。

* 由于TCP连接的减少，使网络拥塞状况得到改善，慢启动时间减少，使拥塞、丢包恢复的速度更快。


#### 首部压缩(Header Compression)

#### 服务端推送(Server Push)

HTTP/2.0，服务器可以对客户端的一个请求发送多个响应。