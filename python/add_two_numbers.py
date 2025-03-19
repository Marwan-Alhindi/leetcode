# This solution works but its not a linked list
class Solution:
    def addTwoNumbers(self, l1, l2):
        # reverse the lists
        
        reversed_l1 = []
        for i in range(len(l1)):
            reversed_l1.append(l1.pop())
        
        reversed_l2 = []
        for i in range(len(l2)):
            reversed_l2.append(l2.pop())            
        
        # convert the lists to a single number
        num1 = int("".join(str(d) for d in reversed_l1))
        num2 = int("".join(str(d) for d in reversed_l2))
        # sum them up
        numSum = num1 + num2
        # reverse the sum
        l = [int(i) for i in str(numSum)]
        
        reversed_out = []
        for i in range(len(l)):
            reversed_out.append(l.pop())

        return reversed_out

# How do you implement a linked list?
# 1. Define your own ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Helper function to create a linked list from a Python list
def create_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

# 3. Helper function to convert a linked list back to a Python list
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        l1 = create_linked_list(l1)
        print(type(l1))
        l2 = create_linked_list(l2)
        print(l1.val)
        print(l2.val)

        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return linked_list_to_list(dummyHead.next)
    
x = Solution()
print(x.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))

