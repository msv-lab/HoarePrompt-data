#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 50) representing the length of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. The number of test cases t satisfies 1 ≤ t ≤ 1000.
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
        
    #State: The loop control variable `_` will have the value `t` after the loop finishes, and the variables `n` and `a` will have the values from the last test case processed. The output will be a sequence of "YES" or "NO" corresponding to each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. It checks if the list is non-decreasing or if it can be made non-decreasing by removing the first element. For each test case, it outputs "YES" if the list meets the criteria and "NO" otherwise.

