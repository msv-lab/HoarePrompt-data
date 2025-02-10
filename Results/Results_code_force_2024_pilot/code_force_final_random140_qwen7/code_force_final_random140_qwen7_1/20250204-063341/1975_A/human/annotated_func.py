#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n positive integers where each element a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: All variables outside the loop remain unchanged. Specifically, `t` retains its initial value, `n` and `a` retain their final values after the last iteration of the loop. `check_all` and `new_all` are determined based on the final state of the list `a` and the value of `n`.
#Overall this is what the function does:The function processes up to 1000 test cases. For each test case, it reads a list of integers `a` of length `n` (where `2 ≤ n ≤ 50`) and checks if the list is strictly increasing. If not, it further checks if the list can be split into two parts such that the first part is strictly increasing and the second part, when reversed, is also strictly increasing. The function prints 'YES' if either condition is met for any test case, otherwise it prints 'NO'. The final output is based on the conditions evaluated for each test case.

