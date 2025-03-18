#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. Each integer from 1 to n appears at most 2 times in the list a.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times (`pairs`) and half of `n` (`n // 2`).
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer in `a` is between 1 and `n` and appears at most twice. It returns the minimum value between the number of integers in `a` that appear exactly twice and half of `n`. After the function concludes, the input parameters `n` and `a` remain unchanged, and the function does not modify any external state.

#State of the program right berfore the function call: No variables are passed in the function signature, but the function reads input from stdin. The input is expected to be formatted as described in the problem statement, with the first line containing the number of test cases t (1 ≤ t ≤ 10^4), followed by t test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards in your hand, followed by a list of n integers a (1 ≤ a_i ≤ n) representing the integers on the cards in your hand.
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
        
    #State: `input` is now a reference to `sys.stdin.read`, `data` is a list of strings split from the input read from `sys.stdin`, `idx` is `1 + (t * (n + 1))`, `t` is 0, `results` is a list containing `t` elements, each element being the result of `func_1(n, a)` for each iteration, where `n` and `a` are updated according to the input data for each iteration.
    for result in results:
        print(result)
        
    #State: `input` is now a reference to `sys.stdin.read`, `data` is a list of strings split from the input read from `sys.stdin`, `idx` is `1 + (t * (n + 1))`, `t` is 0, `results` is a list containing all the elements, each element being the result of `func_1(n, a)` for each iteration, where `n` and `a` are updated according to the input data for each iteration.
#Overall this is what the function does:The function `func_2` reads input from `stdin` and processes multiple test cases. Each test case includes an integer `n` and a list of `n` integers `a`. The function calls `func_1` for each test case, passing `n` and `a` as arguments, and collects the results. After processing all test cases, it prints each result to `stdout`. The function does not return any value. After the function concludes, `input` is a reference to `sys.stdin.read`, `data` is a list of strings split from the input read from `stdin`, `idx` is `1 + (t * (n + 1))`, `t` is 0, and `results` is a list containing the results of `func_1` for each test case.

