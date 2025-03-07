#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 50) representing the length of the array a, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. There are t (1 ≤ t ≤ 1000) such test cases.
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
        
    #State: The final output state consists of `t` lines, each containing either 'YES' or 'NO', corresponding to the result of each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it checks if the array is non-decreasing or can be made non-decreasing by removing a prefix. It outputs 'YES' if either condition is met, otherwise 'NO'.

