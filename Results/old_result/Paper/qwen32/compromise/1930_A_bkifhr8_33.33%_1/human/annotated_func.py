#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 50) representing the number of pairs of integers on the whiteboard. The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7) representing the numbers written on the whiteboard. The total number of test cases t is between 1 and 5000.
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
        
    #State: `t` is an input integer representing the number of test cases, where \(1 \leq t \leq 5000\); `ans_f` is a list containing the final values of `ans` for each test case; `i` is `n * 2 + 1` if the loop completes all iterations or the iteration number when the loop breaks if `lst` becomes exactly 2 elements; `ans` is the sum of the minimum values of pairs of elements from `lst` until `lst` is reduced to 2 elements or fewer; `n` is the number of pairs processed; `l` is the input string; `lst` is either empty or has 2 elements.
    for i in ans_f:
        print(i)
        
    #State: `t` is an input integer representing the number of test cases, where \(1 \leq t \leq 5000\); `ans_f` is a list containing the final values of `ans` for each test case and has `t` elements; `i` is the last element in `ans_f`; `ans` is the sum of the minimum values of pairs of elements from `lst` until `lst` is reduced to 2 elements or fewer for the last test case; `n` is the number of pairs processed for the last test case; `l` is the input string for the last test case; `lst` is either empty or has 2 elements for the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of the minimum values of pairs of integers from the list until only two or fewer integers remain. The function outputs the result for each test case.

