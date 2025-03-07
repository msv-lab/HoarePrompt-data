#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p of integers from 0 to n-1. The function can interactively query up to 3n times to compare bitwise OR results of pairs of elements in the permutation and must ultimately identify a pair of indices i and j such that p_i ⊕ p_j is maximized.
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
        
    #State: the indices \( k \) and \( \text{best} \) that maximize the bitwise XOR for each test case.
#Overall this is what the function does:The function reads multiple test cases, each with an integer \( n \) and a permutation of integers from 0 to \( n-1 \). It interactively queries up to 3n times to compare bitwise OR results of pairs of elements in the permutation. The goal is to identify and return a pair of indices \( i \) and \( j \) such that the bitwise XOR of the elements at these indices (\( p_i \oplus p_j \)) is maximized.

