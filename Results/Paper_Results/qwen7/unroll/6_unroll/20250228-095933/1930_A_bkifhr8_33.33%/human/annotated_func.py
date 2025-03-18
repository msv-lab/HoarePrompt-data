#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers on the whiteboard are 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: `t` is an input integer between 1 and 5000; `ans_f` is a list containing the sum of the minimum values of pairs of numbers for each input case, where each pair is taken from the list of space-separated integers provided for each case.
    for i in ans_f:
        print(i)
        
    #State: Output State: `ans_f` is a list containing the sum of the minimum values of pairs of numbers for each input case, and the loop prints each element of `ans_f`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t and an integer n, along with 2n integers a_1, a_2, ..., a_{2n}. For each test case, it calculates the sum of the minimum values of all possible pairs of numbers from the given list and stores these sums in a list ans_f. Finally, it prints each element of ans_f.

