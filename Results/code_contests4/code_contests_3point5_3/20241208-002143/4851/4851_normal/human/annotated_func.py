#State of the program right berfore the function call: **
def func_1(a):
    stack, ans = [], 0
    for i in a:
        while stack and stack[-1] < i:
            stack.pop()
        
        stack.append(i)
        
        if len(stack) > 1:
            ans = max(ans, stack[-1] ^ stack[-2])
        
    #State of the program after the  for loop has been executed: `stack` contains elements in non-decreasing order, `ans` is the maximum XOR result of any two elements in the `stack`.
    return ans
    #The program returns the maximum XOR result of any two elements in the 'stack'
#Overall this is what the function does:The function accepts a list of elements, maintains a stack of elements in non-decreasing order, and calculates the maximum XOR result of any two elements in the stack.

