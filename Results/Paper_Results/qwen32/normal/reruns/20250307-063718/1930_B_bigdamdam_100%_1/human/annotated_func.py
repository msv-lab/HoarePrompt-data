#State of the program right berfore the function call: The function receives no direct input arguments. Instead, it should read from standard input where the first line contains a single integer t (1 ≤ t ≤ 10^3) representing the number of test cases. Each of the following t lines contains a single integer n (3 ≤ n ≤ 10^5) representing the length of the permutation p for each test case. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop has executed `t` times, and for each test case, a permutation `p` of length `n` is constructed and printed. The elements at even indices of `p` are `n, n-2, n-4, ..., n-2*floor(n/2)`, and the elements at odd indices are `1 + n % 2, 3 + n % 2, 5 + n % 2, ..., 1 + n % 2 + 2 * ((n-1)//2)` if `n` is odd, or `2, 4, 6, ..., 2*((n-1)//2)` if `n` is even. The variables `ind` and `i` are loop variables and do not retain specific values after the loop completes each test case.
#Overall this is what the function does:The function reads from standard input, where the first line contains an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and constructs a permutation `p` of length `n`. The permutation `p` is such that elements at even indices are filled in descending order starting from `n`, and elements at odd indices are filled in ascending order starting from `1 + n % 2`. The function then prints the constructed permutation for each test case.

