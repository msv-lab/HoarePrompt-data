#State of the program right berfore the function call: None
def func_1():
    return list(map(int, input().split()))
    #The program returns a list of integers converted from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns a list of integers. The integers are derived from a space-separated string input by the user. After the function concludes, the program has a list of integers that were converted from the input string.

#State of the program right berfore the function call: None. This function does not take any parameters and is designed to read an integer input from the user.
def func_2():
    return int(input())
    #The program returns an integer value that the user inputs.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer value from the user and returns this integer value. After the function concludes, the program has returned the integer input by the user.

#State of the program right berfore the function call: None. This function does not take any parameters.
def func_3():
    return map(int, input().split())
    #The program returns an iterator that yields integer values from the input provided by the user, which is split into separate strings based on spaces.
#Overall this is what the function does:The function `func_3` does not accept any parameters. It reads a line of input from the user, splits the input into separate strings based on spaces, converts each string into an integer, and returns an iterator that yields these integer values. After the function concludes, the program has an iterator ready to yield integer values from the user's input.

#State of the program right berfore the function call: None of the variables are passed to the function `func_4`. This function is designed to read input from the standard input stream and strip any leading or trailing whitespace.
def func_4():
    return input().strip()
    #The program returns a string that is the input provided by the user, with any leading or trailing whitespace removed.
#Overall this is what the function does:The function `func_4` reads a string from the standard input, removes any leading or trailing whitespace from the string, and returns the cleaned string.

#State of the program right berfore the function call: n is a positive integer representing the length of the array a, x is a non-negative integer less than \(2^{30}\), and a is a list of n non-negative integers, each less than \(2^{30}\).
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
        
    #State: `n` and `x` are updated to the values returned by `func_3()`, `a` is a list of `n` non-negative integers, each less than \(2^{30}\), `t` is an empty list, `ans` is the maximum count of elements in `a` whose bits contributed to making `op` 0 at some point during the loop, and `i` is -1.
    return max(ans, len(a))
    #The program returns the maximum value between `ans` and the length of list `a`. Here, `ans` is the maximum count of elements in `a` whose bits contributed to making `op` 0 at some point during the loop, and `a` is a list of `n` non-negative integers, each less than \(2^{30}\).
#Overall this is what the function does:The function `func_5` processes a list `a` of `n` non-negative integers, each less than \(2^{30}\), and an integer `x` also less than \(2^{30}\). It iterates over the bits of the numbers in `a` and `x` from the 29th bit down to the 0th bit. Depending on the bit values, it either continues, returns `-1`, or updates a list `t` and a variable `ans`. The function ultimately returns the maximum value between `ans` and the length of `a`. `ans` represents the maximum count of elements in `a` whose bits contributed to making a bitwise operation result 0 during the loop. If certain conditions are met (e.g., `v` is 0 or odd), the function may return `-1` before completing the loop.

