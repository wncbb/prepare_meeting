import collections

class Solution(object):
    def numMatchingSubseq(self, S, words):
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))


        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])


s=Solution()

S="abcde"
words = ["a", "bb", "acd", "ace"]
print s.numMatchingSubseq(S, words)

