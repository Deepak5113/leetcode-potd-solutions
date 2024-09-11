class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start=bin(start).replace('0b','')
        goal=bin(goal).replace('0b','')
        if len(start)>=len(goal):
            m=len(start)-len(goal)
            goal='0'*m+goal
        else:
            m=len(goal)-len(start)
            start='0'*m+start
        count=0
        for i in range(len(start)):
            if start[i]!=goal[i]:
                count+=1
        return count



