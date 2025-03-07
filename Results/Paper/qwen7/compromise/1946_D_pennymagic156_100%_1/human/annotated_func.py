#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. Additionally, the subsequent line for each test case contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers entered by the user for each test case, where each list contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
#Overall this is what the function does:The function processes input from the user for multiple test cases. For each test case, it reads an integer t indicating the number of cases, followed by t pairs of integers n and x, and then n integers a_1, a_2, ..., a_n. It returns a list containing t lists, where each inner list consists of n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and x such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30; and the third line is empty or contains additional input which should be ignored.
def func_2():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function accepts no parameters and returns an integer input by the user.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and x separated by a space, where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; the second line contains n integers a_1, a_2, ..., a_n separated by spaces, where 0 ≤ a_i < 2^30; and the function does not return anything for the current function signature, implying that the main logic for solving each test case is implemented elsewhere.
def func_3():
    return map(int, input().split())
    #The program returns two integers n and x separated by a space, where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30.
#Overall this is what the function does:The function reads input from standard input, including an integer t (1 ≤ t ≤ 10^4) indicating the number of test cases, followed by t test cases. Each test case consists of two integers n and x (1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30), and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < 2^30). After processing the input, the function returns two integers n and x from the first test case, separated by a space.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 <= n <= 10^5 and 0 <= x < 2^30. Additionally, the subsequent input contains n integers representing the array a for each test case.
def func_4():
    return input().strip()
    #The program returns the first line of input after stripping any trailing whitespace, which represents the number of test cases 't'.
#Overall this is what the function does:The function reads the first line of input, strips any trailing whitespace, and returns it as the number of test cases 't'.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, x is an integer such that 0 ≤ x < 2^30, and a is a list of n integers such that 0 ≤ a_i < 2^30 for all i from 1 to n.
def func_5():
    n, x = func_3()
    a = func_1()
    t, ans = [], -1
    for i in range(29, -1, -1):
        u, v = x >> i & 1, sum([(val >> i & 1) for val in a])
        
        if u == v == 0:
            continue
        
        if u == 0:
            if v % 2:
                return ans
            else:
                op = ai = 0
                for val in a:
                    op ^= val >> i & 1
                    ai ^= val
                    if not op:
                        t.append(ai)
                        ai = 0
                a, t = t, []
        elif v % 2:
            continue
        elif v:
            op = cnt = 0
            for val in a:
                op ^= val >> i & 1
                if not op:
                    cnt += 1
            ans = max(ans, cnt)
        else:
            break
        
    #State: Output State: `t` is an empty list, `ans` is the maximum value found during the loop execution, `i` is 0, `u` is `a[0] >> 0 & 1`, `v` is the sum of `[(val >> 0 & 1) for val in a]`.
    #
    #In this final state, after all iterations of the loop (from 29 down to 0), the list `t` remains empty because no elements were appended to it throughout the loop's execution. The variable `ans` holds the highest value among all counts of consecutive zeros found in the binary representation of the elements in `a`, as determined by the loop. The variable `i` reaches 0 after the last iteration. The variable `u` is the least significant bit of the first element in `a`, and `v` is the sum of the least significant bits of all elements in `a`.
    return max(ans, len(a))
    #The program returns the maximum value between ans and the length of list a.
#Overall this is what the function does:The function processes a list of integers `a` and an integer `x` to find the maximum count of consecutive zeros in the binary representation of the elements in `a`. If certain conditions are met, it returns -1 or 0, otherwise, it returns the maximum value between -1 or 0 and the length of the list `a`.

