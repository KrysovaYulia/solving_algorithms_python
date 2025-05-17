class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f'{self.val}' 
class Solution:
    def deleteDuplicates(self, head):
        curr = head
        if curr is None:
            return head
        while curr.next != None:

            if curr.val == curr.next.val:
        
                curr.next = curr.next.next
            elif curr.val != curr.next.val:
                curr = curr.next
        return head
      
            
node4 = ListNode(3)
node3 = ListNode(2, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)
solution = Solution()
reversed_head = solution.deleteDuplicates(node1)