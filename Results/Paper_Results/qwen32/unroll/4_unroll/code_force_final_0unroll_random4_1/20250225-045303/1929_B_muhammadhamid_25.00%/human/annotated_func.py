#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
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
        
    #State: A series of printed results, one for each test case, based on the given logic.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k`. For each test case, it calculates and prints a specific value based on the relationship between `n` and `k`. If `k` is 1, it prints 1. If `k` is less than or equal to `2 * n`, it prints the ceiling of `k / 2`. Otherwise, it prints `k // 2 + 1`.

