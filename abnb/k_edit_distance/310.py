# -*- encoding: utf-8 -*-

import collections

class TrieNode:
    def __init__(self, value):
        self.isWord=False
        self.value=value
        self.children=collections.defaultdict()

    @classmethod
    def insert(cls, root, word):
        p=root
        for c in word:
            # should be p, not root
            child=p.children.get(c)
            if child is None:
                child=TrieNode(c)
                p.children[c]=child
            p=child
        p.isWord=True

class Solution:
    def dfs(self, prevDp, root, tempWord, layer):
        print 'tempWord ', tempWord
        print 'prevDp ', prevDp
        if root.isWord and prevDp[-1]<=self.k:
            print tempWord
            self.result.append(''.join(tempWord))

        for ch in root.children:
            dp=[0]*len(self.target)
            dp[0]=layer
            for j in range(1, len(self.target)):
                if ch==self.target[j]:
                    dp[j]=prevDp[j-1]
                else:
                    dp[j]=min(prevDp[j], prevDp[j-1], dp[j-1])+1
            tempWord.append(ch)
            self.dfs(dp, root.children[ch], tempWord, layer+1)
            tempWord.pop()

    def kDistance(self, words, target, k):
        self.result=[]
        self.target='$'+target
        self.k=k
        
        root=TrieNode('')
        for word in words:
            TrieNode.insert(root, word)

        # dp=[0]*len(target)
        # for i in range(len(target)):
        #     dp[i]=i
        dp=[i for i in range(len(self.target))]

        self.dfs(dp, root, [], 1)
        return self.result



words=["abc", "abd", "abcd", "adc"]
target="ac"
k=1

s=Solution()
print s.kDistance(words, target, k)
