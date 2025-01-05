#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9.
def func_1():
    mod = 998244353
    n = int(input())
    l1 = list(input().split())
    arr = [0] * 10
    for item in l1:
        arr[len(item) - 1] += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 100,000; `l1` is a list of strings containing `n` strings; `arr[i]` is the count of strings of length `i + 1` for `i` from 0 to 9; `arr` reflects the distribution of string lengths in `l1`.
    ans = 0
    for item in l1:
        for i in range(1, 11):
            if arr[i - 1] == 0:
                continue
            x = len(item)
            res = 0
            if x <= i:
                for j in range(x - 1, -1, -1):
                    res = (res + int(item[j]) * pow(10, (x - j - 1) * 2, mod)) % mod
                    res = (res + int(item[j]) * pow(10, (x - j) * 2 - 1, mod)) % mod
                ans = ans + arr[i - 1] * res
            else:
                x -= 1
                i -= 1
                j = 0
                while x > i:
                    res = (res + 2 * int(item[j]) * pow(10, x - i + 2 * (i + 1) - 1,
                        mod)) % mod
                    x -= 1
                    j += 1
                i += 1
                x = len(item)
                for j in range(i - 1, -1, -1):
                    res = (res + int(item[j + (x - i)]) * pow(10, (i - j - 1) * 2, mod)
                        ) % mod
                    res = (res + int(item[j + (x - i)]) * pow(10, (i - j) * 2 - 1, mod)
                        ) % mod
                ans = ans + arr[i - 1] * res
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100,000; `l1` is a list of strings with `n` strings; `item` is the last string in `l1`; `ans` is the accumulated result of calculations based on all strings in `l1` and the contents of `arr`; `i` is 11; `x` is the length of the last string in `l1`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` and a list of `n` strings, where each string represents an integer. It calculates a result based on the lengths of these strings and their numerical values, using a specific modular arithmetic approach, and prints the accumulated result. The function handles strings of varying lengths and their distribution but does not explicitly validate the constraints on the values of `n` or the contents of the strings.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100000, and a_i are integers in the range 1 <= a_i <= 10^9 for i = 1 to n.
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        
        y = y >> 1
        
        x = x * x % p
        
    #State of the program after the loop has been executed: `y` is 0, `res` is the final result of the modular exponentiation of `x` raised to the original value of `y` modulo `p`, and `x` is the final value after all iterations of squaring and taking modulo `p`.
    return res
    #The program returns the final result of the modular exponentiation of x raised to the original value of 0 modulo p, which is 1, since any number raised to the power of 0 is 1.
#Overall this is what the function does:The function accepts three parameters: `x`, `y`, and `p`. It computes the modular exponentiation of `x` raised to the power of `y` modulo `p`, which means it calculates (x^y) % p. The function returns the result of this calculation. The annotations incorrectly state that it returns 1 when `y` is 0; however, this function will return the correct result for any valid positive integer values of `x`, `y`, and `p`. If `y` is 0, the function will still correctly compute the result modulo `p` as 1, since x^0 = 1 for any x.

#State of the program right berfore the function call: xs is a list of integers where each integer is between 1 and 10^9, and the length of xs is a positive integer n such that 1 <= n <= 100,000.
def count_next_smaller_elements(xs):
    ys = sorted((x, i) for i, x in enumerate(xs))
    zs = [0] * len(ys)
    for i in range(1, len(ys)):
        zs[ys[i][1]] = zs[ys[i - 1][1]]
        
        if ys[i][0] != ys[i - 1][0]:
            zs[ys[i][1]] += 1
        
    #State of the program after the  for loop has been executed: `zs` is a list where each element indicates the number of unique integers in `xs` up to the corresponding index in `ys`, `ys` is a sorted list of tuples containing each integer from `xs` paired with its original index, and `xs` is a list of integers.
    ts = [0] * (zs[ys[-1][1]] + 1)
    us = [0] * len(xs)
    for i in range(len(xs) - 1, -1, -1):
        x = zs[i] + 1
        
        while True:
            us[i] += ts[x - 1]
            x -= x & -x
            if x <= 0:
                break
            x = zs[i] + 1
        
        while True:
            x += x & -x
            if x > len(ts):
                break
            ts[x - 1] += 1
        
    #State of the program after the  for loop has been executed: `us` is a list updated with cumulative sums from `ts`, `ts` is a list reflecting counts based on the indices traversed, `i` is -1 after the loop completes, and `x` is less than or equal to 0 after all iterations.
    return us
    #The program returns the list 'us' which contains cumulative sums derived from the list 'ts' after the loop and considers that 'i' is -1 and 'x' is less than or equal to 0.
#Overall this is what the function does:The function accepts a list of integers `xs` and returns a list `us`, where each element at index `i` in `us` represents the count of how many integers in `xs` are smaller than the integer at index `i` in `xs`. This is achieved through sorting and cumulative counting, ensuring that the counts reflect the unique integers present in `xs`. The function handles lists of varying lengths (from 1 to 100,000) and integer values between 1 and 10^9, returning the appropriate cumulative counts based on the input.

#State of the program right berfore the function call: zero is an integer, and there exists an array of n integers a_i such that 1 ≤ n ≤ 100000 and 1 ≤ a_i ≤ 10^9.
def func_2(zero):
    conv = ord if py2 else lambda x: x
    A = []
    numb = zero
    sign = 1
    i = 0
    s = sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'0'[0]:
                numb = 10 * numb + conv(s[i]) - 48
            elif s[i] == b'-'[0]:
                sign = -1
            elif s[i] != b'\r'[0]:
                A.append(sign * numb)
                numb = zero
                sign = 1
            
            i += 1
            
        #State of the program after the loop has been executed: `i` is the length of `s`, `numb` contains the last number parsed from `s`, `sign` is either 1 or -1 depending on the last sign encountered, `A` contains all the parsed numbers with their respective signs, and `zero` remains an integer.
    except:
        pass
    #State of the program after the try-except block has been executed: `i` is the length of `s`, `numb` contains the last number parsed from `s`, `sign` is either 1 or -1 depending on the last sign encountered, `A` contains all the parsed numbers with their respective signs, and `zero` remains an integer. If an exception occurs, the program does nothing and exits the try block.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`i` is the length of `s`, `numb` contains the last number parsed from `s`, `sign` is either 1 or -1 depending on the last sign encountered, `A` contains all the parsed numbers with their respective signs including `sign * numb`, `zero` remains an integer, and `s` is a non-empty sequence where the last character of `s` is greater than or equal to the ASCII value of '0'.
    return A
    #The program returns the list A that contains all the parsed numbers from the sequence s, adjusted by their respective signs, including the last number parsed, numb, multiplied by sign.
#Overall this is what the function does:The function accepts an integer `zero` and reads a sequence of bytes, parsing integers from that sequence. It returns a list `A` containing all the parsed integers, adjusted by their respective signs (positive or negative). If the sequence ends with a valid number, that number is included in the list. The function handles potential exceptions during parsing but does not explicitly manage or report errors if the sequence is invalid.

