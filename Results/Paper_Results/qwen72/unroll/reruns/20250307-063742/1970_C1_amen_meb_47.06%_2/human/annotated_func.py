#State of the program right berfore the function call: n is an integer such that 2 \leq n \leq 2 \times 10^5, and the tree is represented by a list of edges where each edge is a tuple (u, v) with 1 \leq u, v \leq n, and the tree has exactly two leaves. The starting node u_1 is an integer such that 1 \leq u_1 \leq n.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: `numbers` is a list of pairs of integers that were input until an input with a different format was encountered. The tree and `n` remain unchanged, and `u_1` also remains unchanged.
    return numbers
    #The program returns the list `numbers` which contains pairs of integers that were input until an input with a different format was encountered.
#Overall this is what the function does:The function `func_1` accepts no parameters and processes pairs of integers from user input until an input with a different format is encountered. It returns a list `numbers` containing the pairs of integers that were input. The function does not modify any external state or variables.

