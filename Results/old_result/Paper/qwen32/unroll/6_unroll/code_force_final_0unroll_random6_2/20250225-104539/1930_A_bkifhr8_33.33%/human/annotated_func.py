#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 5000) representing the number of test cases. For each test case, it receives an integer n (1 ≤ n ≤ 50) indicating that there are 2n integers on the whiteboard. It also receives a list of 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7) representing the numbers written on the whiteboard.
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
        
    #State: ans_f is a list containing the sums of the minimum values of each pair of integers for each test case.
    for i in ans_f:
        print(i)
        
    #State: The sums of the minimum values of each pair of integers for each test case have been printed, and the list `ans_f` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then calculates the sum of the minimum values of each pair of integers from the list and prints the result for each test case.

