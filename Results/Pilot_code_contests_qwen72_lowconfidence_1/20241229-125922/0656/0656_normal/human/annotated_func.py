#State of the program right berfore the function call: x and y are non-negative integers.
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` is the greatest common divisor (GCD) of the original values of `x` and `y`, `y` is 0
    return x
    #The program returns the greatest common divisor (GCD) of the original values of `x` and `y`
#Overall this is what the function does:The function `func_1` accepts two non-negative integer parameters `x` and `y`. It computes and returns the greatest common divisor (GCD) of the original values of `x` and `y`. After the function concludes, `x` holds the GCD of the original `x` and `y`, and `y` is 0. The function correctly handles the edge case where either or both `x` and `y` are zero, returning the non-zero value as the GCD, or 0 if both are zero.

#State of the program right berfore the function call: n and m are integers such that 2 ≤ n ≤ 100 and 1 ≤ m ≤ 200. a and b are lists of integers where each element a[i] and b[i] satisfies 1 ≤ a[i], b[i] ≤ n and a[i] ≠ b[i].
def func_2():
    n, m = map(int, input().split())
    station = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        
        station[a - 1].append(b - 1)
        
    #State of the program after the  for loop has been executed: To determine the output state after all iterations of the loop have finished, we need to consider the final values of the variables and their relationships based on the loop code. Let's break it down step by step:
    #
    #### Initial State:
    #- `n` and `m` are integers such that 2 ≤ n ≤ 100 and 1 ≤ m ≤ 200.
    #- `a` and `b` are lists of integers where each element `a[i]` and `b[i]` satisfies 1 ≤ a[i], b[i] ≤ n and a[i] ≠ b[i].
    #- `station` is a list of `n` empty lists.
    #
    #### Loop Code:
    #```python
    #for i in range(m):
    #    a, b = map(int, input().split())
    #    station[a - 1].append(b - 1)
    #```
    #
    #### Analysis:
    #1. **Loop Execution**:
    #   - The loop runs `m` times.
    #   - In each iteration, the user inputs two integers `a` and `b` such that 1 ≤ a, b ≤ n and a ≠ b.
    #   - The value `b - 1` is appended to the list at index `a - 1` in `station`.
    #
    #2. **Final State**:
    #   - After `m` iterations, `station` will be a list of `n` lists.
    #   - Each list `station[a - 1]` will contain all the values `b - 1` that were appended during the iterations where `a` was the corresponding index.
    #   - The values of `n` and `m` remain unchanged.
    #   - The values of `a` and `b` are specific integers input by the user in each iteration, and they do not retain any specific final value after the loop (they are overwritten in each iteration).
    #
    #### Output State:
    #- `n` and `m` are integers such that 2 ≤ n ≤ 100 and 1 ≤ m ≤ 200.
    #- `station` is a list of `n` lists.
    #- For each valid pair `(a, b)` input during the loop, the list `station[a - 1]` contains the elements `b - 1` appended in the order they were input.
    #- The loop will execute `m` times, and `i` will be `m - 1` after the last iteration.
    #- `a` and `b` are not defined after the loop as they are re-assigned in each iteration.
    #
    #Therefore, the output state is:
    #**`n` and `m` are integers such that 2 ≤ n ≤ 100 and 1 ≤ m ≤ 200, `station` is a list of `n` lists where each `station[a - 1]` contains the elements `b - 1` appended in the order they were input during the `m` iterations, `i` is `m - 1`.**
    max_candy = [0] * n
    for i in range(n):
        try:
            max_candy[i] = min(station[i], key=lambda x: x + n - i if x < i else x - i)
        except ValueError:
            pass
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that \(2 \leq n \leq 100\) and \(1 \leq m \leq 200\), `station` is a list of `n` lists, `i` is `n - 1`, `max_candy` is a list of `n` elements where each `max_candy[i]` is either the element from `station[i]` that minimizes the key function `lambda x: x + n - i if x < i else x - i`, or `0` if `station[i]` is empty or all elements are filtered out by the key function.
    for i in range(n):
        res = 0
        
        for j in range(i, i + n):
            if len(station[j % n]) == 0:
                continue
            dist = j - i
            j %= n
            dist += (len(station[j]) - 1) * n + (max_candy[j] + n - j if max_candy[
                j] < j else max_candy[j] - j)
            res = max(res, dist)
        
        print(res, end=' ')
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 100\), `m` is an integer such that \(1 \leq m \leq 200\), `station` is a list of `n` lists, `i` has completed all iterations from `0` to `n-1`, `max_candy` is a list of `n` elements where each `max_candy[i]` is either the element from `station[i]` that minimizes the key function `lambda x: x + n - i if x < i else x - i`, or `0` if `station[i]` is empty or all elements are filtered out by the key function, `res` has been calculated and printed `n` times, each time representing the maximum distance for the corresponding `i`, `j` has been used in the inner loop and will have taken on values from `i` to `i + n - 1` modulo `n`.
#Overall this is what the function does:The function `func_2` reads input values for `n` and `m`, where `n` is an integer such that \(2 \leq n \leq 100\) and `m` is an integer such that \(1 \leq m \leq 200\). It then reads `m` pairs of integers `(a, b)` where each pair satisfies \(1 \leq a, b \leq n\) and \(a \neq b\). The function constructs a list `station` of `n` lists, where each `station[a - 1]` contains the elements `b - 1` appended in the order they were input. After constructing `station`, the function calculates a list `max_candy` of `n` elements, where each `max_candy[i]` is the element from `station[i]` that minimizes the key function `lambda x: x + n - i if x < i else x - i`, or `0` if `station[i]` is empty or all elements are filtered out by the key function. Finally, the function computes and prints `n` values, each representing the maximum distance for the corresponding `i` based on the elements in `station` and `max_candy`. The function does not return any value.

