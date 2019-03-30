class Solution:

    def justify(self, words, maxWidth, isLast=False):
        print 'words:{}, maxWidth:{}'.format(words, maxWidth)
        ret=''
        if isLast or len(words)==1:
            ret+=' '.join(words)
        else:
            nonSpaceLen=0
            for word in words:
                nonSpaceLen+=len(word)
            interval=(maxWidth-nonSpaceLen)/(len(words)-1)
            moreSpace=(maxWidth-nonSpaceLen)%(len(words)-1)
            for i in range(len(words)-1):
                ret=ret+words[i]+' '*interval
                if moreSpace>0:
                    ret=ret+' '
                    moreSpace=moreSpace-1
            ret=ret+words[-1]
        ret+=' '*(maxWidth-len(ret))
        return ret
            

    def justify2(self, wl, maxWidth, tl, left_align=False):
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
                ret.append(self.justify(wl, maxWidth, False))
                wl = [word]
                tl = len(word)
            else:
                tl += len(word)
                wl.append(word)
        # last line should be left justified, if it happens to be tl + wl + len(word) == maxWidth for the last line, then left justified won't matter
        if len(wl) > 0:
            ret.append(self.justify(wl, maxWidth, True))
        return ret

words=["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

s=Solution()
ret=s.fullJustify(words, maxWidth)
for v in ret:
    print v