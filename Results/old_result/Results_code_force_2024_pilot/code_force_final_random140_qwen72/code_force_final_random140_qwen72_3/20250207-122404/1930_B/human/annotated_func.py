#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case involves a single integer n (3 ≤ n ≤ 10^5), representing the length of the permutation to be generated. The total number of test cases, t, is a positive integer (1 ≤ t ≤ 10^3), and the sum of all n values across all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        a = [int(i) for i in input().split()][0]
        
        p = []
        
        for i in range(2, a + 1, 2):
            p += [i]
        
        for i in range(1, a + 1, 2):
            p += [i]
        
        print(*p)
        
    #State: After all iterations of the loop, `a` remains unchanged for each test case, `p` is a list containing all even numbers from 2 up to and including `a` (if `a` is even) or `a - 1` (if `a` is odd), followed by all odd numbers from 1 up to and including `a` (if `a` is odd) or `a - 1` (if `a` is even). The variable `i` is no longer relevant after the loop completes, and `t` remains unchanged, representing the total number of test cases.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` (3 ≤ n ≤ 10^5) and generates a permutation of length `n`. The permutation starts with all even numbers from 2 up to and including `n` (or `n-1` if `n` is odd), followed by all odd numbers from 1 up to and including `n` (or `n-1` if `n` is even). The function prints the permutation for each test case. The function does not return any value; it only prints the permutations.

