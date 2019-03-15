# -*- encoding: utf-8 -*-


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        wordDict={}
        res=[]
        for i in range(len(words)):
            wordDict[words[i]]=i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp1=words[i][:j]
                tmp2=words[i][j:]
                if tmp1[::-1] in wordDict and wordDict[tmp1[::-1]]!=i and tmp2==tmp2[::-1]:
                    res.append([i, wordDict[tmp1[::-1]]])
                # A B  
                if j!=0 and tmp2[::-1] in wordDict and wordDict[tmp2[::-1]]!=i and tmp1==tmp1[::-1]:
                # if tmp2[::-1] in wordDict and wordDict[tmp2[::-1]]!=i and tmp1==tmp1[::-1]:
                    res.append([wordDict[tmp2[::-1]], i])
        return res

    # wordict = {}
    # res = [] 
    # for i in range(len(words)):
    #     wordict[words[i]] = i
    # for i in range(len(words)):
    #     for j in range(len(words[i])+1):
    #         tmp1 = words[i][:j]
    #         tmp2 = words[i][j:]
    #         if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
    #             res.append([i,wordict[tmp1[::-1]]])
    #         if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
    #             res.append([wordict[tmp2[::-1]],i])
                
    # return res

words=["bat", "tab", "cat"]

s=Solution()
print s.palindromePairs(words)
