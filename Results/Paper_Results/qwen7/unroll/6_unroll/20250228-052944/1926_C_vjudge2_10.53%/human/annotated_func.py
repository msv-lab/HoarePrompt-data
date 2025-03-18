#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: Output State: `t` integers are read from the input and appended to the `numbers` list, resulting in a list of `t` integers where `1 ≤ t ≤ 10^4`.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: Output State: `total` is 45, `numbers` is a list of `t` integers (unchanged), `values` is a list of 10 integers `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, `sum_values` is a list of 10 integers `[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]`.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: Output State: `total` is 45, `numbers` is a list of `t` integers (unchanged), `values` is a list of 10 integers `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 45]`, `sum_values` is a list of 11 integers `[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 90]`.
    #
    #Explanation: The loop iterates from 10 to `n` (assuming `n` is at least 10 for the loop to run). For each iteration, it calculates `values[i]` based on the last digit and the remaining part of the number, then updates `sum_values[i]` by adding `values[i]` to the previous sum up to `i-1`. Given the initial conditions, the loop will extend the lists `values` and `sum_values` to include the new calculated values for indices 10 to `n`. Since no specific `n` was provided beyond 10, we assume the loop runs until `n` is just above 10, thus extending the lists to index 10. The final value in `values` is 45, and the final value in `sum_values` is the sum of all previous values plus 45, which is 90.
    for n in numbers:
        print(sum_values[n])
        
    #State: Output State: `total` is 45, `numbers` is a list of `t` integers (unchanged), `values` is a list of 11 integers `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 45]`, `sum_values` is a list of 11 integers `[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 90]`.
    #
    #Explanation: The loop iterates over each element in the `numbers` list. However, since the loop body does not modify any of the given variables (`total`, `numbers`, `values`, or `sum_values`), these variables remain unchanged. The loop simply prints the `sum_values` at the index of each element in `numbers`. Given the initial conditions, the lists `values` and `sum_values` are extended to include the new calculated values for indices 10 to 10 (since only one iteration is expected if `numbers` contains only one element). Therefore, the final values in both lists remain as specified in the initial state.
#Overall this is what the function does:The function reads an integer `t` and `t` integers `n` from the input, then processes these integers to update two lists, `values` and `sum_values`. After processing, it prints the value of `sum_values` at the index of each integer in the `numbers` list. The function does not return any value but modifies the `values` and `sum_values` lists based on the input integers.

