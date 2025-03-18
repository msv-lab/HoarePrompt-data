#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers u_1, ..., u_t where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node of the stone for each round.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: `numbers` is a list of all the pairs of integers read from the input until a non-pair input is encountered.
    return numbers
    #The program returns a list of all the pairs of integers read from the input until a non-pair input is encountered.
#Overall this is what the function does:The function reads pairs of integers from the input until a non-pair input is encountered and returns a list of these pairs.

