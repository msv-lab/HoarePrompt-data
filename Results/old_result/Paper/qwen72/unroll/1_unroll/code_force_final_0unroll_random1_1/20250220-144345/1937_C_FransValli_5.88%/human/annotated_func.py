#State of the program right berfore the function call: The function operates in an interactive environment where the input is a sequence of integers p_0, p_1, ..., p_{n-1}, which is a permutation of {0, 1, ..., n-1}. The function can ask at most 3n queries of the form "? a b c d" where 0 <= a, b, c, d < n, and receives a comparison result "<", ">", or "=" based on the bitwise OR of the selected indices. The function must find and output a pair of indices i and j (0 <= i, j < n) such that p_i ⊕ p_j is maximized, and the number of test cases t (1 <= t <= 10^3) and the sum of n over all test cases do not exceed 10^4.
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
        
    #State: The function has completed all iterations of the loop and has output a pair of indices (k, best) for each test case, such that the bitwise XOR of the elements at these indices in the permutation is maximized. The variables `t` and `n` remain unchanged, while `k` and `best` have been updated to the indices that maximize the XOR for each test case.
#Overall this is what the function does:The function operates in an interactive environment to find and output a pair of indices `i` and `j` such that the bitwise XOR of `p_i` and `p_j` is maximized, given a sequence of integers `p_0, p_1, ..., p_{n-1}` which is a permutation of `{0, 1, ..., n-1}`. The function can ask at most 3n queries to determine the comparison results based on the bitwise OR of selected indices. It handles up to 10^3 test cases, and the sum of `n` over all test cases does not exceed 10^4. After the function concludes, it has output a pair of indices `(k, best)` for each test case, where `k` and `best` are the indices that maximize the bitwise XOR of the elements in the permutation. The variables `t` and `n` remain unchanged, while `k` and `best` are updated to the indices that maximize the XOR for each test case.

