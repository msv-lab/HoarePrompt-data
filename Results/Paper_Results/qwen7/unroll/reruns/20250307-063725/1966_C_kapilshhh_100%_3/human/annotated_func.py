#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9; the sum of n over all test cases does not exceed 2⋅10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: Output State: The output state will consist of a series of names ('Alice' or 'Bob') printed based on the conditions within the loop for each test case.
    #
    #Each iteration of the loop processes one test case. For each test case, the loop first reads an integer `n`, which is the length of the array. Then it reads a space-separated list of integers, converts them to a set to remove duplicates, sorts them in descending order, and appends a zero. It then initializes a boolean variable `dp` to `True`. The loop iterates through the array (excluding the last element), checking if the difference between consecutive elements is greater than 1 or if `dp` is `False`. If either condition is met, `dp` remains `True`; otherwise, it becomes `False`. Finally, it prints 'Alice' if `dp` is `True`, and 'Bob' otherwise, before decrementing `tc`.
    #
    #The output state will be a sequence of 'Alice' or 'Bob' for each test case, depending on the input arrays provided for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (number of test cases), an integer `n` (number of piles), and a list of `n` integers representing the initial number of stones in each pile. For each test case, it determines whether Alice or Bob wins based on the distribution of stones across the piles. Specifically, it sorts the list of stones in descending order, removes duplicates, and checks if the difference between any two consecutive stones is greater than 1 or if a certain condition (`dp`) is false. If the condition holds true, it prints 'Alice'; otherwise, it prints 'Bob'. The function does not return any value but prints the result for each test case.

