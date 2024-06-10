# problem link: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        v1 = ""
        v2 = ""

        while l1 is not None:
            v1 = str(l1.val) + v1
            l1 = l1.next
        
        while l2 is not None:
            v2 = str(l2.val) + v2
            l2 = l2.next


        total = str(int(v1) + int(v2))
        
        linkedList = None

        for d in total:
            linkedList = ListNode(d, linkedList)
        
        return linkedList

        