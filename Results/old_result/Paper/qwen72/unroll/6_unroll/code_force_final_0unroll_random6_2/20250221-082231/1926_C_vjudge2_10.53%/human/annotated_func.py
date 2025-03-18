#State of the program right berfore the function call: The function should accept an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: `t` is an input integer between 1 and 10^4, `n` is an integer between 1 and 2 · 10^5 for the last test case, `numbers` is a list containing `t` integers, each between 1 and 2 · 10^5.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: `t` remains an input integer between 1 and 10^4, `n` remains an integer between 1 and 2 · 10^5 for the last test case, `numbers` remains a list containing `t` integers, each between 1 and 2 · 10^5, `values` is a list where the first 10 elements are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], `sum_values` is a list where the first 10 elements are [0, 1, 3, 6, 10, 15, 21, 28, 36, 45], and `total` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: `t` remains an input integer between 1 and 10^4, `n` remains an integer between 1 and 2 · 10^5 for the last test case, `numbers` remains a list containing `t` integers, each between 1 and 2 · 10^5, `values` is a list where the first 10 elements are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and the subsequent elements up to index `n` are calculated based on the loop logic, `sum_values` is a list where the first 10 elements are [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] and the subsequent elements up to index `n` are calculated based on the loop logic, and `total` is 45.
    for n in numbers:
        print(sum_values[n])
        
    #State: The values of `t`, `numbers`, `values`, and `total` remain unchanged. The `sum_values` list is accessed and printed for each element in `numbers`, but the list itself is not modified.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads another integer `n` from the input, representing the largest number Vladislav writes. It then calculates the cumulative sum of a sequence of values based on the digits of the numbers from 1 to `n`. The function prints the cumulative sum for each `n` in the test cases. The function does not return any value; it only prints the results. After the function concludes, `t` remains an integer between 1 and 10^4, `numbers` is a list of `t` integers each between 1 and 2 · 10^5, and `sum_values` is a list containing the cumulative sums up to the largest `n` in the test cases.

