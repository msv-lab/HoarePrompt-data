#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: 1 [n] 3 [n-1] 5 [n-3] ... (where [n] is the last element, [n-1] is the second last element, and so on, following the pattern of reversing every second element)
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` (where 3 ≤ n ≤ 10^5) and constructs a list `a` containing integers from 1 to `n`. It then reverses every second element in the list and prints the modified list. The function does not return any value but prints the final state of the list for each test case.

