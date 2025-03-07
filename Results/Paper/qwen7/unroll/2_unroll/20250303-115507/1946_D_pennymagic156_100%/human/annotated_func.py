#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three lines: the first line contains two integers n and x such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30; the second line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30; the input format for each test case follows the structure described in the problem statement.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from the input split and mapped to integers.
#Overall this is what the function does:The function reads three lines of input from the standard input. The first line contains two integers \( n \) and \( x \), where \( 1 \leq n \leq 10^5 \) and \( 0 \leq x < 2^{30} \). The second line contains \( n \) integers \( a_1, a_2, \ldots, a_n \), each satisfying \( 0 \leq a_i < 2^{30} \). The function then converts the second line into a list of integers and returns this list.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. The following line contains a list of n integers a, where 0 ≤ a_i < 2^30.
def func_2():
    return int(input())
    #The program returns an integer input provided by the user, which represents the number of test cases.
#Overall this is what the function does:The function reads an integer input from the user, which represents the number of test cases, and returns this integer. This integer will be used to determine how many times subsequent operations (not defined in this function) should be repeated.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. Additionally, the subsequent line contains n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_3():
    return map(int, input().split())
    #The program returns a map object containing integers parsed from the input. The input consists of multiple lines, where the first line contains an integer t representing the number of test cases. Each subsequent line starts with an integer n and an integer x, followed by n integers a_1, a_2, ..., a_n.
#Overall this is what the function does:The function processes input data consisting of multiple lines, where the first line contains an integer t representing the number of test cases. For each test case, it reads two integers n and x, followed by n integers a_1, a_2, ..., a_n. The function returns a map object containing these integers parsed from the input.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and for each test case, n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30. Additionally, the subsequent lines contain n integers a_1, a_2, ..., a_n such that 0 ≤ a_i < 2^30.
def func_4():
    return input().strip()
    #The program returns the first line of input after stripping any leading or trailing whitespace. This line represents the number of test cases, t.
#Overall this is what the function does:The function reads the first line of input, strips any leading or trailing whitespace, and returns this value as the number of test cases, t.

#State of the program right berfore the function call: (n, x) is a tuple of two integers where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, and a is a list of n integers where each integer satisfies 0 ≤ a_i < 2^30.
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
        
    #State: Output State: `n` is a value returned by `func_3()`, `x` is a value returned by `func_3()`, and `a` is a value returned by `func_1()`, `t` is an empty list, `ans` is the maximum count of consecutive 1s found during the loop execution.
    #
    #To explain in natural language: After the loop completes all its iterations, the variable `n` retains its initial value, `x` retains its initial value, and `a` retains its initial value. The list `t` remains empty as it is reset to an empty list at the end of each inner loop iteration where `a` is modified. The variable `ans` holds the maximum count of consecutive 1s found during the loop execution.
    return max(ans, len(a))
    #The program returns the maximum count of consecutive 1s found during the loop execution, which is either `max(ans, len(a))`.
#Overall this is what the function does:The function accepts a tuple `(n, x)` where `n` is an integer between 1 and 10^5 inclusive, and `x` is an integer less than 2^30. It also accepts a list `a` of `n` integers, where each integer in the list is less than 2^30. The function iterates over the bits from the most significant to the least significant, checking the parity of the bit in `x` and the sum of the corresponding bits in `a`. Based on these values, it updates a counter `ans` to store the maximum count of consecutive 1s found during the loop execution. If certain conditions are met, it modifies the list `a` and resets the counter. Finally, the function returns the maximum count of consecutive 1s found, which is the greater of `ans` and the length of the list `a`.

