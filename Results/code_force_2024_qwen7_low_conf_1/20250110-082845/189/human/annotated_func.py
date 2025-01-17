#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^3.
def func_1(n):
    points = []
    for i in range(n):
        x = i + 1
        
        y = i * 2 % n + 1
        
        points.append((x, y))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= n <= 10^3, `points` is a list containing tuples (x, y) where x ranges from 2 to n+1 and y ranges from 3 to 2n+1, `i` is n, `x` is n+1, `y` is 2*n+1 % n + 1.
    return points
    #`points` is a list containing tuples (x, y) where x ranges from 2 to n+1 and y ranges from 3 to 2n+1
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 2 to 10^3. It initializes an empty list `points` and iterates over a range from 0 to `n-1`. During each iteration, it calculates `x` as `i + 1` and `y` as `(i * 2) % n + 1`, ensuring that `y` is within the specified range. These values are then appended as a tuple `(x, y)` to the `points` list. After completing the loop, the function returns the `points` list, which contains tuples `(x, y)` where `x` ranges from 2 to `n+1` and `y` ranges from 3 to `2n+1`. This process covers all integers `n` in the specified range, including the edge case when `n` is exactly 10^3.

#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each test case, n is an integer such that 2 <= n <= 10^3.
def func_2():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(t):
        n = int(data[i + 1])
        
        result = func_1(n)
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `t` is the integer value of the first element in `data`, `n` is the integer value of `data[t]`, `data` is a list of strings obtained by splitting the input from `sys.stdin.read`, `results` is a list containing `func_1(int(data[1]))`, `func_1(int(data[2]))`, ..., `func_1(int(data[t]))`, `i` is `t-1`, `result` is `func_1(int(data[t]))`
    for result in results:
        for x, y in result:
            print(x, y)
        
    #State of the program after the  for loop has been executed: 
#Overall this is what the function does:The function reads input from standard input, processes a series of test cases, and prints the results. Specifically, it reads an integer `t` representing the number of test cases, followed by `t` integers `n`, each representing the size of the input for the `func_1` function. For each test case, it calls `func_1(n)` and stores the result in a list `results`. Finally, it iterates over the `results` list and prints each pair of values.

