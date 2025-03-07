#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] <= a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all_new = all([(a[0] >= new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all_new and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: t is a positive integer between 1 and 1, `n` is an input integer, `a` is a list of integers, `check_all` is a boolean indicating whether all elements in `a` from index 0 to `n-2` are less than or equal to the next element, and the final output of the program is determined based on the conditions checked within the loop. If `check_all` remains `True` throughout all iterations and no segment of the list `a` from index `i` to the end satisfies both `check_all_new` and `new_all` being `True`, the program will print 'NO'. Otherwise, if any segment satisfies these conditions, the program will print 'YES'.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t`, an integer `n`, and a list of `n` integers `a`. For each test case, it checks if the list `a` is non-decreasing (each element is less than or equal to the next). If `a` is non-decreasing, it prints 'YES'. If not, it checks if there exists a subsegment of `a` starting from index 1 that can be rearranged to form a non-decreasing sequence while maintaining the first element of `a`. If such a subsegment is found, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the result for each test case.

