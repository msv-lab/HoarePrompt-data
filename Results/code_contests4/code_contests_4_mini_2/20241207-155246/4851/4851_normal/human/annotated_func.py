#State of the program right berfore the function call: a is a list of distinct positive integers, and its length n is such that 1 < n ≤ 10^5, with each integer in the list satisfying 1 ≤ si ≤ 10^9.
def func_1(a):
    stack, ans = [], 0
    for i in a:
        while stack and stack[-1] < i:
            stack.pop()
        
        stack.append(i)
        
        if len(stack) > 1:
            ans = max(ans, stack[-1] ^ stack[-2])
        
    #State of the program after the  for loop has been executed: `stack` contains elements from `a` that are in non-decreasing order, `ans` is the maximum XOR of the last two elements in `stack` if `stack` has at least two elements, otherwise `ans` remains 0.
    return ans
    #The program returns the maximum XOR of the last two elements in the non-decreasing order stack, or 0 if the stack has less than two elements
#Overall this is what the function does:The function accepts a list of distinct positive integers and returns the maximum XOR of the last two elements in a non-decreasing order stack created from the list. If there are fewer than two elements in the stack during execution, it returns 0.

