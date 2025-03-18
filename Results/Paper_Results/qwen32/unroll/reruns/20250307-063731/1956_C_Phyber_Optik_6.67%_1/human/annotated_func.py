#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each test case consists of a single integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a. It is guaranteed that the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: For each test case with size `n`, the output consists of the sum calculated based on the described conditions, followed by `n + r` lines where each line either starts with `1` or `2` and is followed by the numbers from `1` to `n`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an n × n matrix. For each test case, it calculates a sum based on specific conditions and prints this sum followed by `n + r` lines. Each line either starts with `1` or `2` and is followed by the numbers from `1` to `n`.

