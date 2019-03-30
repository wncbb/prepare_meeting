import sys

class Solution:
    def findMedianSortedArrays(self, A, B):
        aLen=len(A)
        bLen=len(B)
        if (aLen+bLen)%2==0:
            num1=self.findKth(A, B, (aLen+bLen)/2)
            num2=self.findKth(A, B, (aLen+bLen)/2+1)
            print num1, num2
            return (num1+num2)/2.0
        else:
            return self.findKth(A, B, (aLen+bLen)/2+1)

    def findKth(self, A, B, k):
        if len(A)==0:
            return B[k-1]
        if len(B)==0:
            return A[k-1]
        if k==1:
            return min(A[0], B[0])

        halfA=sys.maxint
        if len(A)>=k/2:
            halfA=A[k/2-1]

        halfB=sys.maxint
        if len(B)>=k/2:
            halfB=B[k/2-1]

        if halfA<halfB:
            return self.findKth(A[k/2:], B, k-k/2)
        return self.findKth(A, B[k/2:], k-k/2)


s1=[1,2,3,4,5,6]
s2=[2,3,4,5]
s=Solution()
# print s.findMedianSortedArrays(s1, s2)

for i in range(1, 11, 1):
    print s.findKth(s1, s2, i)


s1=[1,2,3,4,5,6]
s2=[2,3,4,5]
s=Solution()
print s.findMedianSortedArrays(s1, s2)
