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
        
    #State: `ans_f` contains the sum of the minimum values of all possible pairs from the list `lst` for each iteration, and `i` is equal to `t * 2`.
    for i in ans_f:
        print(i)
        
    #State: `ans_f` must contain at least three elements, and `i` is equal to the last element in `ans_f`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t (number of test cases) and an integer n (number of pairs of integers), along with 2n integers a_1, a_2, ..., a_{2n}. For each test case, it calculates the sum of the minimum values of all possible pairs from the list of integers and stores these sums in a list. Finally, it prints each sum from the list.

