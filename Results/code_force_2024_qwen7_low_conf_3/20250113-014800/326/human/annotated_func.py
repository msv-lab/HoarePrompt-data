#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the list contains 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    ans_f = []
    for i in range(t):
        ans = 0
        
        n = int(input())
        
        l = input()
        
        lst = l.split(' ')
        
        for i in range(n * 2):
            if len(lst) != 2:
                ans += min(int(lst[0]), int(lst[1]))
                lst.remove(lst[0 * 2])
                lst.remove(lst[1 * 2])
            else:
                ans += min(int(lst[0]), int(lst[1]))
                break
        
        ans_f.append(ans)
        
    #State of the program after the  for loop has been executed: `t` is an integer between 1 and 5000, `ans_f` is a list containing the sum of the minimums of all valid pairs of integers extracted from the input strings `l`, where each `l` corresponds to an input integer `n` and is processed as described in the loop. `n` is a positive integer for each iteration, and `i` is always `n * 2`. `lst` is either empty or contains the remaining elements after all valid pairs are formed for the last iteration.
    for i in ans_f:
        print(i)
        
    #State of the program after the  for loop has been executed: `t` is an integer between 1 and 5000, `ans_f` is a list containing the sum of the minimums of all valid pairs of integers extracted from the input strings `l`, where each `l` corresponds to an input integer `n` and is processed as described in the loop, `n` is a positive integer for each iteration, `i` is `n * 2`, `lst` is either empty or contains the remaining elements after all valid pairs are formed for the last iteration, the value of `i` is printed for each iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves an integer \( n \) (1 ≤ \( n \) ≤ 50) and a list of \( 2n \) integers (1 ≤ \( a_i \) ≤ \( 10^7 \)). For each test case, the function calculates the sum of the minimum values of all valid pairs of integers from the list. After processing all test cases, the function prints the result of each test case. The function handles the following edge cases:
1. If the list length is less than 2, the function processes whatever elements are available.
2. The function ensures that the list is processed completely or partially based on the available elements.

