#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters. It reads input from the standard input and returns a list of integers.
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers obtained from the user input, where each input item is converted to an integer and split by spaces.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits the input into items by spaces, converts each item to an integer, and returns a list of these integers. The function does not accept any parameters and does not modify any external variables. After the function concludes, the program has a list of integers derived from the user input.

#State of the program right berfore the function call: None. This function does not take any parameters.
def func_2():
    return int(input())
    #The program returns an integer value that is input by the user.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an integer value provided by the user. After the function concludes, the program state includes the returned integer, which is the user's input converted to an integer.

#State of the program right berfore the function call: None of the variables are passed to the function, as it reads input directly.
def func_3():
    return map(int, input().split())
    #The program returns a map object that converts each element from the input (which is split by spaces) into an integer.
#Overall this is what the function does:The function `func_3` reads a line of input from the user, which is expected to be a string of numbers separated by spaces. It then returns a map object that converts each of these numbers into integers. The map object can be iterated over to access the converted integers.

#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_4():
    return input().strip()
    #The program returns the input string with leading and trailing whitespace removed.
#Overall this is what the function does:The function `func_4` does not accept any parameters and returns a string with leading and trailing whitespace removed, obtained from user input.

#State of the program right berfore the function call: n and x are integers where 1 ≤ n ≤ 10^5 and 0 ≤ x < 2^30, and a is a list of n integers where 0 ≤ a_i < 2^30.
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
        
    #State: `n` and `x` are unchanged, `a` is a modified list of integers, `t` is an empty list, `ans` is the maximum value of `cnt` encountered during the iterations where `u == 1` and `v % 2 == 0`.
    return max(ans, len(a))
    #The program returns the maximum value between `ans` and the length of the modified list `a`. `ans` is the maximum value of `cnt` encountered during the iterations where `u == 1` and `v % 2 == 0`. The length of `a` is the number of elements in the modified list `a`.
#Overall this is what the function does:The function `func_5` accepts no parameters and returns an integer. It operates on an integer `n`, an integer `x`, and a list `a` of `n` integers, which are obtained internally through calls to `func_3` and `func_1`. The function modifies the list `a` and returns the maximum value between `ans` and the length of the modified list `a`. `ans` is the maximum count of elements in `a` that have a specific bit pattern, encountered during the iterations where the i-th bit of `x` is 1 and the sum of the i-th bits of the elements in `a` is even. The function does not change the values of `n` and `x`, but `a` is modified during the process.

