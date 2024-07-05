# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]
        critical_paths=[]
        prev=head
        curr=head.next
        pos=1
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                critical_paths.append(pos)
            prev=curr
            curr=curr.next
            pos+=1
        
        if len(critical_paths)<2:
            return [-1,-1]

        min_distance=float('inf')
        max_distance=critical_paths[-1]-critical_paths[0]
        for i in range(1, len(critical_paths)):
            min_distance=min(min_distance,critical_paths[i]-critical_paths[i-1])
        return [min_distance,max_distance]