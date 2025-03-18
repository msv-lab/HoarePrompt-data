#State of the program right berfore the function call: The function should be called within a loop that iterates over a list of test cases, where each test case is a list containing an integer n (2 ≤ n ≤ 50) and a list of integers p_1, p_2, ..., p_n (1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct).
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: The loop does not modify the values of `n` or `v`. The loop will either print `2` and return if the condition `v[v[i]] == i` is met for any `i` in the range `1` to `n`, or it will complete all iterations without printing anything if the condition is never met.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `v` from the input. It checks if for any index `i` in the range from 1 to `n`, the value `v[v[i]]` equals `i`. If such an index is found, the function prints `2` and returns immediately. If no such index is found after checking all values, the function prints `3` and returns. The function does not modify the values of `n` or `v` and does not return any value.

