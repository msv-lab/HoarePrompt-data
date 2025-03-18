#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [a1, a2[::-1], a3, a4[::-1], a5, ...]
#Overall this is what the function does:The function processes a series of test cases, where each test case involves a positive integer `t` (1 ≤ t ≤ 10^3) and an integer `n` (3 ≤ n ≤ 10^5). For each test case, it generates a list of integers from 1 to `t`, reverses every second element in the list, and prints the modified list. The function does not return any value but prints the processed list for each test case.

