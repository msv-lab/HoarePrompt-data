#State of the program right berfore the function call: The function `func_1` does not take any parameters, but it is expected to read input from stdin. The input consists of: the first line containing two integers n and t, where 2 ≤ n ≤ 2×10^5 and t = 1, representing the number of nodes in the tree and the number of rounds, respectively. The next n-1 lines contain pairs of integers u and v, where 1 ≤ u, v ≤ n, each representing an edge in the tree. The tree is guaranteed to have exactly two leaves. The last line contains a single integer u_1, where 1 ≤ u_1 ≤ n, indicating the starting node for the round.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: The `numbers` list contains all the pairs of integers representing the edges in the tree, and the loop has stopped after reading the last line which contains a single integer.
    return numbers
    #The program returns the list `numbers` which contains all the pairs of integers representing the edges in the tree.
#Overall this is what the function does:The function `func_1` reads input from stdin until a line with a different format is encountered. It expects the input to start with `n-1` lines, each containing a pair of integers representing edges in a tree, followed by a line with a single integer. The function returns a list of lists, where each inner list contains a pair of integers representing the edges in the tree. The input line with a single integer is not included in the returned list.

