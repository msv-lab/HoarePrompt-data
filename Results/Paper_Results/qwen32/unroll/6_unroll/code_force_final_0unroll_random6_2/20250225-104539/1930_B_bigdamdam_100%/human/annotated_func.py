#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10³) — the number of test cases. Each of the following t lines contains a single integer n (3 ≤ n ≤ 10⁵) — the length of the permutation p. The sum of n over all test cases does not exceed 10⁵.
def func():
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: For each test case with input n, the output is a permutation p of length n where even indices are filled with decreasing values starting from n and odd indices are filled with increasing values starting from 1 + n % 2.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the length of a permutation. For each test case, it generates a permutation `p` of length `n` such that even indices are filled with decreasing values starting from `n`, and odd indices are filled with increasing values starting from `1 + n % 2`. The function outputs this permutation for each test case.

