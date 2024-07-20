class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N=len(rowSum)
        M=len(colSum)
        r,c=0,0
        res=[[0]*M for _ in range(N)]
        while r<N and c<M:
            min_val=min(rowSum[r],colSum[c])
            res[r][c]=min_val
            rowSum[r]-=min_val
            colSum[c]-=min_val
            if rowSum[r]==0:
                r+=1
            else: c+=1
        return res