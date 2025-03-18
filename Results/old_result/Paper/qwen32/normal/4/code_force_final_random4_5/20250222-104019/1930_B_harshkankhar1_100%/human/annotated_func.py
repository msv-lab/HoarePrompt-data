#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer \( t \) (1 \(\leq\) \( t \) \(\leq\) 10\(^3\)) representing the number of test cases. Each of the next \( t \) lines contains a single integer \( n \) (3 \(\leq\) \( n \) \(\leq\) 10\(^5\)) representing the length of the permutation \( p \). The sum of \( n \) over all test cases does not exceed 10\(^5\).
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: elements of `a` where elements at even indices are reversed and elements at odd indices remain unchanged
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( n \) representing the length of a permutation. It outputs a permutation of the first \( n \) natural numbers such that the elements at even indices are reversed while the elements at odd indices remain unchanged.

