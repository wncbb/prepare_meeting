class Solution:
    def justify(self, wl, maxWidth, tl, left_align=False):
        extra_spaces = maxWidth - tl
        if not left_align and len(wl) > 1:
            l = len(wl)
            i = 0
            while extra_spaces > 0:
                # distribute whitespaces
                wl[i] += ' '
                i += 1
                extra_spaces -= 1
                if i == l-1:
                    i = 0
            return ''.join(wl)
        # left justified
        ret = ' '.join(wl)
        while len(ret) < maxWidth:
            ret += ' '
        return ret
            
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        # write your code here
        ret = []
        tl = 0  # total words length
        wl = []  # word list
        for word in words:
            if tl + len(wl) + len(word) > maxWidth:
                ret.append(self.justify(wl, maxWidth, tl))
                wl = [word]
                tl = len(word)
            else:
                tl += len(word)
                wl.append(word)
        # last line should be left justified, if it happens to be tl + wl + len(word) == maxWidth for the last line, then left justified won't matter
        if len(wl) > 0:
            ret.append(self.justify(wl, maxWidth, tl, True))
        return ret
