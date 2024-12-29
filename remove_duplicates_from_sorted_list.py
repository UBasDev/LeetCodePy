from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next = None):
        self.val: int = val
        self.next: ListNode = next

class RemoveDuplicatesFromSortedListSolution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        response: ListNode = ListNode()
        node_stack: list[ListNode] = []
        while True:
            node_stack.append(head.val)
            if head.next is None:
                response.val = node_stack.pop()
                break
            head = head.next
        for _ in range(len(node_stack)):
            l = node_stack.pop()
            if response.val != l:
                new_response = ListNode(l)
                new_response.next = response
                response = new_response
        return response