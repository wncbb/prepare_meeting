class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        pre = collections.defaultdict(set)
        suc = collections.defaultdict(set)

        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        charToProcess = chars - set(pre)
        order = ''
        while charToProcess:
            ch = charToProcess.pop()
            order += ch
            for b in suc[ch]:
                pre[b].discard(ch)
                if not pre[b]:
                    charToProcess.add(b)
        return order * (set(order) == chars)
