#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: Output State: `t` integers are read from input and added to the list `numbers`. The list `numbers` contains these `t` integers.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: Output State: `total` is 45, `numbers` is unchanged, `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45].
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: Output State: `total` is 45, `numbers` is unchanged, `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46], `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 46, 48, 51, 55, 60, 66, 73, 80, 88, 97].
    for n in numbers:
        print(sum_values[n])
        
    #State: Output State: `total` is 45, `numbers` is unchanged, `values` is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46], `sum_values` is [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 46, 48, 51, 55, 60, 66, 73, 80, 88, 97].
    #
    #Explanation: The loop iterates over each element in the `numbers` list and prints the corresponding value from the `sum_values` list. Since `numbers` remains unchanged and the loop does not modify any of the other variables (`total`, `values`, or `sum_values`), their states remain the same after the loop execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( t \) and \( n \). For each test case, it reads \( t \) integers from input and stores them in a list named `numbers`. It then initializes two lists, `values` and `sum_values`, and populates them with specific values. Finally, it iterates over the `numbers` list and prints the corresponding values from the `sum_values` list. The function does not return any value but modifies and uses the `sum_values` list to store cumulative sums based on certain rules.

