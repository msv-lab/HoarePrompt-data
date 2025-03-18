#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 50, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^6, representing the elements of the array a.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] < a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all = all([(a[0] > new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: After all iterations of the loop, `_` is equal to `t`, `t` is an input integer between 1 and 1000, `n` is a new input integer between 2 and 50, and `a` is a list of integers read from the input. For each iteration, if `check_all` is `True`, it means all elements in `a` are in strictly increasing order, and 'YES' is printed. If `check_all` is `False`, the loop checks each pair of consecutive elements in `a` from index 1 to `n-1`. If at any point `a[i - 1]` is greater than `a[i]`, `new` is set to the sublist of `a` starting from index `i` to the end. `check_all` is `True` if all elements in `new` are less than `a[0]`, and `new_all` is `True` if all elements in `new` are in non-decreasing order. If both `check_all` and `new_all` are `True`, 'YES' is printed and the loop breaks. Otherwise, 'NO' is printed and the loop breaks. If no such condition is met, the loop completes all iterations without printing anything.
#Overall this is what the function does:The function `func` reads an integer `t` (1 ≤ t ≤ 1000) indicating the number of test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 50) and a list `a` of `n` integers (1 ≤ a_i ≤ 10^6). It then checks if the list `a` is either strictly increasing or can be split into two parts where the first part is strictly increasing and the second part is non-decreasing and all elements in the second part are less than the first element of the list. If either condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function completes without returning any value.

