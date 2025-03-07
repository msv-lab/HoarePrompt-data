#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The value of `t` is unchanged, and for each test case, the output is the sum of the number of odd values among the first three elements of `p` (which can be 0 or 3) and the integer division of the sum of all elements in `p` by 2.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` (1 <= t <= 10^4) representing the number of test cases. For each test case, it reads a list `p` of four integers (0 <= p_i <= 200) from user input. The function then calculates and prints the sum of the number of odd values among the first three elements of `p` (which can be 0 or 3) and the integer division of the sum of all elements in `p` by 2. The value of `t` remains unchanged after the function execution.

