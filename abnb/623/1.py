# -*- coding: utf-8 -*-
def getKdistanceWord(wordList, target, k):
    nodes={}
    for word in wordList:
        curNode=nodes 
        for i in range(len(word)):
            if word[i] not in curNode:
                curNode[word[i]]={}
            curNode=curNode[word[i]]
            if i==len(word)-1:
                curNode['#']=1
                print nodes

    def helper(prevDp, curChar, node, target, prevStr, result):
        # prevDp[i]表示prevStr与target[0:i]的编辑距离
        # curDp[i]表示prevStr+curChar与target[0:i]的编辑距离
        print "len1: ", len(prevStr)+1
        print "len2: ", len()
        curDp=[prevDp[0]+1]
        for i in range(len(target)):
            if curChar==target[i]:
                curDp.append(prevDp[i])
            else:
                # compare with target的前i个字符
                # 不相等的话，要么
                # prevDp[i]+1=dp[a-1][b-1]+1
                # curDp[i]+1 =dp[a][b-1]+1
                # prevDp[i+1]+1=dp[a-1][b]+1
                minDis=min(prevDp[i]+1, curDp[i]+1, prevDp[i+1]+1)
                curDp.append(minDis)
        if curDp[-1]<=k and '#' in node:
            result.append(prevStr+curChar)
            
        for nxt in node:
            if nxt!='#':
                helper(curDp, nxt, node[nxt], target, prevStr+curChar, result)

    result=[]
    for key in nodes:
        prevDp=[i for i in range(len(target)+1)]
        helper(prevDp, key, nodes[key], target, "", result)
    return result

print  getKdistanceWord(["abc", "abd", "abcd", "adc"], "ac", 1)



