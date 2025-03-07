#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n and k are integers for each test case where 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The loop has finished executing for all test cases, and the variables t, n, and k remain unchanged as they are input variables. The output for each test case is determined by the conditions within the loop: if k is 1, the output is 1; if k is less than or equal to 2 * (n + (n - 2)), the output is the ceiling of k divided by 2; otherwise, the output is k divided by 2 (integer division) plus 1.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integer parameters `n` and `k`, where `2 <= n <= 10^8` and `1 <= k <= 4n - 2`. The function is called `t` times, where `1 <= t <= 1000`. For each test case, the function prints a result based on the values of `n` and `k`: if `k` is 1, it prints 1; if `k` is less than or equal to `2 * (n + (n - 2))`, it prints the ceiling of `k / 2`; otherwise, it prints `k // 2 + 1`. After processing all test cases, the function completes, and the input variables `t`, `n`, and `k` remain unchanged.

