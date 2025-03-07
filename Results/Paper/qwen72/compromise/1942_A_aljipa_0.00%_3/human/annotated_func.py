#State of the program right berfore the function call: The function should take two parameters, n and k, where n is the length of the array and k is the number of sorted cyclic shifts required. Both n and k are integers such that 1 ≤ k ≤ n ≤ 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The loop will execute `t` times, and for each iteration, it will read `n` and `k` from the input. If `k` equals `n`, it will print an array of `n` ones. If `k` equals 1, it will print the range of numbers from 0 to `n-1`. Otherwise, it will print `-1`. The variables `n`, `k`, and `t` will retain their final values after the loop completes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the length of an array and `k` is a parameter. If `k` equals `n`, it prints an array of `n` ones. If `k` equals 1, it prints the range of numbers from 0 to `n-1`. If `k` is neither `n` nor 1, it prints `-1`. The function does not return any value; it only prints the results to the console. After the function concludes, the variables `t`, `n`, and `k` retain their final values.

