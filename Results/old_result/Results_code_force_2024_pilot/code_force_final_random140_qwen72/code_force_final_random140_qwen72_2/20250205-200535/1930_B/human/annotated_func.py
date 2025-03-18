#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^3, representing the number of test cases. For each test case, n is an integer where 3 ≤ n ≤ 10^5, representing the length of the permutation p.
def func():
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: After the loop executes all the iterations, `t` is an integer where 1 ≤ t ≤ 10^3, and for each test case, `a` is an integer where 3 ≤ a ≤ 10^5. The variable `i` is the last value of the loop index, which is `a` if `a` is odd or `a + 1` if `a` is even. The list `p` contains all even numbers from 2 up to and including `a` if `a` is even, or up to `a - 1` if `a` is odd, followed by all odd numbers from 1 up to and including `a` if `a` is odd, or up to `a - 1` if `a` is even.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by an integer `a` (3 ≤ a ≤ 10^5). For each test case, the function generates and prints a permutation of integers from 1 to `a`. The permutation starts with all even numbers from 2 up to and including `a` (or `a - 1` if `a` is odd), followed by all odd numbers from 1 up to and including `a` (or `a - 1` if `a` is even). The function does not return any values; it only prints the permutations for each test case. After processing all test cases, the function completes its execution.

