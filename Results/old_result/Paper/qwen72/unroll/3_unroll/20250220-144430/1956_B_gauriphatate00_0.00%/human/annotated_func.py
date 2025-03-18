#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= n. Each integer from 1 to n appears in the list a at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times (`pairs`) and half of the total number of integers in `a` (`n // 2`).
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer in `a` is between 1 and `n` and appears at most 2 times. It returns the minimum value between the number of integers in `a` that appear exactly 2 times and half of the total number of integers in `a` (`n // 2`). The function does not modify the input list `a` or the integer `n`.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= n.
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
        
    #State: Output State: `t` is the integer value of `data[0]`, `n` is the last value of `n` processed in the loop, `a` is the last list of integers processed in the loop, `data` is the same list of strings as in the initial state, `idx` is the index after the last processed element in `data`, `results` is a list containing the results of `func_1(n, a)` for each iteration of the loop.
    for result in results:
        print(result)
        
    #State: `t` is the integer value of `data[0]`, `n` is the last value of `n` processed in the loop, `a` is the last list of integers processed in the loop, `data` is the same list of strings as in the initial state, `idx` is the index after the last processed element in `data`, `results` is a list containing the results of `func_1(n, a)` for each iteration of the loop.
#Overall this is what the function does:The function reads input from `sys.stdin`, processes it to handle `t` test cases, where each test case consists of an integer `n` and a list of `n` integers `a`. For each test case, it calls `func_1(n, a)` and appends the result to a list `results`. After processing all test cases, it prints each result in `results`. The function does not return any value. The final state of the program includes `t` being the integer value of `data[0]`, `n` being the last value of `n` processed, `a` being the last list of integers processed, `data` remaining the same list of strings as in the initial state, `idx` being the index after the last processed element in `data`, and `results` containing the results of `func_1(n, a)` for each test case.

