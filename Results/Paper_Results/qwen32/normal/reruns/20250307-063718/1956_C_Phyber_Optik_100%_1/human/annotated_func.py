#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500), the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 500), which represents the size of the n × n matrix a. The sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: t is 0; n is the last input integer; sum is (n(n + 1)/2)^2 for the last test case; j is n + 1.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates a specific sum based on the matrix size and prints this sum along with `2n`. It then prints a sequence of `2n` lines, each containing a specific pattern of numbers related to the matrix size.

