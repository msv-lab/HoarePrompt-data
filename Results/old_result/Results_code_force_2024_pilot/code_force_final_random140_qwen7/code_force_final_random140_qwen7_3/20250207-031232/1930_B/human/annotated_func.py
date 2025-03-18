#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: The list `p` contains all odd numbers from 1 up to `a-1`, `i` is equal to `a`, and `a` is greater than 3.
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer `t` (1 ≤ t ≤ 10³) and an integer `n` (3 ≤ n ≤ 10⁵), where the sum of all `n` values does not exceed 10⁵. For each test case, the function generates a sequence of integers from 1 to `a` (where `a` is the input value for each test case), ensuring the sequence alternates between odd and even numbers. The function then prints this sequence for each test case.

