class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for i in s:
            if i == '[':
                stack.append(i) 
            elif stack and stack[-1] == '[':
                stack.pop() 
            else:
                stack.append(i)

        return math.ceil(len(stack) // 2 / 2.0)
                