#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree has exactly n nodes and n-1 edges, the tree has exactly two leaves, and the next line contains t integers 1 ≤ u_1, ..., u_t ≤ n, each representing the starting node for a round.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: numbers is an empty list.
    return numbers
    #The program returns an empty list.
#Overall this is what the function does:The function reads pairs of integers from the input until a line with a number of elements not equal to 2 is encountered, then returns an empty list.

