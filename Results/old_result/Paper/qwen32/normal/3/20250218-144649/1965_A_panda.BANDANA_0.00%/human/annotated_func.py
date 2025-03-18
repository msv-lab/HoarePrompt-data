#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the program reads an integer `n` and a list `l` of `n` integers. It checks if the integer 1 is in the list `l`. If 1 is present, it prints 'Bob'; otherwise, it prints 'Alice'. The variables `n`, `l`, `e`, `m`, and `i` are updated for each iteration, but `t` remains unchanged as it represents the total number of test cases.
#Overall this is what the function does:The function reads a number of test cases and for each test case, it reads a number of piles and the number of stones in each pile. It then determines and prints the winner ('Bob' if there is at least one pile with one stone, otherwise 'Alice') for each test case.

