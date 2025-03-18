#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes for each test case.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: `t` is an input integer representing the number of test cases (1 ≤ t ≤ 10^4), `numbers` is a list containing `t` elements, each element being an input integer.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: `t` is an input integer representing the number of test cases (1 ≤ t ≤ 10^4), `numbers` is a list containing `t` elements, each element being an input integer, `values` is a list of length `max(numbers) + 1` with the first 10 elements set to `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` and all other elements initialized to 0, `sum_values` is a list of length `max(numbers) + 1` with the first 10 elements set to `[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]` and all other elements initialized to 0, `total` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: t is an input integer representing the number of test cases (1 ≤ t ≤ 10^4), numbers is a list containing t elements, each element being an input integer, values is a list of length max(numbers) + 1 with the first 10 elements set to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and all other elements initialized to 0 except values[10] which is 1, values[11] which is 2, and values[12] which is 3, sum_values is a list of length max(numbers) + 1 with the first 10 elements set to [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] and all other elements initialized to 0, except sum_values[10] which is 46, sum_values[11] which is 48, and sum_values[12] which is 51, total is 45.
    for n in numbers:
        print(sum_values[n])
        
    #State: t is an input integer representing the number of test cases (1 ≤ t ≤ 10^4), numbers is a list containing t elements, each element being an input integer, values is a list of length max(numbers) + 1 with the first 10 elements set to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and all other elements initialized to 0 except values[10] which is 1, values[11] which is 2, and values[12] which is 3, sum_values is a list of length max(numbers) + 1 with the first 10 elements set to [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] and all other elements initialized to 0, except sum_values[10] which is 46, sum_values[11] which is 48, and sum_values[12] which is 51, total is 45. The loop has iterated t times, and for each n in numbers, the value sum_values[n] has been printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the next `t` lines, it reads an integer `n` and prints the sum of the values of all digits from 1 to `n`, where the value of a number is defined as the sum of the values of its digits.

