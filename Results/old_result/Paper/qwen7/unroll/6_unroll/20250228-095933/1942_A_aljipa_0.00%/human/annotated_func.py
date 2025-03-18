#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3 and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: A series of lines, each containing either 1 repeated n times, or -1, or a sequence of numbers from 0 to n-1 based on the values of n and k provided in each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it generates and prints a list based on the values of `n` and `k`. If `k` equals `n`, it prints a list with `n` ones. If `k` equals 1, it prints a list with numbers from 0 to `n-1`. Otherwise, it prints a list with `-1`.

