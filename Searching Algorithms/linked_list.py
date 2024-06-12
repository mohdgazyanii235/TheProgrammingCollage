class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    

# Print a linked list

def print_list(head: ListNode):
    while head.next:
        print(str(head.val) + " -> ", end="")
        head = head.next
    print(head.val)

def print_list_recursive(head):
    if head:
        if head.next:
            print(str(head.val) + " -> ", end="")
        else:
            print(head.val)
        print_list_recursive(head.next)

# Reverse a linked list
def reverse(head: ListNode) -> ListNode:
    final = None
    while head.next:
        final = ListNode(head.val, final)
        head = head.next
    final = ListNode(head.val, final)
    return final


# Reverse a linked list in position
def reverse_in_position(head: ListNode) -> ListNode:
    last_node = None
    while head:
        next_node = head.next
        head.next = last_node
        last_node = head
        head = next_node
    head = last_node
    return head


# Insert at end of linked list
def insert(head: ListNode, item) -> ListNode:
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(item, None)
    return head

# Insert at start of linked list
def insert_at_start(head: ListNode, item) -> ListNode:
    head = ListNode(item, head)
    return head

# Insert in sorted order in linked list
def insert_sorted(head: ListNode, item) -> ListNode:
    if not head or item < head.val:
        return ListNode(item, head)

    current = head
    while current.next and current.next.val < item:
        current = current.next
    
    current.next = ListNode(item, current.next)

    return head

list = ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
# print_list(list)
# print_list_recursive(list)


# print_list(reverse(list))
# print_list(reverse_in_position(list))

# print_list(insert(list, 4))
# print_list(insert_at_start(list, 4))
# print_list(insert_sorted(list, 4))

