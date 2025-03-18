#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The function can interactively query up to 3n times per test case by providing four indices a, b, c, and d (0 ≤ a, b, c, d < n) to receive a comparison result of (p_a | p_b) and (p_c | p_d). The function's goal is to determine a pair of indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized.
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
        
    #State: `R` is a lambda function that reads an integer from the input. The variables `n`, `g`, `v1`, `v2`, `prev`, and `r` will have values determined by the last iteration of the loop, but these are not specified as they depend on the input provided during execution.
#Overall this is what the function does:The function determines and returns a pair of indices from a given permutation such that the bitwise XOR of the elements at these indices is maximized. It interactsively queries up to 3n times by providing four indices to receive comparison results of bitwise OR operations on the elements of the permutation.

