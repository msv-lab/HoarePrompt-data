#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n x n matrix a filled with zeroes. The input consists of multiple test cases, with the first line containing the number of test cases t (1 ≤ t ≤ 500). It is guaranteed that the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: The printed results for each test case, which include the calculated sum and `2n`, followed by the specified matrix patterns for each row from 1 to `n`.
#Overall this is what the function does:The function reads input to determine the number of test cases and the sizes of square matrices for each test case. For each test case, it calculates and prints a specific sum and a pattern of matrix indices.

