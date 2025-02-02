# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        first = head
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
# prev - reversed second part
# merge prev and first part
        while prev:
            temp1, temp2 = first.next, prev.next
            first.next = prev
            prev.next = temp1
            first , prev = temp1, temp2 
        


        