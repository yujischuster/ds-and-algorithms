# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:

# if length of both lists are the same
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         num1 = ""
#         num2 = ""
#         def traverse(l1, l2, num1, num2):
#             if l1 == None:
#                 total = int(num1[::-1]) + int(num2[::-1])
#                 arr = [int(d) for d in str(total)]
#                 node = None
#                 for i in range(len(arr)):
#                     node = ListNode(arr[i], node)
#                 return node
#             num1 += str(l1.val)
#             num2 += str(l2.val)
#             return traverse(l1.next, l2.next, num1, num2)
            
#         return traverse(l1, l2, num1, num2)

    def create_num(L):
        """
        create number from linked list
        """
        num = ""
        curr = L
        while curr != None:
            num += str(curr.val)
            curr = curr.next
        return int(num[::-1])    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  
        # exceptions
        if l1.val == 0 and l1.next == None:
            return l2
        elif l2.val == 0 and l2.next == None:
            return l1   
        # sum and create array
        total = create_num(l1) + create_num(l2)
        arr = [int(d) for d in str(total)]
        # array to linked list
        nodes = None
        for a in arr:
            nodes = ListNode(a, nodes)
        return nodes
