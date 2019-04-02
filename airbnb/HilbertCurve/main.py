

def t(x, y, i):
    if i==0:
        return 1
    areaCnt=1<<(i*2-2)
    borderLen=1<<(i-1)

    if x>=borderLen and y>=borderLen:
        return areaCnt*2+t(x-borderLen, y-borderLen, i-1)
    elif x<borderLen and y>=borderLen:
        return areaCnt+t(x, y-borderLen, i-1)
    elif x<borderLen and y<borderLen:
        return t(y, x i-1)
    else:
        return areaCnt*3+t(borderLen-1-y, 2*borderLen-1-x, i-1)
