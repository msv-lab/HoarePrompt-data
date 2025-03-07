#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
def func_1():
    numbers = []
    while True:
        nums = input().split()
        
        if len(nums) != 2:
            break
        
        num1 = int(nums[0])
        
        num2 = int(nums[1])
        
        numbers.append([num1, num2])
        
    #State: Output State: The list `numbers` contains all pairs of integers `[num1, num2]` entered as input until the input no longer consists of exactly two elements. The variables `n`, `t`, `u`, and `v` retain their initial values or states as described in the initial state, with `n` being an integer such that 2 ≤ n ≤ 2×10^5, `t` being 1, `u` and `v` being integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
    #
    #In simpler terms, `numbers` will contain all the pairs of integers provided as input until the input does not consist of exactly two elements. The other variables (`n`, `t`, `u`, `v`) will remain unchanged from their initial states.
    return numbers
    #The program returns the list `numbers` which contains all pairs of integers `[num1, num2]` entered as input until the input no longer consists of exactly two elements. The variables `n`, `t`, `u`, and `v` retain their initial values: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `u` and `v` are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
#Overall this is what the function does:The function processes input pairs of integers [num1, num2] until the input no longer consists of exactly two elements. It retains the initial values of n, t, u, and v: n is an integer such that 2 ≤ n ≤ 2×10^5, t is 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element. The function returns a list numbers containing all processed pairs of integers.

