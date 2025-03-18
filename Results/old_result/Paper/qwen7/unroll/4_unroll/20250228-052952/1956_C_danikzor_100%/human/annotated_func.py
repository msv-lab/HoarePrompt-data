#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 500, n is an integer such that 1 ≤ n ≤ 500, and the following outputs are produced:
    #- For each i from 1 to n (inclusive), two lines are printed:
    #  1. A line starting with 1, followed by i and then the numbers from n down to 1.
    #  2. A line starting with 2, followed by i and then the numbers from n down to 1.
#Overall this is what the function does:The function processes a single test case defined by an integer \( n \) (where \( 1 \leq n \leq 500 \)). It calculates and prints the value of \( n \times (n + 1) \times (4 \times n - 1) // 6 \) followed by \( 2 \times n \). Subsequently, for each integer \( i \) from 1 to \( n \) (inclusive), it prints two lines: the first starting with 1 and the second with 2, each followed by \( i \) and the numbers from \( n \) down to 1. After processing all test cases, the function concludes with the specified outputs.

