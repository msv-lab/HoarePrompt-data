#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 50) representing the length of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. There are multiple test cases, with the first line containing the number of test cases t (1 ≤ t ≤ 1000).
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
        
    #State: The output state consists of `t` lines, each corresponding to the result of a test case. Each line contains either 'YES' or 'NO' based on whether the array `a` can be split into two parts such that the first part is non-decreasing and the second part is also non-decreasing, with the first element of the array being greater than or equal to all elements in the second part.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it determines if the list can be split into two parts such that the first part is non-decreasing, the second part is non-decreasing, and the first element of the list is greater than or equal to all elements in the second part. It outputs 'YES' if such a split is possible, otherwise 'NO'.

