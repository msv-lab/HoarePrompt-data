#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: 1 5 3 2 5 ... (where the list continues with the pattern of alternating between the first half and the reversed second half of the list)
#Overall this is what the function does:The function reads a positive integer `t` from input, which represents the number of test cases. For each test case, it generates a list of integers from 1 to `t`, reverses the order of every second element starting from the first, and then prints the modified list. The final output is a series of lists, each representing the processed sequence for a given test case.

