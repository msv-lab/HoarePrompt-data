#State of the program right berfore the function call: The function `func()` does not take any input parameters directly. Instead, it interacts with an external system to receive the number of test cases `t` (1 ≤ t ≤ 10^3), and for each test case, it receives an integer `n` (2 ≤ n ≤ 10^4) representing the length of a secret permutation `p` of the set {0, 1, ..., n-1}. The function can issue queries in the form of "? a b c d" where 0 ≤ a, b, c, d < n to receive comparisons of bitwise OR operations on elements of `p`. The function must find two indices `i` and `j` such that `p_i ⊕ p_j` is maximized, using at most 3n queries per test case. The sum of `n` over all test cases does not exceed 10^4.
def func():
    I = lambda : list(map(int, input().split(' ')))
    R = lambda : int(input())
    for kp in range(int(input())):
        n = int(input())
        
        g = 0
        
        v1 = 0
        
        for i in range(1, n):
            v2 = i
            print(f'? {v1} {v1} {v2} {v2}')
            sys.stdout.flush()
            r = input('')
            if r == '<':
                v1 = v2
        
        prev = 0
        
        for i in range(1, n):
            print(f'? {v1} {i} {v1} {prev}')
            sys.stdout.flush()
            r = input()
            if r == '>':
                prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: the final values of `prev` and `v1` after the last iteration of the loop.
#Overall this is what the function does:The function `func` interacts with an external system to determine two indices `i` and `j` for each test case, such that the bitwise XOR of the elements at these indices in a secret permutation `p` is maximized. It uses a limited number of queries to achieve this goal.

