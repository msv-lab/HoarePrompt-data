#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n, a, and b are positive integers such that 1 <= n, a, b <= 10^9.
def func_1(k, a, b, n):
    ans = 0
    ans += k * b
    ans += (n - k) * a
    return ans <= n * max(a, b)
    #The program returns a boolean value indicating whether ans is less than or equal to n times the maximum of a and b.
#Overall this is what the function does:The function accepts four parameters: k, a, b, and n. It calculates the value of `ans` as `k * b + (n - k) * a`. The function then returns `True` if `ans` is less than or equal to `n * max(a, b)`, otherwise it returns `False`.

