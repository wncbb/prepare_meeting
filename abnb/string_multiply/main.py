

class Solution:
    def f(self, s1, s2):
        if len(s1)==0 or len(s2)==0:
            return '0'
        if s1=='0' or s2=='0':
            return '0'
        result=[0]*(len(s1)+len(s2))
        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                mul=int(s1[i])*int(s2[j])
                print s1[i], ' , ', s2[j], ' , ', mul
                posLow=i+j+1
                posHigh=i+j
                mul+=result[posLow]
                result[posLow]=mul%10
                result[posHigh]+=mul/10
        print result
        res=''
        isUselessZero=True
        for num in result:
            if num==0 and isUselessZero:
                continue
            if num!=0:
                isUselessZero=False
            res+=str(num)
        if len(res)==0:
            return '0'
        return res

s=Solution()
print s.f('99', '99')
