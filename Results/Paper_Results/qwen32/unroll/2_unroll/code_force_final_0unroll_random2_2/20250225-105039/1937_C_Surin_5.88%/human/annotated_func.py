#State of the program right berfore the function call: There are multiple test cases, each containing an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. For each test case, you can ask up to 3n queries in the form "? a b c d" to compare the bitwise OR of pairs (p_a, p_b) and (p_c, p_d). The interactor will respond with "<", "=", or ">" based on the comparison. After finding a pair of indices i and j such that p_i ⊕ p_j is maximized, you must print "! i j". The total number of queries across all test cases must not exceed 3 times the sum of all n values, which is at most 3 * 10^4.
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
        
    #State: the indices `prev` and `v1` that maximize the XOR value for the current test case.
#Overall this is what the function does:The function interacts with an interactor to determine a permutation of integers from 0 to n-1 for multiple test cases. For each test case, it asks up to 3n queries to compare the bitwise OR of pairs of elements. Based on these comparisons, it identifies a pair of indices (i, j) that maximizes the bitwise XOR of the elements at these indices and prints "! i j".

