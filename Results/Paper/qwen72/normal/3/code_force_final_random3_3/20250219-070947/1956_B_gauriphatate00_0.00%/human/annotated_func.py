#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (1 ≤ a_i ≤ n) where each integer from 1 to n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between `pairs` and `n // 2`, where `pairs` is the number of integers in `a` that appear exactly twice, and `n` is a positive integer representing the length of the list `a`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer from 1 to `n` appears at most twice. It returns the minimum value between the number of integers in `a` that appear exactly twice and `n // 2`.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, n is a positive integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 1 <= a_i <= n, with each integer from 1 to n appearing at most twice.
def func_2():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        results.append(func_1(n, a))
        
    #State: `t` is 0, `n` is a positive integer such that 1 <= n <= 2 * 10^5, `a` is a list of `n` integers where each integer is the integer value of the corresponding string in `data[idx:idx + n]`, `data` is a list of strings obtained by splitting the input from `sys.stdin`, `idx` is `1 + t * (1 + n)`, `results` is a list containing the results of `func_1(n, a)` appended `t` times.
    for result in results:
        print(result)
        
    #State: `results` must have at least `t` elements, and each `result` in the loop is the corresponding element in `results` from the first to the `t`-th element.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes it to handle `t` test cases, where each test case consists of a positive integer `n` and a list `a` of `n` integers. For each test case, it calls `func_1` with `n` and `a` as arguments and appends the result to a list `results`. After processing all test cases, it prints each result in `results`. The function does not return any value. After the function concludes, `t` is 0, `results` contains the results of `func_1` for each test case, and `idx` is `1 + t * (1 + n)`.

