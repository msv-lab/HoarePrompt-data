#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, representing the number of piles, and a list of n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9, representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has finished executing all iterations. The variable `t` has not been modified and still represents the initial number of test cases. For each test case, the variables `n` and `l` have been used to process the input, and the variable `e` has been set to a set of unique elements from `l`. The variable `m` has been set to the length of the list `l`. The loop has printed 'Bob' if any pile contains exactly 1 stone, and 'Alice' otherwise. The values of `n`, `l`, `e`, and `m` will be different for each test case, but they will not affect the next test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of a number of piles `n` and a list of integers `l` representing the initial number of stones in each pile. For each test case, it prints 'Bob' if any pile contains exactly 1 stone, and 'Alice' otherwise. The function does not return any value. After the function concludes, the variable `t` remains unchanged, and the variables `n`, `l`, `e`, and `m` are not retained for the next test case.

