#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t lines contains two integers n and k such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state is a sequence of integers printed for each test case based on the conditions provided in the loop. Specifically, for each test case with integers `n` and `k`, the output is `1` if `k == 1`, `ceil(k / 2)` if `k <= 2 * n`, and `k // 2 + 1` if `k > 2 * n`. This sequence is printed after all `t` test cases have been processed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it calculates and prints a specific integer based on the values of `n` and `k`. The printed value is `1` if `k` is `1`, `ceil(k / 2)` if `k` is less than or equal to `2 * n`, and `k // 2 + 1` if `k` is greater than `2 * n`.

