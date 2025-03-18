#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (1 ≤ a_i ≤ n) where each integer from 1 to n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times (`pairs`) and half the total number of integers in `a` (`n // 2`).
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer from 1 to `n` appears at most 2 times. It returns the minimum value between the number of integers in `a` that appear exactly 2 times and half the total number of integers in `a` (`n // 2`). The function does not modify the input parameters.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input from `sys.stdin` and processes multiple test cases.
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
        
    #State: `func_2` reads input from `sys.stdin` and splits it into a list of strings, which is assigned to the variable `data`. `idx` is assigned the value `1 + t * (1 + n)`, where `n` is the sum of the values of `n` for each iteration. `t` is assigned the integer value of `data[0]` and must be greater than or equal to the number of iterations. `results` is a list containing the results of `func_1(n, a)` for each iteration. `a` is a list of `n` integers for the last iteration, starting from the element at index `idx - n - 1` in `data`.
    for result in results:
        print(result)
        
    #State: `results` is a list containing all the results from `func_1(n, a)` for each iteration, and the loop has printed each result in the list.
#Overall this is what the function does:The function `func_2` reads input from `sys.stdin`, processes multiple test cases, and prints the results of each test case. Each test case involves reading an integer `n` followed by `n` integers, and the function calls another function `func_1` with these values. The final state of the program after `func_2` concludes is that all results from `func_1` for each test case have been printed to the standard output.

