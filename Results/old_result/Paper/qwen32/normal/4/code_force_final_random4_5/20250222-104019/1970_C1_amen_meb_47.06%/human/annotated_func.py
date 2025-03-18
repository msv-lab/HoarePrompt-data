#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer where t=1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n and the tree has exactly two leaves, and there is a list of t integers (u_1) where 1 ≤ u_1 ≤ n representing the starting node of the stone.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is an integer where t=1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n and the tree has exactly two leaves, and there is a list of t integers (u_1) where 1 ≤ u_1 ≤ n representing the starting node of the stone. `numbers` is a list containing all the pairs of integers `[num1, num2]` that were read from the input until a non-pair input was encountered.
    return numbers
    #The program returns the list `numbers` which contains all the pairs of integers `[num1, num2]` that were read from the input until a non-pair input was encountered.
#Overall this is what the function does:The function reads pairs of integers from the input until a non-pair input is encountered and returns a list of these pairs.

