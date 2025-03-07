#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. The subsequent line for each test case contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers entered by the user for each test case, where each list corresponds to the n integers a_1, a_2, ..., a_n for each test case.
#Overall this is what the function does:The function processes user input for multiple test cases. For each test case, it reads a line of input containing `n` integers and returns a list of these integers. The function does not accept any direct parameters but interacts with the user to gather the required data.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two integers n and x such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. Each of the following n lines contains an integer a_i such that 0 ≤ a_i < 2^30.
def func_2():
    return int(input())
    #The program returns an integer input by the user, which is within the range of 1 to 10^4.
#Overall this is what the function does:The function reads an integer input from the user, which must be within the range of 1 to 10^4, and returns this integer.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. Additionally, the subsequent line for each test case contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing integers split from the input for each test case. Each map object corresponds to the integers n and x followed by n integers a_1, a_2, ..., a_n for each test case, where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, and 0 ≤ a_i < 2^30.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and x, followed by n integers a_1, a_2, ..., a_n. It returns a map object containing these integers for each test case, where 1 ≤ n ≤ 10^5, 0 ≤ x < 2^30, and 0 ≤ a_i < 2^30.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. The following line contains a list of n integers representing the array a, where 0 ≤ a_i < 2^30.
def func_4():
    return input().strip()
    #The program returns the first input line after stripping any trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns the first input line after stripping any trailing whitespace.

#State of the program right berfore the function call: (n, x) is a tuple of two integers where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; a is a list of n integers where 0 ≤ a_i < 2^30.
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
        
    #State: `t` is an empty list, `ans` is the maximum count of times `op` became 0 during any iteration of the loop, `i` is 0, `u` is 0, and `v` is 0.
    return max(ans, len(a))
    #The program returns the maximum value between ans (which is the maximum count of times op became 0 during any iteration of the loop) and len(a) (which is the length of list a)
#Overall this is what the function does:The function processes a list of integers `a` and an integer `x`. It iterates over the bits of `x` and compares them with the corresponding bits of the integers in `a`. Based on these comparisons, it updates a counter `ans` which tracks the maximum number of times a specific condition is met during the iterations. Finally, it returns the maximum value between `ans` and the length of the list `a`. If no valid operations are performed, it returns -1.

