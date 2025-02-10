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
        
    #State: `t` is 0, `n` is an input integer, `a` is a list of integers from the last user input, `check_all` is `True` if `a` is strictly increasing, otherwise `False`. If `check_all` is `False`, `i` is set to `n-1`, and if any `a[i - 1]` is greater than `a[i]` during the loop, `new` is the sublist of `a` starting from that index to the end, and `new_all` is `True` if `new` is sorted in non-decreasing order, otherwise `False`. The loop will break if `check_all` and `new_all` are both `True` or if either is `False`. If no such condition is met, the loop completes all iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it checks if the list `a` is strictly increasing. If so, it prints 'YES'. If not, it further checks if there exists a point in the list where, after this point, the remaining elements form a non-decreasing sequence and all elements before this point are greater than all elements after this point. If such a point exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function ends.

