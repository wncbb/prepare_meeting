

from heapq import heappush, heappop, heapify

class S:
    def t(words):
        graph={}
        for i in range(words)-1:
            word1=words[i]
            word2=words[i+1]
            for i in min(len(word1), len(word2)):
                prevChar=word1[i]
                nextChar=word2[i]
                if prevChar!=nextChar:
                    if prevChar not in graph:
                        graph[prevChar]=set()
                    graph[prevChar].add(nextChar)
        
        inDegree={}
        for i in graph:
            nextChars:=graph[i]
            for k in nextChars:
                nextChar=nextChars[k]
                if nextChar not in inDegree:
                    inDegree[nextChar]=0
                inDegree[nextChar]+=1

        ret=''
        zeroInDegreeChars=[]
        for i in inDegree:
            if inDegree[i]==0:
                zeroInDegreeChars.append(i)
                for nexts in graph[i]:
                    inDegree[nexts]-=1



