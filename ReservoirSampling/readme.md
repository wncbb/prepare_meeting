```
有一串数字(在线)，不知道有多少，一个一个的出现。
随机选择10个(不够10个，全取)

对于1-10个，数据，直接存到最终结果里
对于第11个数据，我们生成一个随机数rd=rand(1, 11)
如果rd=11,很不幸，我们不选他
如果rd<=10, 我们把他地换掉第rd个数。

对于第11个数而言:
1/11的概率不取， 10/11的概率取

对于前10个数而言
取的概率是:
P(当第11个数不取)+P(当第11个数取)
=1/11 + 10/11 * 9/10
=1/11 + 9/11
=10/11

所有的数都是10/11，所以成立。

对于第12个数，
2/12的概率不取， 10/12的概率取

假设前n-1个数成立，即对于每个前n-1个数，留下的概率是 k/(n-1)

对于第n个数
取的概率是 k/n
对于前k个数，取的概率是
 P(k个数保留到现在)*(P(当不取第n个数)+P(当取第n个数))
=(k/(n-1)) * ( (n-k)/n + (k/n)*((k-1)/k) )
=k/n



```