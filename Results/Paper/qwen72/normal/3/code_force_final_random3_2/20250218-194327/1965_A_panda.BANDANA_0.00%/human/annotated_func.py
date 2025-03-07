#State of the program right berfore the function call: The function `func` is expected to take input through standard input (stdin) and provide output through standard output (stdout). The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is an integer in the range 1 ≤ t ≤ 10^4, `i` is `t-1`, `n` is an input integer, `l` is a list of integers provided by the user, `e` is a set containing the unique elements from the list `l`, and `m` is the length of the list `l`. If `1` is in the list `l`, the set `e` contains the integer 1. Otherwise, `1` is not in the set `e`.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input (stdin). Each test case consists of an integer `n` followed by a list of `n` integers. For each test case, the function checks if the number `1` is present in the list of integers. If `1` is found, it prints 'Bob' to standard output (stdout); otherwise, it prints 'Alice'. The function does not return any value. After processing all test cases, the function concludes, and the state of the program includes the processed test cases and the corresponding output for each.

