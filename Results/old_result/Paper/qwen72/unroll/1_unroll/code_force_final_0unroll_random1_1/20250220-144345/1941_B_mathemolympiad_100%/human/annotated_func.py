#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 3 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_j is such that 0 <= a_j <= 10^9. The sum of the values of n over all test cases does not exceed 2 * 10^5.
def func():
    numTest = int(input())
    for _ in range(0, numTest):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        stop = False
        
        for i in range(0, n - 2):
            if a[i] < 0:
                print('NO')
                stop = True
                break
            opNum = a[i]
            a[i] -= opNum
            a[i + 1] -= 2 * opNum
            a[i + 2] -= opNum
        
        if stop == True:
            continue
        
        if a[len(a) - 1] != 0 or a[len(a) - 2] != 0:
            print('NO')
        else:
            print('YES')
        
    #State: The values of `t` and `n` remain unchanged. The list `a` is modified for each test case, but the final state of `a` is not predictable without the specific input values. The variable `numTest` is decremented by the number of iterations the loop completes. The variable `stop` is reset to `False` at the beginning of each test case. The loop prints 'NO' if any element in `a` is negative during the iteration or if the last two elements of `a` are not zero after the loop. It prints 'YES' if the last two elements of `a` are zero after the loop.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then checks if any element in `a` is negative, and if so, prints 'NO' and moves to the next test case. If no element is negative, it performs a series of operations on the list `a` and checks if the last two elements of `a` are zero. If they are, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value, but it prints the result for each test case. The values of `t` and `n` remain unchanged, and the list `a` is modified for each test case, but its final state is not predictable without the specific input values.

