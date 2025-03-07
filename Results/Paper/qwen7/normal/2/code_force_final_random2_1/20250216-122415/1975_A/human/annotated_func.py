#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n positive integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: The value of `t` will be 0, indicating that no more inputs need to be processed. For each iteration of the loop, the conditions described in the previous states will have been checked, and based on those checks, either 'YES' or 'NO' will have been printed for each input list `a`. After all iterations, if `t` was originally greater than 0, it would now be 0, signifying that all inputs have been processed. The final output will be 'NO' if none of the conditions for 'YES' were met across all inputs; otherwise, 'YES' would have been printed for at least one input list `a`.
    #
    #This means that after all iterations of the loop, the output will be a series of 'YES' or 'NO' based on the conditions checked for each input list `a`, and the loop variable `t` will be 0, indicating the end of processing.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (number of test cases), an integer \( n \) (length of the list), and a list \( a \) of \( n \) positive integers. For each test case, it checks if the list \( a \) is non-decreasing. If the list is non-decreasing, it prints 'YES'. Otherwise, it checks if the list can be split into two parts such that the first part is non-increasing and the second part is non-decreasing. If such a split exists, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function ensures that the variable \( t \) is set to 0, indicating the end of processing.

