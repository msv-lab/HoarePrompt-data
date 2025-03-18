#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: `t` is the integer value of the input representing the number of test cases; `numbers` is a list containing `t` integers, each read from the input during the loop iterations.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: `t` is the integer value of the input representing the number of test cases; `numbers` is a list containing `t` integers, each read from the input during the loop iterations; `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]; `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]; `total` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: `t` is the integer value of the input representing the number of test cases; `numbers` is a list containing `t` integers, each read from the input during the loop iterations; `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 46, 48, 51, 55, 60, 66, 73, 81, 90, 100]; `total` is 45.
    for n in numbers:
        print(sum_values[n])
        
    #State: t is the integer value of the input representing the number of test cases; numbers is a list containing t integers, each read from the input during the loop iterations; values is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; sum_values is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 46, 48, 51, 55, 60, 66, 73, 81, 90, 100]; total is 45.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and computes a value based on a specific rule, then prints the result for each `n`.

