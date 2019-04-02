def letterCasePermutation(S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i+ch for i in res]
    return res


s='aBc'
rst=letterCasePermutation(s)
for v in rst:
    print v
