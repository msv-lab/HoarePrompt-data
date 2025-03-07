#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: `t` is an integer representing the number of test cases, where `t` is 0; `numbers` is a list containing `t` input integers, each representing the number provided in each iteration of the loop.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: `t` is 0; `numbers` is a list containing `t` input integers; `values` is a list with the first 10 elements set to 0 through 9; `sum_values` is a list of length `max(numbers) + 1` with the first 10 elements set to 0, 1, 3, 6, 10, 15, 21, 28, 36, 45; `total` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: - `t` is 0
    #- `numbers` is a list containing `t` input integers
    #- `values` is a list with the first 10 elements set to 0 through 9, and additional elements calculated as described
    #- `sum_values` is a list of length `max(numbers) + 1` with the first 10 elements set to 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, and additional elements calculated as described
    #- `total` is 45
    #
    #Specifically for `n = 20`:
    #- `values` will be `[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 3]`
    #- `sum_values` will be `[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 46, 48, 52, 59, 70, 86, 108, 137, 174, 220, 223]`
    #
    #Output State:
    for n in numbers:
        print(sum_values[n])
        
    #State: `t` is 0, `numbers` is `[20, 21, 22]`, `values` is a list with the first 10 elements set to 0 through 9 and additional elements calculated as described, `sum_values` is a list of length `max(numbers) + 1` with the first 10 elements set to 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, and additional elements calculated as described, `total` is 45
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the cumulative sum of a specific sequence value up to `n`.

