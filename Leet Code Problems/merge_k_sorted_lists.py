
# problem url - https://leetcode.com/problems/merge-k-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:

    def insert_in_order(self, head: ListNode, item: int) -> ListNode:
        # if head is empty
        if not head:
            head = ListNode(item, None)
        
        # if item is smaller than the head
        elif item <= head.val:
            item = ListNode(item, head)
            head = item
        
        else:
            current = head
            while current.next and item > current.next.val:
                current = current.next
            
            item = ListNode(item, current.next)
            current.next = item
        
        return head

    def mergeKLists(self, lists):
        final_list = None
        for list in lists:
            while list:
                value = list.val
                list = list.next
                final_list = self.insert_in_order(final_list, value)

        return final_list