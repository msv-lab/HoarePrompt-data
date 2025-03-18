#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each i, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: After the loop executes all iterations, `t` must be greater than 0, `i` is equal to `t`, `n` is an input integer, `l` is a list of integers obtained from splitting the input string and converting each element to an integer, `e` is a set containing unique elements from the list `l`, `m` is the length of the list `l`. The final output will be 'Bob' if 1 is present in the list `l` for any iteration, otherwise, it will be 'Alice'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer t and a list of n integers. For each test case, it checks if the number 1 is present in the list. If 1 is found in any list, it prints 'Bob'; otherwise, it prints 'Alice'. The function does not return a value but prints the result for each test case.

