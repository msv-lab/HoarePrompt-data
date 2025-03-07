#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^3) representing the number of test cases. For each test case, it receives an integer n (3 ≤ n ≤ 10^5) which is the length of the permutation p. The sum of n across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: elements of the list `a` after reversing elements at even indices and keeping elements at odd indices unchanged
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and constructs a permutation of the first `n` natural numbers. It then reverses the elements at even indices (considering 0-based indexing) while keeping the elements at odd indices unchanged. The modified permutation is printed for each test case.

