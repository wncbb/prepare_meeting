
import collections

class TrieNode(object):
    def __init__(self, v):
        self.isWord=False
        self.v=v
        self.children=collections.OrderedDict()

    @classmethod
    def insert(cls, root, word):
        p=root
        for c in word:
            child=p.children.get(c)
            if child is None:
                child=TrieNode(c)
            p.children[c]=child
            p=child
        p.isWord=True

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        self.target=target

        root=TrieNode('')
        for w in words:
            TrieNode.insert(root, w)

        for key in root.children:
            prevDp=[i for i in range(len(target)+1)]
            self.dfs()

    def dfs(self, prevDp, prevStr, curChar, result):
        currDp=[prevDp[0]+1]
        for i in range(len(target)):
            if target[i]==w:
                currDp

"""
 words=['abc', 'bcd', 'abm']
 root=TrieNode('')
 for w in words:
     TrieNode.insert(root, w)

 print dict(root.children)
"""
