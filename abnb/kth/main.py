class Solution:
    def kth(self, a, b, k):
        m=len(a)
        n=len(b)
        if m==0:
            return b[k-1]
        if n==0:
            return a[k-1]
        if k==m+n:
            if a[m-1]>b[n-1]:
                return a[m-1]
            else:
                return b[n-1]

        i=float(m)/(m+n)*(k-1)
        j=k-1-i
        if j>=n:
            j=n-1
            i=k-n

        if 
