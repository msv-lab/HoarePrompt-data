#State of the program right berfore the function call: Each test case contains a single integer n (3 ≤ n ≤ 10^5) representing the length of the permutation p. The function will be called multiple times with different values of n, and the sum of all n values across the test cases does not exceed 10^5.
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
        
    #State: a permutation of numbers from 1 to n where even indices are filled in descending order starting from n and odd indices are filled in ascending order starting from 1 or 2 depending on the parity of n.
#Overall this is what the function does:The function reads multiple integers `n` from the input, each representing the length of a permutation `p`. For each `n`, it constructs a permutation `p` of numbers from 1 to `n` where even indices are filled in descending order starting from `n` and odd indices are filled in ascending order starting from 1 or 2 depending on the parity of `n`. The function then prints each constructed permutation.

