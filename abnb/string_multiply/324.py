class Solution:
    # should be t(self, s1, s2)
    # not t(t1, t2)
    def t(self, s1, s2):
        # parameters
        sign=1
        if s1[0]=='-':
            sign=-1*sign
            s1=s1[1:]
        if s2[0]=='-':
            sign=-1*sign
            s2=s2[1:]


        result=[0]*(len(s1)+len(s2))
        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                mul=int(s1[i])*int(s2[j])
                posLow=i+j+1
                posHigh=i+j
                mul+=result[posLow]
                result[posLow]=mul%10
                # should be result[posHigh]+=mul/10
                # not result[posHigh]=mul/10
                result[posHigh]+=mul/10

        res=''
        for num in result:
            if len(res)==0 and num==0:
                continue
            res=res+str(num)
        
        if res=='':
            return '0'
        if sign==-1:
            return '-'+res
        return res


s=Solution()
print s.t('99', '-99')
