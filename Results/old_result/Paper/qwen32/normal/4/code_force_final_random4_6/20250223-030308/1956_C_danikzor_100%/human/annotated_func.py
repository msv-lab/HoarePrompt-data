#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n x n matrix filled with zeroes. The number of test cases t is between 1 and 500. The sum of n^2 over all test cases does not exceed 5 * 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: - Since `n` is a variable whose value is not explicitly provided, we describe the output in terms of `n`.
    #   - The first value printed is the sum of squares of the first `n` natural numbers.
    #   - The second value printed is twice the value of `n`.
    #
    #Thus, the output of the `print` statement is described as follows:
    #Output:
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The loop will output `2n` lines in total. For each `i` from 1 to `n`, there will be two lines printed: the first line starting with `1` and the second line starting with `2`, both followed by `i` and the sequence `n, n-1, ..., 2, 1`.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, prints the sum of squares of the first `n` natural numbers and twice the value of `n`, and then prints `2n` lines. Each pair of lines consists of a sequence starting with `1` and `2`, followed by the current index `i` and the sequence `n, n-1, ..., 2, 1`. The function does not return any value.

