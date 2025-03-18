#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an input integer where 1 ≤ t ≤ 5000; `ans_f` is a list containing the sum of the minimum values of pairs of numbers read from input, repeated `n * 2` times for each `n` provided, where `n` is the value of `t`.
    for i in ans_f:
        print(i)
        
    #State: Output State: `ans_f` is a list containing the sum of the minimum values of pairs of numbers read from input, repeated `t * 2` times for each `t` provided, where `t` is the initial input integer; each element in the list is printed in separate lines during the loop execution.
#Overall this is what the function does:The function processes a series of test cases, where each case involves an integer t (1 ≤ t ≤ 5000) and an integer n (1 ≤ n ≤ 50), along with 2n integers a_1, a_2, …, a_{2n} (1 ≤ a_i ≤ 10^7). For each test case, it calculates the sum of the minimum values of all possible pairs of numbers from the given list and stores these sums in a list. Finally, it prints each sum from the list on a new line.

