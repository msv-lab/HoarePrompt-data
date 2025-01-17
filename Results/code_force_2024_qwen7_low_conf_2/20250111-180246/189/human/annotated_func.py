#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^3.
def func_1(n):
    points = []
    for i in range(n):
        x = i + 1
        
        y = i * 2 % n + 1
        
        points.append((x, y))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^3\); `points` contains tuples of the form ((i + 1, i * 2 % n + 1) for each iteration of the loop where \(0 \leq i < n\)); `i` is `n - 1` after the loop finishes.
    return points
    #`The program returns a list of tuples, where each tuple is of the form (i+1, i*2 % n + 1) for 0 <= i < n, and i is n-1 after the loop finishes`
#Overall this is what the function does:The function `func_1` accepts an integer `n` such that \(2 \leq n \leq 10^3\) and returns a list of tuples. Each tuple in the list is of the form \((i+1, i*2 \% n + 1)\) for \(0 \leq i < n\). After the loop finishes, the variable `i` will be equal to \(n-1\). There are no edge cases mentioned that would change this behavior, and the code correctly implements the described functionality.

#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func_2():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(t):
        n = int(data[i + 1])
        
        result = func_1(n)
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer within the range 1 to \(10^3\), `n` is an integer between 2 and \(10^3\) (inclusive), `data` is a list of strings obtained by splitting the input from `sys.stdin`, `results` is a list containing the return values of `func_1(n)` for each iteration, `result` is the return value of `func_1(n)` for the last iteration, `i` is `t - 1`
    for result in results:
        for x, y in result:
            print(x, y)
        
    #State of the program after the  for loop has been executed: `i` is the length of `results`, `results` is a list of pairs `(x, y)` where each pair is the return value of `func_1(n)` for each iteration, `result` is the last element in `results`, and the print statements will have printed each pair `(x, y)` in `results` exactly once.
#Overall this is what the function does:The function processes multiple test cases internally, where for each test case, it reads an integer `n` (2 ≤ n ≤ 10^3) and a positive integer `t` (1 ≤ t ≤ 50) from standard input. It then calls `func_1(n)` for each test case and collects the results in a list. Finally, it prints each pair `(x, y)` returned by `func_1(n)` for every test case. The function does not accept any parameters directly and does not have a specific return value. However, it ensures that the input `t` is within the range 1 to 50 and `n` is within the range 2 to 10^3. If `t` exceeds 50 or `n` is outside the specified range, the function will not handle these cases explicitly, but the behavior of `func_1(n)` may vary.

