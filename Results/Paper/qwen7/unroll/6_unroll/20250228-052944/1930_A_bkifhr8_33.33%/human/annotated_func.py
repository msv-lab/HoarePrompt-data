#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an input integer between 1 and 5000 inclusive; `ans_f` is a list containing the sum of the minimum values of pairs from the input lists for each iteration of the outer loop.
    for i in ans_f:
        print(i)
        
    #State: Output State: `ans_f` is a list containing the sum of the minimum values of pairs from the input lists for each iteration of the outer loop; `t` is an input integer between 1 and 5000 inclusive. After the loop executes all the iterations, the value of `t` remains unchanged, and `ans_f` contains the printed values from each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `n` and `2n` integers. For each test case, it calculates the sum of the minimum values of all possible pairs of integers and stores these sums in a list `ans_f`. Finally, it prints each sum in `ans_f`. The function does not return any value but modifies the list `ans_f` and prints its contents.

