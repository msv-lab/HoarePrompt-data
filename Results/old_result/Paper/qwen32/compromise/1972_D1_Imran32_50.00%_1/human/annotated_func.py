#State of the program right berfore the function call: The function `func_1` does not take any direct input arguments. Instead, it is expected to read input from standard input. The input consists of multiple test cases. The first line contains a single integer `t` (1 ≤ t ≤ 10^4), which is the number of test cases. Each of the next `t` lines contains two integers `n` and `m` (1 ≤ n, m ≤ 2 · 10^6). It is guaranteed that the sum of `n` and the sum of `m` over all test cases does not exceed 2 · 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: ans for each test case
    print(ans)
    #This is printed: ans (where ans is the value to be printed for each test case)
#Overall this is what the function does:The function `func_1` reads multiple test cases from standard input, where each test case consists of an integer `n`. For each test case, it calculates a specific value `ans` based on the input `n` and prints this value. The calculation involves iterating up to the square root of `n` and adjusting `ans` by adding the integer division of `n + i` by `i * i` for each `i` from 2 up to the square root of `n`.

