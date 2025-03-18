#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers a_1, a_2, ..., a_{2n} are integers such that 1 ≤ a_i ≤ 10^7.
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
        
    #State: Output State: After the loop executes all its iterations, `t` remains the same as it was initially (an integer between 1 and 5000), `ans_f` is a list containing the cumulative sum of `ans` for each iteration of the loop, and `lst` is an empty list since all elements have been processed according to the conditions inside the loop. The variable `i` is no longer used in the final state but was incremented in each iteration of the loop. The state of `n` is not relevant in the final output state as it is an input for each iteration and gets replaced with new values in each iteration.
    for i in ans_f:
        print(i)
        
    #State: t is an integer between 1 and 5000, ans_f is a list containing the cumulative sums of ans for each iteration, lst is an empty list, i is the last element of ans_f.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( t \) (number of test cases), an integer \( n \) (half the number of elements in the sequence), and a sequence of \( 2n \) integers \( a_1, a_2, \ldots, a_{2n} \). For each test case, it calculates the sum of the minimum values of every pair of consecutive integers in the sequence and stores these sums in a list. Finally, it prints each calculated sum. The function does not return any value but modifies a list `ans_f` which contains the results for all test cases.

