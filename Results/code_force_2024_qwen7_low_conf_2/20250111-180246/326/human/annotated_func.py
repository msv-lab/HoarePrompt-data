#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and there are 2n positive integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 5000\), `ans_f` is a list containing `t` elements, each element representing the sum of the minimum values of pairs of elements from `lst` until the conditions of the loop no longer hold, `n` is the integer input by the user for each iteration, `i` is `n * 2 + k` where `k` is the number of times the loop did not execute due to the condition `len(lst) == 2`, `l` is the string input by the user for each iteration, `lst` is the list of strings obtained by splitting `l` by spaces and modified according to the loop conditions, `ans` is the cumulative sum of the minimum values of pairs of elements in `lst` until the length of `lst` becomes 2 or less.
    for i in ans_f:
        print(i)
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 5000\), `ans_f` is a list containing `t` elements, `n` is the integer input by the user for each iteration, `i` is within the bounds of `ans_f`, `l` is the string input by the user for each iteration, `lst` is a list of strings obtained by splitting `l` by spaces and modified according to the loop conditions, `ans` is the cumulative sum of the minimum values of pairs of elements in `lst` until the length of `lst` becomes 2 or less, and all elements in `ans_f` are printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves an integer `t` (1 ≤ t ≤ 5000) indicating the number of subsequent test cases to process, followed by an integer `n` (1 ≤ n ≤ 50) and 2n positive integers `a_1, a_2, ..., a_{2n}` (1 ≤ a_i ≤ 10^7). For each test case, the function reads these integers, splits them into pairs, and calculates the sum of the minimum values of each pair until the list of integers is reduced to 2 or fewer elements. This process is repeated for each test case, and the results are stored in a list `ans_f`. After processing all test cases, the function prints the results for each test case. The final state of the program includes the list `ans_f` containing the sums of the minimum values for each test case.

