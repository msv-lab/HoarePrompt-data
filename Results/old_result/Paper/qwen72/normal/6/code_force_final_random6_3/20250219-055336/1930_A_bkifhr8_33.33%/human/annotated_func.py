#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50, 1 ≤ a_i ≤ 10^7) for each test case.
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
        
    #State: `t` is 0, `i` is `t - 1` (which is -1), `ans_f` is a list containing the sum of the minimum values of pairs of elements from each test case, `n` is the last input integer that must be greater than 0, `l` is the last input string, and `lst` is the last list of substrings obtained by splitting the last `l` using spaces as the delimiter. If the length of `lst` was initially greater than or equal to 2, `lst` will have all but the last two elements removed, and `ans` will be the sum of the minimum values of the pairs of elements removed. If the length of `lst` was exactly 2, `ans` will be the minimum of the two integers obtained by converting the substrings in `lst` to integers, and the loop will have exited after the first iteration.
    for i in ans_f:
        print(i)
        
    #State: `t` is 0, `i` has iterated through all elements of `ans_f`, `ans_f` contains all the elements it had initially, `n` is the last input integer that must be greater than 0, `l` is the last input string, `lst` is the last list of substrings obtained by splitting the last `l` using spaces as the delimiter, and `ans` is the sum of the minimum values of the pairs of elements removed if the length of `lst` was initially greater than or equal to 2, or the minimum of the two integers obtained by converting the substrings in `lst` to integers if the length of `lst` was exactly 2.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a space-separated string of 2n integers. It then processes these integers in pairs, summing the minimum value of each pair, and appends the result to a list `ans_f`. After processing all test cases, the function prints each element in `ans_f`, which contains the sum of the minimum values of pairs for each test case. The function does not return any value.

