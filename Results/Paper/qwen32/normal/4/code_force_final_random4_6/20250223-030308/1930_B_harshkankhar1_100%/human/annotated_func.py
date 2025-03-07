#State of the program right berfore the function call: Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. For each test case, the first line contains a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p. It is guaranteed that the sum of n over all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: a (where a is the permutation list of numbers from 1 to n with elements at even indices reversed)
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` representing the length of a permutation. For each test case, it generates a permutation of numbers from 1 to `n`, reverses the elements at even indices, and prints the resulting permutation.

