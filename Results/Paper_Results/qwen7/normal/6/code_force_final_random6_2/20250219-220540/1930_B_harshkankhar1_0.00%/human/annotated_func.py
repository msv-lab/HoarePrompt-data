#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [1, 2, 3, 4, 5, ..., t-2, t-1, t-1, t-3, t-5, ..., 3, 1]
#Overall this is what the function does:The function reads a series of test cases, each containing a positive integer \( t \) and an integer \( n \). For each test case, it generates a list of integers from 1 to \( t \), reverses every second element in the list, and prints the modified list. The final state of the program is that it has processed all test cases and printed the modified lists.

