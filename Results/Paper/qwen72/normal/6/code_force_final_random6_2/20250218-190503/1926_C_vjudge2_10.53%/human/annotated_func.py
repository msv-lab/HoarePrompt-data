#State of the program right berfore the function call: The function should take an integer t and a list of integers n, where 1 <= t <= 10^4 and for each n, 1 <= n <= 2 * 10^5.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: `t` is 0, `numbers` is a list containing `t` input integers, `n` is the last input integer.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: `t` is 0, `numbers` is a list containing `t` input integers, `n` is the last input integer, `values` is a list of zeros with length `max(numbers) + 1` if `numbers` is not empty, otherwise `values` is an empty list, `sum_values` is a list of zeros with length `max(numbers) + 1` if `numbers` is not empty, otherwise `sum_values` is an empty list, `total` is 45, `i` is 9, `values[0]` is 0, `sum_values[0]` is 0, `values[1]` is 1, `sum_values[1]` is 1, `values[2]` is 2, `sum_values[2]` is 3, `values[3]` is 3, `sum_values[3]` is 6, `values[4]` is 4, `sum_values[4]` is 10, `values[5]` is 5, `sum_values[5]` is 15, `values[6]` is 6, `sum_values[6]` is 21, `values[7]` is 7, `sum_values[7]` is 28, `values[8]` is 8, `sum_values[8]` is 36, `values[9]` is 9, `sum_values[9]` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: `total` is 45, `i` is `n`, `n` is the last input integer, `values` is a list of integers where each value at index `i` is the sum of the values at the indices corresponding to the last digit and the remainder of `i` when split into digits, `sum_values` is a list of integers where each value at index `i` is the cumulative sum of the values in `values` up to index `i`.
    for n in numbers:
        print(sum_values[n])
        
    #State: `total` is 45, `i` is the last input integer from the `numbers` list, `n` is the last input integer from the `numbers` list, `values` is a list of integers, `sum_values` is a list of integers, `numbers` must be a non-empty list of integers.
#Overall this is what the function does:The function `func_1` reads an integer `t` from user input, representing the number of integers to be processed. It then reads `t` integers from user input and stores them in a list `numbers`. The function initializes two lists, `values` and `sum_values`, with a length of `max(numbers) + 1` (if `numbers` is not empty) to store specific integer values and their cumulative sums, respectively. The first 10 elements of `values` and `sum_values` are set to the integers 0 through 9 and their cumulative sums, respectively. For each integer `i` from 10 to the maximum value in `numbers`, the function calculates the value at index `i` in `values` as the sum of the values at the indices corresponding to the last digit and the remainder of `i` when split into digits. The cumulative sum up to `i` is stored in `sum_values`. Finally, the function prints the cumulative sum for each integer in `numbers`. The function does not return any value.

