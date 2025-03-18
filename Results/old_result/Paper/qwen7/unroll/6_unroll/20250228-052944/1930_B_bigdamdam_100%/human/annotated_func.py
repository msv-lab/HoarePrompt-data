#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
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
        
    #State: Output State: For each test case, the output is a list `p` of length `n`, where elements at even indices are filled with values starting from `n` and decrementing by 2, and elements at odd indices are filled with values starting from 1 plus the remainder when `n` is divided by 2 and incrementing by 2.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n (3 ≤ n ≤ 10^5). For each n, it generates a list p of length n. Elements at even indices in p are filled with values starting from n and decrementing by 2, while elements at odd indices are filled with values starting from 1 plus the remainder when n is divided by 2 and incrementing by 2. The function prints the generated list p for each test case.

