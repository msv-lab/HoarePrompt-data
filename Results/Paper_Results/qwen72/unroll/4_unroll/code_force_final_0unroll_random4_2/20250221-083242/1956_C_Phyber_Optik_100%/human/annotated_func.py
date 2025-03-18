#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix. The number of test cases t is an integer (1 ≤ t ≤ 500). The sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: The loop will have processed all t test cases. For each test case, it will have printed the sum calculated using the formula \( \sum_{i=2}^{n} (i^2 - (i-1)^2) \cdot i \) followed by \( 2n \). Additionally, for each test case, it will have printed two lines for each row of the n×n matrix, where the first line starts with 1 and the second line starts with 2, both followed by the row number and a sequence of integers from 1 to n. The variable `t` will be unchanged, and the variable `n` will be the value of the last test case processed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 500), representing the size of an n×n matrix. The function calculates and prints the sum of the series \( \sum_{i=2}^{n} (i^2 - (i-1)^2) \cdot i \) followed by the value `2n`. Additionally, for each test case, it prints two lines for each row of the n×n matrix: the first line starts with 1 and the second line starts with 2, both followed by the row number and a sequence of integers from 1 to n. After processing all test cases, the variable `t` remains unchanged, and the variable `n` holds the value of the last test case processed.

