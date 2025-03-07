#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. For each test case, n, f, and k are positive integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 100.
def func():
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k - 1] < x else 'MAYBE')
        
    #State: Output State: The list `a` is sorted in descending order after all iterations. The variable `x` is set to the element at index `f - i` in list `a`, where `i` is the number of iterations minus one (since the loop starts from zero). The variable `n` remains the same as the input integer from the first split. The variable `f` is reduced by the total number of iterations, and `k` is reduced by the total number of iterations as well. If any condition in the if-else block triggers a change, it will be reflected in the output based on the logic provided; otherwise, the values of `x`, `f`, and `k` will be adjusted accordingly but will not change the overall sorted order of `a`.
    #
    #In simpler terms, after all iterations, the list `a` will be sorted in descending order, `x` will be the element at the adjusted index `f - i` where `i` is the number of iterations, and `n`, `f`, and `k` will be reduced by the number of iterations.
#Overall this is what the function does:The function processes a list of integers `a` of length `n` and checks a condition involving indices `f` and `k`. After processing, the list `a` is sorted in descending order. The function then compares the element at index `f` with the element at index `k` in the sorted list. Based on the comparison, it prints either 'YES', 'NO', or 'MAYBE'. The function does not return any value but modifies the list `a` and prints the result for each test case.

