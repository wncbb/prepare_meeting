l=[0, 6, 9, 4, 3, 5, 2, 8, 1, 7]

def findNth(n, left, right):
    while left<=right:
        print 'left', left, 'right', right
        guess=(left+right)/2
        cnt=0
        nextNum=right
        for x in l:
            if x<guess:
                cnt+=1
            else:
                nextNum=min(x, nextNum)
        
        if cnt==n-1:
            return nextNum

        if cnt<n-1:
            left=guess
        else:
            right=guess

    return 0.0


rst=findNth(5, 0, 100)
print rst
