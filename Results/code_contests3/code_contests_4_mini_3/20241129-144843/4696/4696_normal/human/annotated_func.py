#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 50, and m is a positive integer such that 1 ≤ m ≤ cntn, where cntn is the number of permutations of length n with maximum possible value of f(p).
def func():
    a, b = raw_input().split()
    n = int(a)
    i = int(b)
    i = i - 1
    p = range(1, n + 1)
    for k in range(1, n + 1):
        f = factorial(n - k)
        
        d = i // f
        
        print(p[d]),
        
        p.remove(p[d])
        
        i = i % f
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is `n`, `p` is an empty list, `i` is the final value after all updates.
#Overall this is what the function does:The function reads two positive integers, n and m, from input. It generates the m-th permutation of the numbers from 1 to n, where 1 ≤ n ≤ 50. The function does not validate the input values or handle cases where m exceeds the total number of permutations, which is n!. If m is greater than n!, the output may not correspond to any valid permutation, leading to an IndexError when attempting to access an out-of-bounds index in the list.

