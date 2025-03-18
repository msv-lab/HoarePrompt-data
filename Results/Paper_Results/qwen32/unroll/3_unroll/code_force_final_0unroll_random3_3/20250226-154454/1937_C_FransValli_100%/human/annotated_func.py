#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p of the set {0, 1, ..., n-1}. The function can interactively query up to 3n times per test case by providing indices a, b, c, and d (0 ≤ a, b, c, d < n) to receive a comparison result of (p_a | p_b) versus (p_c | p_d). The goal is to determine any two indices i and j such that p_i ⊕ p_j is maximized among all pairs (0 ≤ i, j < n). The sum of n across all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        maxi = 0
        
        for i in range(1, n):
            print('?', maxi, maxi, i, i, flush=True)
            res = input()
            if res == '<':
                maxi = i
        
        arr = [0]
        
        for i in range(1, n):
            print('?', maxi, arr[0], maxi, i, flush=True)
            res = input()
            if res == '<':
                arr = [i]
            elif res == '=':
                arr.append(i)
        
        mini = arr[0]
        
        for item in arr[1:]:
            print('?', mini, mini, item, item, flush=True)
            res = input()
            if res == '>':
                mini = item
        
        print('!', maxi, mini, flush=True)
        
    #State: the indices `maxi` and `mini` are printed such that `p_maxi ⊕ p_mini` is maximized.
#Overall this is what the function does:The function determines and prints two indices `i` and `j` for each test case such that the bitwise XOR of `p_i` and `p_j` is maximized among all pairs `(0 ≤ i, j < n)` for a given permutation `p` of the set `{0, 1, ..., n-1}`. It achieves this by interactively querying up to `3n` times per test case, comparing specific pairs of indices based on bitwise OR operations.

