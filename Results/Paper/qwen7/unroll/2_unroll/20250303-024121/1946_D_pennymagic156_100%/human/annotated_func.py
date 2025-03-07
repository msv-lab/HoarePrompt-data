#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. The following line contains a list of n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from user input, split and converted to integers.
#Overall this is what the function does:The function processes user input for multiple test cases. For each test case, it reads an integer `t` representing the number of test cases, then for each test case, it reads an integer `n`, an integer `x`, and a list of `n` integers `a_1, a_2, ..., a_n`. After processing all test cases, it returns a list of integers obtained from the user input, split and converted to integers.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and x such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30; and the third line is empty or contains additional input which should be ignored.
def func_2():
    return int(input())
    #The program returns an integer input by the user. This integer is the first input provided in the test case, following the pattern described in the initial state.
#Overall this is what the function does:The function reads an integer input from the user, which corresponds to the value of \( n \) from the first line of the test case. It then returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, representing the length of the array a and the favorite number x respectively. The next line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30, representing the array a itself.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing integers split from the input.
#Overall this is what the function does:The function processes input data for multiple test cases. For each test case, it reads integers t, n, x, and an array a, then returns a map object containing these integers split from the input.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. The following line contains a list of n integers representing the array a, where 0 ≤ a_i < 2^30.
def func_4():
    return input().strip()
    #The program returns a string containing the next input from the user, stripped of any leading or trailing whitespace.
#Overall this is what the function does:The function accepts no parameters and returns a string containing the next input from the user, stripped of any leading or trailing whitespace.

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
        
    #State: Output State: `t` is an empty list, `ans` is 14.
    #
    #Explanation: The loop iterates from 29 down to 0. The key logic in the loop involves checking bits of a list `a` and updating `ans` based on certain conditions. Since the loop iterates over each bit position and the final value of `ans` is set to the maximum count of consecutive zeros found in any bit position, and given the range of iteration (29 to 0), the maximum possible value for `ans` is half of the number of iterations, which is 14. The list `t` remains empty as no elements are appended to it during the loop's execution.
    return max(ans, len(a))
    #The program returns 14, which is the maximum count of consecutive zeros found in any bit position of the list `a`. The list `t` remains empty as no elements are appended to it during the loop's execution.
#Overall this is what the function does:The function takes a list `a` of `n` integers (each less than \(2^{30}\)) and an integer `x` (though `x` is not used in the function). It iterates through each bit position from 29 down to 0, checking for consecutive zeros in the bit positions of the integers in list `a`. It updates the variable `ans` to store the maximum count of consecutive zeros found across all integers in the list. The function ensures that a list `t` remains empty, as no elements are appended to it during the loop's execution. Finally, it returns the maximum count of consecutive zeros (`ans`).

