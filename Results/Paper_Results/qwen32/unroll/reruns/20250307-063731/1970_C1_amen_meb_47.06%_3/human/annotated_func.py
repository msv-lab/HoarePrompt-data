#State of the program right berfore the function call: n is an integer such that 2 \(\leq\) n \(\leq\) 2 \(\times\) 10^5, t is an integer such that t = 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 \(\leq\) u, v \(\leq\) n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 \(\leq\) u_i \(\leq\) n, representing the starting node for each round.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: `numbers` will contain all the pairs of integers that were read from the input until a non-pair line was encountered. All other variables (`n`, `t`, the tree structure, and the starting node `u_1`) remain unchanged.
    #
    #Output State:
    return numbers
    #The program returns `numbers`, which contains all the pairs of integers that were read from the input until a non-pair line was encountered.
#Overall this is what the function does:The function reads pairs of integers from the input until a non-pair line is encountered and returns a list of these pairs.

