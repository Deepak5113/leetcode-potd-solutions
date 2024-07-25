class Solution:
    def merge(self,arr,l,m,r):
        n1=m-l+1
        n2=r-m
        L=[0]*n1
        R=[0]*n2
        for i in range(n1):
            L[i]=arr[l+i]
        for j in range(n2):
            R[j]=arr[m+j+1]
        i,j,k=0,0,l
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<n1:
            arr[k]=L[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=R[j]
            j+=1
            k+=1

    def mergesort(self,arr,l,r):
        if l<r:
            m=l+(r-l)//2
            self.mergesort(arr,l,m)
            self.mergesort(arr,m+1,r)
            self.merge(arr,l,m,r)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums