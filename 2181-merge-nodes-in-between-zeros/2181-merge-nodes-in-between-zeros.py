# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        current = head.next  # Skip the initial zero
        sum_val = 0

        while current:
            if current.val == 0:
                if sum_val > 0:
                    tail.next = ListNode(sum_val)
                    tail = tail.next
                    sum_val = 0
            else:
                sum_val += current.val
            current = current.next

        return dummy.next