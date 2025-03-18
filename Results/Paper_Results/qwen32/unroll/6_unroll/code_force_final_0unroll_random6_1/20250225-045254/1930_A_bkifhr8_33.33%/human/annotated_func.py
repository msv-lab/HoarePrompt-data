#State of the program right berfore the function call: The function receives multiple test cases. For each test case, it is given an integer n (1 ≤ n ≤ 50) representing half the number of integers on the whiteboard, and a list of 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7) representing the numbers written on the whiteboard. The number of test cases t (1 ≤ t ≤ 5000) is provided at the start.
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
        
    #State: `ans_f` is a list containing the results of each test case, where each result is the sum of the minimum values of the pairs formed from the input list for that test case.
    for i in ans_f:
        print(i)
        
    #State: `ans_f` is a list containing the results of each test case, where each result is the sum of the minimum values of the pairs formed from the input list for that test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of the minimum values of `n` pairs formed from the list and prints the result for each test case.

