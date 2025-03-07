#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains n (2 ≤ n ≤ 100) integers (1 ≤ a_i ≤ 10^9) representing the elements of the array a for each test case.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: `ntest` must be greater than or equal to the number of iterations, `itest` is `ntest - 1`, `n` is an input integer, `a` is a sorted list of integers provided by the user that must have at least 2 elements, `kq` is the sum of the differences between the corresponding pairs of elements from the end and the beginning of the list `a` for the first half of the list, `i` is `len(a) // 2 - 1`.
#Overall this is what the function does:The function reads a series of test cases from the user. For each test case, it reads an integer `n` and a list of `n` integers, sorts the list, and calculates the sum of the differences between the corresponding pairs of elements from the end and the beginning of the sorted list for the first half of the list. It prints this sum for each test case. The function does not return any values. After the function concludes, the input values for `ntest`, `itest`, `n`, `a`, and `kq` are no longer relevant as they are local to the function.

