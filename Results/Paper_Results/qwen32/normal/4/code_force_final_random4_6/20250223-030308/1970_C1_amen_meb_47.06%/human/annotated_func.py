#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, the next n-1 lines contain pairs of integers (u, v) representing edges of the tree where 1 ≤ u, v ≤ n, and the last line contains a single integer u_1 representing the starting node of the stone, where 1 ≤ u_1 ≤ n. The tree is guaranteed to have exactly two leaves.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, the next n-1 lines contain pairs of integers (u, v) representing edges of the tree where 1 ≤ u, v ≤ n, and the last line contains a single integer u_1 representing the starting node of the stone, where 1 ≤ u_1 ≤ n; `numbers` is a list containing n-1 elements `[[num1, num2], [num1, num2], ..., [num1, num2]]` representing all the edges of the tree; `nums` is a list of strings obtained from the most recent input; `num1` is the integer value of `nums[0]` from the last input; `num2` is the integer value of `nums[1]` from the last input.
    return numbers
    #The program returns the list `numbers` which contains n-1 elements, where each element is a pair of integers [num1, num2] representing the edges of the tree.
#Overall this is what the function does:The function reads input representing the edges of a tree and returns a list of these edges as pairs of integers.

