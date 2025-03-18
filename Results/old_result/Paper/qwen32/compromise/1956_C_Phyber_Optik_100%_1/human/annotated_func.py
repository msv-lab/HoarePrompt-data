#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix a filled with zeroes. The input consists of multiple test cases, with the first line containing the number of test cases t (1 ≤ t ≤ 500). It is guaranteed that the sum of n^2 over all test cases does not exceed 5⋅10^5.
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
        
    #State: t is 0, n is the last input integer, sum is \(\frac{n(n + 1)(4n - 1)}{6}\), j is \(n + 1\)
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it calculates a specific sum based on the formula \(\frac{n(n + 1)(4n - 1)}{6}\) and prints this sum along with `2n`. It then prints a series of `n` lines, each containing a sequence of numbers describing positions in an `n×n` matrix.

