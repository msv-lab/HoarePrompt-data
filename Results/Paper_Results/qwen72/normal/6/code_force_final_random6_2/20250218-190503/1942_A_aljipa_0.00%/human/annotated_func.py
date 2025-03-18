#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the length of the array a, and k is an integer representing the number of sorted cyclic shifts the array a must have, such that 1 ≤ k ≤ n ≤ 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: `t` is 0, `n` is the last input integer, `k` is the last input integer, `res` is a list of `n` ones if `k` equals `n`, `res` is a list containing numbers from 0 to `n-1` if `k` equals 1, otherwise `res` is a list containing `-1`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the length of an array and `k` is a parameter related to sorting cyclic shifts. The function then prints a list `res` based on the values of `n` and `k`: if `k` equals `n`, it prints a list of `n` ones; if `k` equals 1, it prints a list of integers from 0 to `n-1`; otherwise, it prints a list containing `-1`. After processing all test cases, the function concludes with `t` being 0, and `n`, `k`, and `res` holding the values of the last test case.

