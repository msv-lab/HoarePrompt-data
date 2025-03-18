#State of the program right berfore the function call: The function `func` is expected to be called with no arguments, but it internally processes multiple test cases. Each test case includes an integer n (2 ≤ n ≤ 50) representing the length of the array a, and a list of n positive integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6) representing the elements of the array a. The number of test cases t is an integer (1 ≤ t ≤ 1000).
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
        
    #State: The loop has finished executing all iterations. The variable `t` is now 0, as it has been decremented by the loop. The variables `n` and `a` are not defined outside the loop and are reset with each iteration based on the input. The variables `check_all`, `new`, `check_all_new`, and `new_all` are also reset with each iteration and do not persist outside the loop.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case involves reading an integer `n` (2 ≤ n ≤ 50) and a list of `n` positive integers (1 ≤ a_i ≤ 10^6). The function checks if the list is non-decreasing. If it is, it prints 'YES'. If not, it checks if the list can be split into two parts such that the first part is non-increasing and the second part is non-decreasing. If such a split is possible, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function concludes and no variables persist outside the function.

