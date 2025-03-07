#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The function can interactively query up to 3n times per test case to compare bitwise OR results of pairs of elements in the permutation. The goal is to find any two indices i and j such that the bitwise XOR of p_i and p_j is maximized.
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
        
    #State: After the loop executes all the iterations, the function will have identified two indices k and best such that the bitwise XOR of p_k and p_best is maximized. The function will have interacted with the input/output system to compare bitwise OR results of pairs of elements in the permutation up to 3n times per test case, as allowed. The variables n, k, and best will reflect the state of the last test case processed. The state of other variables not mentioned in the loop head and body remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each involving a permutation of integers from 0 to n-1. For each test case, it interactively queries up to 3n times to compare bitwise OR results of pairs of elements in the permutation. The goal is to identify two indices such that the bitwise XOR of the corresponding elements in the permutation is maximized. After processing all test cases, the function outputs these two indices for each test case.

