#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 50) representing the length of the array a, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. There are t (1 ≤ t ≤ 1000) such test cases.
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
        
    #State: All test cases have been processed and evaluated for whether the array `a` can be considered non-decreasing by potentially removing a prefix.
#Overall this is what the function does:The function evaluates multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it determines if the array can be made non-decreasing by potentially removing a prefix of the array. It prints 'YES' if the array can be made non-decreasing in this manner, otherwise it prints 'NO'.

