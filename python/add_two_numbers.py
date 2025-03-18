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



x = Solution()
print(x.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
print("Hello world")