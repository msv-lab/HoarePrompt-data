#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [1, t, 3, t-1, 5, t-2, ...]
#Overall this is what the function does:The function reads a positive integer `t` from the user, creates a list `a` containing integers from 1 to `t`, reverses every second element in the list, and prints the modified list. The final state of the program is that it has printed a list where the odd-indexed elements are reversed compared to their original order.

