#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 * 10^5, and a is a list of integers of length n where each integer is between 1 and n inclusive.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between `pairs` and `n // 2`.
#Overall this is what the function does:The function `func_1` takes a positive integer `n` and a list of integers `a` of length `n`, where each integer in `a` is between 1 and `n` inclusive. It calculates the number of integers that appear exactly twice in the list and returns the minimum of this count and `n // 2`.

#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
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
        
    #State: `n` is the number of cards from the last test case, `a` is the list of cards from the last test case, `input` is `sys.stdin.read`, `data` is the list of strings obtained by splitting the input line, `idx` is the index after processing all test cases, `t` is the number of test cases, `results` is a list containing the results of `func_1(n, a)` for each test case.
    for result in results:
        print(result)
        
    #State: results list is fully printed, n, a, input, data, idx, t remain unchanged.
#Overall this is what the function does:The function `func_2` reads input from standard input, which includes multiple test cases. Each test case consists of a positive integer `n` and a list `a` of `n` integers where each integer from 1 through `n` appears at most twice. The function processes each test case by calling `func_1` with `n` and `a`, and collects the results. It then prints the result for each test case. The final state of the program includes the printed results for all test cases, while the input variables remain unchanged.

