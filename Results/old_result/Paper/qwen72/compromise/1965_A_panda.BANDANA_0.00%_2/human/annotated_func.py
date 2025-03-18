#State of the program right berfore the function call: The function `func` is expected to take input through standard input and output through standard output. The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop will execute `t` times, and for each test case, it will read an integer `n` and a list `l` of `n` integers. It will then check if the number 1 is present in the list `l`. If 1 is present, it will print 'Bob'. If 1 is not present, it will print 'Alice'. The variables `t`, `n`, `l`, `e`, and `m` will be updated for each test case, but their final values will depend on the last test case processed. The variable `t` will remain unchanged after the loop finishes.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` representing the number of piles, followed by a list of `n` integers representing the number of stones in each pile. For each test case, it checks if the number 1 is present in the list of stones. If 1 is present, it prints 'Bob' to standard output; otherwise, it prints 'Alice' to standard output. The function does not return any value and does not modify any external state beyond the standard input and output. The variables `t`, `n`, `l`, `e`, and `m` are used internally and their final values are not relevant after the function concludes.

