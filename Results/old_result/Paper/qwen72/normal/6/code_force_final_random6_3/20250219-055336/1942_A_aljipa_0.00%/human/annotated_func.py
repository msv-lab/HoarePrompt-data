#State of the program right berfore the function call: The function should take two parameters, n and k, where n is the length of the array and k is the number of sorted cyclic shifts required, such that 1 ≤ k ≤ n ≤ 10^3. The function should return a list of n integers, each between 1 and 10^9, that satisfies the given conditions, or -1 if no such array exists.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: `n` and `k` are input integers, `t` equals the number of times the loop was executed, `res` is a list of `n` ones if `k == n`, a range from 0 to `n-1` if `k == 1`, otherwise `res` is a list containing `-1`.
#Overall this is what the function does:The function reads an integer `t` from the input, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the length of the array and `k` is the number of sorted cyclic shifts required. The function then prints a list of `n` integers: a list of `n` ones if `k == n`, a range from 0 to `n-1` if `k == 1`, or a list containing `-1` if neither condition is met. The function does not return any value.

