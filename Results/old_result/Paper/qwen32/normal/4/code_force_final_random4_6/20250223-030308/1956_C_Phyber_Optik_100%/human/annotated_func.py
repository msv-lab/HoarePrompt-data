#State of the program right berfore the function call: Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a. The input consists of multiple test cases, with the first line containing the number of test cases t (1 ≤ t ≤ 500). The sum of n^2 over all test cases does not exceed 5 · 10^5.
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
        
    #State: t is 0, n is the value of the last test case, sum is the sum of cubes of integers from 1 to n for the last test case, j is n + 1.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates a sum related to the cubes of integers from 1 to `n` and prints this sum along with `2 * n`. It also prints a sequence of `n` lines, each containing two integers followed by a sequence of integers from 1 to `n`.

