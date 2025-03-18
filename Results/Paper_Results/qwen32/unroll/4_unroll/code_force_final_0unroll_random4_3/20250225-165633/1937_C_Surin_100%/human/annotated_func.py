#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (2 ≤ n ≤ 10^4), representing the length of a secret permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The function can interact with the system by sending queries in the form "? a b c d" where 0 ≤ a, b, c, d < n, and receiving responses "<", "=", or ">" based on the comparison of bitwise OR operations on elements of the permutation. The function must find two indices i and j such that p_i ⊕ p_j is maximized, using at most 3n queries per test case. The sum of n over all test cases does not exceed 10^4.
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
            elif r == '=':
                print(f'? {i} {i} {prev} {prev}')
                sys.stdout.flush()
                r2 = input('')
                if r2 == '<':
                    prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: The variables `v1` and `prev` will hold the two largest distinct numbers for each test case. The variable `g` remains 0, and `n` holds the number of elements in the list for the current test case.
#Overall this is what the function does:The function interacts with a system to determine two indices `i` and `j` of a secret permutation `p` such that the bitwise XOR of `p_i` and `p_j` is maximized. It sends up to 3n queries per test case in the form "? a b c d" to receive comparisons of bitwise OR operations on elements of the permutation. The function outputs the indices `i` and `j` that maximize `p_i ⊕ p_j`.

