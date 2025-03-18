#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50) and each integer a_i (1 ≤ a_i ≤ 10^7).
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
        
    #State: Output State: `t` is the same input integer, `ans_f` is a list containing `t` elements, each element being the sum of the minimum values of pairs from the input lists.
    for i in ans_f:
        print(i)
        
    #State: The loop prints each element in the list `ans_f`, which contains `t` elements, each being the sum of the minimum values of pairs from the input lists. The variables `t` and `ans_f` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from user input, representing the number of test cases. It then reads `t` lines of input, each containing a list of 2n integers (where 1 ≤ n ≤ 50). For each test case, the function calculates the sum of the minimum values of pairs of integers from the input list and appends this sum to a result list `ans_f`. After processing all test cases, the function prints each element in `ans_f`, which contains `t` elements, each being the sum of the minimum values of pairs from the corresponding input list. The function does not return any value.

