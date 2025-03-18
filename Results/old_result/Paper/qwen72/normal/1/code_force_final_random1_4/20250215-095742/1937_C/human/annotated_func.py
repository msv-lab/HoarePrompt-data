#State of the program right berfore the function call: The function operates in an interactive environment where the input is provided through a series of queries and responses. The input consists of multiple test cases, each defined by an integer n (2 ≤ n ≤ 10^4), representing the size of a permutation p of the set {0, 1, ..., n-1}. The function can make at most 3n queries to determine a pair of indices (i, j) such that p_i ⊕ p_j is maximized. Each query involves selecting four indices a, b, c, d (0 ≤ a, b, c, d < n) and receiving a response indicating the relationship between (p_a | p_b) and (p_c | p_d). The total number of test cases t satisfies 1 ≤ t ≤ 10^3, and the sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has completed all its iterations, and for each test case, the final values of `k` and `best` have been determined. For each test case, `k` is the index that maximizes the bitwise OR operation with the smallest index (0) among all indices, and `best` is the index that maximizes the bitwise OR operation with `k` among all indices. The loop has printed the result for each test case in the format `! k best`.
#Overall this is what the function does:The function operates in an interactive environment and processes multiple test cases. For each test case, it determines a pair of indices (i, j) from a permutation p of the set {0, 1, ..., n-1} such that the XOR of p_i and p_j is maximized. The function makes up to 3n queries to achieve this, where each query involves comparing the bitwise OR of two pairs of indices. After processing all test cases, the function prints the pair of indices (i, j) that maximize p_i ⊕ p_j for each test case in the format `! k best`. The function does not explicitly accept any parameters and does not return any values; instead, it interacts with the environment through standard input and output.

