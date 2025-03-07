#State of the program right berfore the function call: The function should accept two parameters, n and k, where n is the length of the array and k is the number of sorted cyclic shifts required. Both n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The function should handle up to 10^3 test cases.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The loop will execute `t` times, and for each iteration, it will read a pair of integers `n` and `k` from the input. If `k` equals `n`, it will print an array of `n` ones. If `k` equals 1, it will print the range of numbers from 0 to `n-1`. Otherwise, it will print `-1`. After all iterations, the values of `t`, `n`, and `k` will be unchanged, but the output will be the result of the print statements for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the length of an array and `k` is a parameter. If `k` equals `n`, it prints an array of `n` ones. If `k` equals 1, it prints the range of numbers from 0 to `n-1`. Otherwise, it prints `-1`. The function does not return any value; it only prints the results for each test case. After the function concludes, the values of `t`, `n`, and `k` remain unchanged, but the output will be the printed results for each test case.

