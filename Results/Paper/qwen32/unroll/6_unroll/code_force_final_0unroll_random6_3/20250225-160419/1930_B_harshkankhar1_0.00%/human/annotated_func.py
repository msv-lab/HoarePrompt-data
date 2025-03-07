#State of the program right berfore the function call: Each test case contains a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p. The first line of the input contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. The sum of n over all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a (where a is the list formed by reversing the elements at even indices of the permutation p and keeping the elements at odd indices unchanged)
#Overall this is what the function does:The function `func_1` processes multiple test cases, where each test case consists of an integer `n` (3 ≤ n ≤ 10^5) representing the length of a permutation `p`. For each test case, it creates a list `a` containing integers from 1 to `n`, reverses the elements at even indices of this list, and prints the modified list.

