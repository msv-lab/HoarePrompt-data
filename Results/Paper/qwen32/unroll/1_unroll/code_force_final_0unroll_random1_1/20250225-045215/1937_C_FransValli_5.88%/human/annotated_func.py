#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The function can interactively query up to 3n times per test case by providing four indices a, b, c, d (0 ≤ a, b, c, d < n) to receive a comparison result of (p_a | p_b) and (p_c | p_d). The goal is to determine any pair of indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized. The sum of n across all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: After the loop executes all iterations, the output state will be a series of pairs of indices (k, best) for each test case, where (p_k ⊕ p_best) is maximized. The variables k and best are determined through a series of comparisons using the provided query mechanism. The initial state variables not directly affected by the loop remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each involving a permutation of integers. It interactively queries the system to compare bitwise OR results of pairs of elements from the permutation. The function's purpose is to identify and output a pair of indices for each test case such that the bitwise XOR of the elements at these indices is maximized.

