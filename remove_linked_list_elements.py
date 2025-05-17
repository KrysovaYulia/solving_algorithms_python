class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode()
        tail = dummy
        while head:
            if head.val != val:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next
        return dummy.next

node6 = ListNode(6)
node5 = ListNode(1, node6)
node4 = ListNode(3, node5)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)
solution = Solution()
reversed_head = solution.removeElements(node1, 1)