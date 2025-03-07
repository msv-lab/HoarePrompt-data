#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (1 ≤ a_i ≤ n) where each integer from 1 to n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times (`pairs`) and half of the total number of integers in `a` (`n // 2`).
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer from 1 to `n` appears at most 2 times. It returns the minimum value between the number of integers in `a` that appear exactly 2 times and half of the total number of integers in `a`.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input from `stdin`, processes multiple test cases, and calls `func_1` with the appropriate parameters for each test case.
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
        
    #State: The variable `t` remains the same as its initial value. The variable `idx` is now `1 + t + sum(n for n in map(int, data[1:1+t]))`, where `t` is the number of test cases and each `n` represents the number of elements in each test case. The variable `results` is a list containing the results of `func_1(n, a)` for each test case, where `n` is the number of elements in the test case and `a` is the list of those elements. No other variables are affected.
    for result in results:
        print(result)
        
    #State: Output State: The variable `t` remains the same as its initial value. The variable `idx` is now `1 + t + sum(n for n in map(int, data[1:1+t]))`, where `t` is the number of test cases and each `n` represents the number of elements in each test case. The variable `results` is a list containing the results of `func_1(n, a)` for each test case, where `n` is the number of elements in the test case and `a` is the list of those elements. The loop has printed each element in the `results` list, but the `results` list itself remains unchanged. No other variables are affected.
#Overall this is what the function does:The function `func_2` reads input from `stdin`, processes multiple test cases, and calls `func_1` with the appropriate parameters for each test case. It does not return any value. After the function concludes, the variable `t` (number of test cases) remains unchanged, the variable `idx` is updated to `1 + t + sum(n for n in map(int, data[1:1+t]))`, and the variable `results` is a list containing the results of `func_1(n, a)` for each test case, where `n` is the number of elements in the test case and `a` is the list of those elements. Each element in the `results` list is printed to the standard output, but the `results` list itself remains unchanged. No other variables are affected.

