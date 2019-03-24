# -*- encoding: utf-8 -*-

import collections

class TrieNode:
    def __init__(self, value):
        self.value=value
        self.isWord=False
        self.children=collections.defaultdict()

    @classmethod
    def insert(cls, root, word):
        p=root
        for ch in word:
            child=p.children.get(ch)
            if child is None:
                child=TrieNode(ch)
                p.children[ch]=child
            p=child
        p.isWord=True
        p.word=word



class Solution:
    def kDistance(self, words, target, k):
        self.result=[]
        self.target='$'+target
        self.k=k

        root=TrieNode('')
        for word in words:
            TrieNode.insert(root, word)


        dp=[i for i in range(len(self.target))]
        self.helper(dp, root, 1)
        return self.result

    def helper(self, prevDp, node, layer):
        print 'prevDp ', prevDp
        if node.isWord and prevDp[-1]<=self.k:
            self.result.append(node.word)

        for ch in node.children:
            dp=[0]*len(self.target)
            dp[0]=layer
            for j in range(1, len(self.target)):
                if ch==self.target[j]: 
                    dp[j]=prevDp[j-1]
                else:
                    dp[j]=min(prevDp[j], prevDp[j-1], dp[j-1])+1
            # should be the same with self.helper
            # 遍历完毕之后，才能进入下一轮
            self.helper(dp, node.children[ch], layer+1)

words=["abc", "abd", "abcd", "adc"]
target="ac"
k=1
s=Solution()
print s.kDistance(words, target, k)












