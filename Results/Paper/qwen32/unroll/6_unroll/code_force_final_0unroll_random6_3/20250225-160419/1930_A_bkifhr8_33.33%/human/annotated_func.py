#State of the program right berfore the function call: Each test case consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 50) representing the number of pairs of integers on the whiteboard. The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7) representing the numbers written on the whiteboard. The input starts with an integer t (1 ≤ t ≤ 5000) indicating the number of test cases.
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
        
    #State: `ans_f` is a list containing the sum of the minimums of the pairs for each test case.
    for i in ans_f:
        print(i)
        
    #State: Each element in the list `ans_f` is printed on a new line. The state of `ans_f` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of pairs of integers. For each test case, it calculates the sum of the minimum values from each pair and prints the result for each test case on a new line.

