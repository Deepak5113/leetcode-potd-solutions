class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folderDepth=0
        for log in logs:
            if log=="../":
                folderDepth=max(0,folderDepth-1)
            elif log!="./":
                folderDepth+=1
            
        return folderDepth