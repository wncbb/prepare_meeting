def countingValleys(n, s):
    curHight=0
    vallyNum=0
    for ch in n:
        if ch=='_':
            continue
        if ch=='/':
            curHight+=1
        if ch=='\':
            if curHight==0:
                vallyNum+=1
            curHight-=1
    return vallyNum


print countingValleys(8, '')