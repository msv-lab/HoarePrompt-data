#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case provides a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p. It is guaranteed that the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The loop has completed all its iterations. `i` is `n-1`. `n` remains unchanged. `p` is a list of `n` integers where `p[0]` is `n`, `p[1]` is 1, `p[2]` is `n-2`, `p[3]` is 3, `p[4]` is `n-4`, `p[5]` is 5, and so on, with `p[j]` being `j + 1` for all odd indices `j` from 1 to `n - 1`, and `p[k]` being `n - k` for all even indices `k` from 0 to `n - 2`. `ind` is `n`.
#Overall this is what the function does:The function `func` processes multiple test cases, each providing an integer `n` (3 ≤ n ≤ 10^5) representing the length of a permutation `p`. For each test case, it generates a permutation `p` of length `n` such that the elements at even indices are in descending order starting from `n` and decrementing by 2, and the elements at odd indices are in ascending order starting from 1 and incrementing by 2. The function prints the permutation `p` for each test case. After processing all test cases, the function has printed the permutations and the input variables `n` and `p` are no longer relevant.

