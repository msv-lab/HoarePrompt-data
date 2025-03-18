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
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, `n` is an input integer representing the number of elements in the list, `l` is a list of `n` integers obtained from the input, `e` is a set of unique integers from the list `l`, and `m` is the length of the list `l`. After each iteration, the program checks if the integer 1 is in the list `l`. If it is, the program prints 'Bob'; otherwise, it prints 'Alice'. The state of `t` remains unchanged, and the values of `n`, `l`, `e`, and `m` are updated with the values from the current test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines and prints whether 'Bob' or 'Alice' wins based on whether there is at least one pile with exactly one stone.

