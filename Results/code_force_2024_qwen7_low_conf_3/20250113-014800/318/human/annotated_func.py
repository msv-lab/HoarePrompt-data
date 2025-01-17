#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5, and the sum of all n across all test cases does not exceed 10^5. Each n represents the length of the permutation p, which must be a sequence of n distinct integers from 1 to n such that no two distinct indices i and j satisfy the conditions p_i divides p_j and p_{i+1} divides p_{j+1}.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        mid = n // 2
        
        a = []
        
        for i in range(1, n // 2 + 1):
            a.append(i)
            a.append(mid + i)
        
        if n % 2 != 0:
            a.append(n)
        
        for i in range(n):
            print(a[i], end=' ')
        
        print('\n', end='')
        
    #State of the program after the  for loop has been executed: 
#Overall this is what the function does:The function processes a series of test cases where each test case includes an integer `t` (1 ≤ t ≤ 10^3) indicating the number of test cases, followed by `t` integers `n` (3 ≤ n ≤ 10^5) representing the lengths of permutations `p`. For each test case, it generates a specific permutation `p` of length `n` and prints it. The generated permutation is constructed such that the first half consists of numbers from 1 to `n/2`, and the second half consists of numbers from `n/2 + 1` to `n`. If `n` is odd, the largest number `n` is appended to the permutation. The function ensures that no two distinct indices `i` and `j` satisfy `p_i` divides `p_j` and `p_{i+1}` divides `p_{j+1}` within the generated permutation. However, the function does not check the divisibility condition within the generated permutation; it only constructs the permutation according to the specified pattern.

