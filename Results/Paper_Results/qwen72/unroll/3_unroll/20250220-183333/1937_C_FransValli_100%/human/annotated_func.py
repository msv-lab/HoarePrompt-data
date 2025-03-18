#State of the program right berfore the function call: The function operates in an interactive environment with multiple test cases. Each test case involves a permutation p of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. The function can query the comparison of bitwise OR results of four chosen indices (a, b, c, d) within the permutation, and must find a pair of indices (i, j) such that p_i ⊕ p_j is maximized, using at most 3n queries. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop will output the indices (maxi, mini) for each test case, where maxi and mini are the indices in the permutation p such that p_maxi ⊕ p_mini is maximized. The variables n, maxi, arr, and mini will be updated for each test case, but their final values will be specific to the last test case processed.
#Overall this is what the function does:The function operates in an interactive environment to process multiple test cases. For each test case, it takes a permutation `p` of integers from 0 to n-1, where 2 ≤ n ≤ 10^4, and finds a pair of indices (maxi, mini) such that the bitwise XOR of `p[maxi]` and `p[mini]` is maximized. It uses at most 3n queries to achieve this. After processing all test cases, the function outputs the indices (maxi, mini) for each test case where `p[maxi] ⊕ p[mini]` is maximized. The variables `n`, `maxi`, `arr`, and `mini` are updated for each test case, but their final values will be specific to the last test case processed.

