#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is an input integer such that 1 ≤ `t` ≤ 10^4; no other variables from the loop body are retained.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then determines whether the number 1 is present in the list and prints 'Bob' if it is, otherwise it prints 'Alice'.

