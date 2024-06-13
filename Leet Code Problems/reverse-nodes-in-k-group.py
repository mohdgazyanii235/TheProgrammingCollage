# problem url - https://leetcode.com/problems/reverse-nodes-in-k-group/description/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
class Solution:

    def printList(self, head: ListNode):
        while head.next:
            print(str(head.val) + " -> ", end="")
            head = head.next
        print(head.val)

    def reverseList(self, head: ListNode) -> ListNode:
        last_node = None
        while head:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node
        head = last_node # becase current head is none.
        return head
    

    def appendToList(self, head, item) -> ListNode:
        if not head:
            return item

        current = head
        while current.next:
            current = current.next
        current.next = item
        return head

    def reverseKGroup(self, head, k: int) -> ListNode:
        finalList = None
        temp_list = head
        current = temp_list
        counter = 1
        while current:
            if counter == k:
                counter = 1
                next_node = current.next
                current.next = None
                temp_list = self.reverseList(temp_list)
                finalList = self.appendToList(finalList, temp_list)
                temp_list = next_node
                current = temp_list
            elif counter < k:
                current = current.next
                counter += 1
        
        finalList = self.appendToList(finalList, temp_list)
        
        return finalList
        





solution = Solution()

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

solution.printList(list)
solution.printList(solution.reverseKGroup(list, 2))
