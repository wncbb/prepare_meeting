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
        for c in word:
            # 用children[c] or chidlren.get(c)
            child=p.children.get(c)
            if child is None:
                child=TrieNode(c)
                p.children[c]=child
            p=child
        p.isWord=True

class Solution:
    def helper(self, dp, node, tempWord, layer):
        # 判断需要加上 and dp[len(dp)-1]<=k
        # self.k, not k
        if node.isWord and dp[len(dp)-1]<=self.k:
            self.result.append(''.join(tempWord))

        # curDp咋来的?
        # node有很多child， 每个一组dp
        for ch in node.children:
            curDp=[0]*len(self.target)
            curDp[0]=layer
            for j in range(1, len(self.target)):
                # should be self.target[j], not j
                if ch==self.target[j]:
                    curDp[j]=dp[j-1]
                else:
                    curDp[j]=min(dp[j], dp[j-1], curDp[j-1])+1

            nextNode=node.children.get(ch)
            tempWord.append(nextNode.value)
            self.helper(curDp, nextNode, tempWord, layer+1)
            tempWord.pop()

    def kDistance(self, words, target, k):
        root=TrieNode('')
        for word in words:
            TrieNode.insert(root, word)

        target='$'+target
        self.k=k
        self.target=target
        self.result=[]
        dp=[i for i in range(len(target))]
        self.helper(dp, root, [], 1)
        return self.result

words=["abc", "abd", "abcd", "adc"]
target="ac"
k=1

s=Solution()
print s.kDistance(words, target, k)

