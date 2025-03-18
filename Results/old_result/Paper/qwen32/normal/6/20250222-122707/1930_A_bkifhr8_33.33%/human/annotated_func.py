#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer t (1 ≤ t ≤ 5000) representing the number of test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 50), indicating that there are 2n integers on the whiteboard. The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7), which are the numbers written on the whiteboard.
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
        
    #State: `t` is equal to the number of test cases executed, `ans_f` is a list containing the accumulated sum of the minimum values from the first two elements of `lst` for each test case, `n` is the input integer for the last test case, `l` is the input string for the last test case, `lst` is a list with 2 or fewer elements for the last test case, and `i` is `n * 2` for the last test case if the loop executed all iterations without breaking early.
    for i in ans_f:
        print(i)
        
    #State: All elements in `ans_f` are printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of pairs of integers. For each test case, it calculates the sum of the minimum values from each pair and outputs the result for each test case.

