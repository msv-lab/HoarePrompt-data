#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes for each test case.
def func_1():
    t = int(input())
    numbers = []
    for _ in range(t):
        n = int(input())
        
        numbers.append(n)
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; `numbers` is a list containing `t` integers, each read from the input.
    values = [(0) for _ in range(max(numbers) + 1)]
    sum_values = [(0) for _ in range(max(numbers) + 1)]
    total = 0
    for i in range(10):
        values[i] = i
        
        total += i
        
        sum_values[i] = total
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; `numbers` is a list containing `t` integers, each read from the input; `values` is a list where the first 10 elements are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and the rest are 0; `sum_values` is a list where the first 10 elements are [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] and the rest are 0; `total` is 45.
    for i in range(10, n + 1):
        word = str(i)
        
        last = int(word[len(word) - 1])
        
        remainder = int(word[:-1])
        
        values[i] = values[last] + values[remainder]
        
        sum_total = values[i] + sum_values[i - 1]
        
        sum_values[i] = sum_total
        
    #State: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; numbers is a list containing t integers, each read from the input; values is a list where the first 10 elements are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and the rest are computed based on the loop; sum_values is a list where the first 10 elements are [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] and the rest are computed based on the loop; total is 45.
    for n in numbers:
        print(sum_values[n])
        
    #State: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4; numbers is a list containing t integers, each read from the input; values is a list where the first 10 elements are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and the rest are computed based on the loop; sum_values is a list where the first 10 elements are [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] and the rest are computed based on the loop; total is 45.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, followed by `t` integers `n`. For each `n`, it calculates and prints the sum of the values of all integers from 1 to `n`, where the value of each integer is defined recursively based on its last digit and the value of the integer obtained by removing the last digit.

