# -*- encoding: utf-8 -*-
class TrieNode(object):
    def __init__(self,ch):
        self.val=ch
        self.child={}
        self.isWord=False
        
class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        # write your code here
        def dfs(old_dp,trie,target,temp_word,k,layer):
            global res
            #print [trie.val,trie.isWord,old_dp,trie.child.keys()]
            if trie.isWord==True and old_dp[-1]<=k:
                #print "add: "+''.join(temp_word)
                res.append(''.join(temp_word))
            for ch in trie.child.keys():
                dp = [0]*len(target)
                dp[0]=layer
                for j in range(1,len(target)):
                    if ch==target[j]:
                        dp[j]=old_dp[j-1]
                    else:
                        dp[j]=min([old_dp[j],old_dp[j-1],dp[j-1]])+1
                #print dp
                #if dp[-1]>k:return
                #else:
                temp_word.append(ch)
                dfs(dp,trie.child[ch],target,temp_word,k,layer+1)
                temp_word.pop()
                
            
        root = TrieNode(0)
        for word in words:
            cur = root
            for w in word:
                #num = ord(w)-ord('a')
                #if cur.child[num]==None:cur.child[num]=Trienode(num)
                if w not in cur.child:cur.child[w]=TrieNode(w)
                cur = cur.child[w]
            cur.isWord=True
        target = '$'+target
        dp = [0]*len(target)
        for i in range(len(target)):
            dp[i]=i
        global res
        res = []
        dfs(dp,root,target,[],k,1)
        return res


words=["abc", "abd", "abcd", "adc"]
target="ac"
k=1

s=Solution()
print s.kDistance(words, target, k)