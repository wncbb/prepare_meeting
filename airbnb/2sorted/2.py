import sys

class Solution:
    def findMedianSortedArrays(self, A, B):

        m=len(A)
        n=len(B)
        if m>n:
            return self.findMedianSortedArrays(B, A)
        
        iMin=0
        iMax=m
        halfLen=(m+n+1)/2

        while iMin<=iMax:
            # 2
            i=(iMin+iMax)/2
            # 2
            j=halfLen-i
            if i<m and B[j-1]>A[i]:
                iMin=i+1
            elif i>0 and A[i-1]>B[j]:
                # should be iMax, not imax
                iMax=i-1
            else:
                if i==0:
                    maxOfLeft=B[j-1]
                elif j==0:
                    maxOfLeft=A[i-1]
                else:
                    maxOfLeft=max(A[i-1], B[j-1])

                if (m+n)%2==1:
                    return maxOfLeft

                if i==m:
                    minOfRight=B[j]
                elif j==n:
                    minOfRight=A[i]
                else:
                    minOfRight=min(A[i], B[j])

                return (maxOfLeft+minOfRight)/2.0

s1=[5, 6, 7, 8]
s2=[0,1, 2,3]
s=Solution()
print s.findMedianSortedArrays(s1, s2)
