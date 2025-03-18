#State of the program right berfore the function call: The function operates in an environment where it can interactively query a hidden permutation p of {0, 1, ..., n-1} by specifying four indices a, b, c, d (0 ≤ a, b, c, d < n) and receiving a comparison result between (p_a | p_b) and (p_c | p_d). The goal is to find indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized, using at most 3n queries. The function handles multiple test cases, each with a different permutation, and the total number of test cases and the sum of n across all test cases are bounded.
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
        
    #State: After the loop executes all iterations, `n` is greater than 1, `k` is the index that maximizes the bitwise OR operation with 0 among the indices 1 to n-1, and `best` is the index that maximizes the bitwise OR operation with `k` among the indices 0 to n-1.
#Overall this is what the function does:The function `func` interacts with a hidden permutation of integers from 0 to n-1 by making queries to determine the indices `i` and `j` such that the XOR of the elements at these indices in the permutation is maximized. It does this by performing at most 3n queries. The function handles multiple test cases, each with a different permutation, and outputs the indices `k` and `best` for each case, where `k` is the index that maximizes the bitwise OR operation with 0 among the indices 1 to n-1, and `best` is the index that maximizes the bitwise OR operation with `k` among the indices 0 to n-1. The function does not explicitly accept any parameters and does not return any values; instead, it prints the results directly.

