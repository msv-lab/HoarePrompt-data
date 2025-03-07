#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters. It reads input from the standard input and returns a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from the user input, where each input value is converted to an integer.
#Overall this is what the function does:`func_1` does not accept any parameters. It reads a line of input from the standard input, splits the input into individual values, converts each value to an integer, and returns a list of these integers. The function affects the program state by returning this list, which can then be used by the calling code.

#State of the program right berfore the function call: None
def func_2():
    return int(input())
    #The program returns an integer value that the user inputs.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value that the user inputs. The state of the program after the function concludes is that it has obtained an integer from the user, which can be used in further computations or operations.

#State of the program right berfore the function call: None of the variables are used in the function signature. The function reads input from the standard input, expecting a line of space-separated integers.
def func_3():
    return map(int, input().split())
    #The program returns a map object that contains the integers obtained from the space-separated input provided by the user.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of space-separated integers from the standard input and returns a map object containing these integers. The map object can be iterated over to access the integers.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_4():
    return input().strip()
    #The program returns the input string after removing any leading and trailing whitespace.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string obtained from user input after removing any leading and trailing whitespace.

#State of the program right berfore the function call: n and x are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < 2^30.
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
        
    #State: `n` and `x` are unchanged, `a` is an empty list, `t` is an empty list, `ans` is the maximum count of integers in `a` that have the same bit set at the highest position where `x` has a 0 bit and the sum of the bits at that position in `a` is even.
    return max(ans, len(a))
    #The program returns the maximum value between `ans` and the length of the list `a`. Since `a` is an empty list, its length is 0. `ans` is the maximum count of integers in `a` that have the same bit set at the highest position where `x` has a 0 bit and the sum of the bits at that position in `a` is even. However, since `a` is empty, `ans` must be 0. Therefore, the program returns 0.
#Overall this is what the function does:The function `func_5` does not accept any parameters. It returns the maximum count of integers in the list `a` that have the same bit set at the highest position where `x` has a 0 bit and the sum of the bits at that position in `a` is even. If no such integers exist or if the list `a` is empty after processing, the function returns 0. The function modifies the list `a` and `t` during its execution, but both lists are empty by the time the function concludes. The values of `n` and `x` remain unchanged.

