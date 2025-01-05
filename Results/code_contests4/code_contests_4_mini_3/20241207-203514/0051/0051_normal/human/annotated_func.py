#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a_i are integers such that 1 ≤ a_i ≤ 10^9 for i in range(1, n).
def func_1():
    mod = 998244353
    n = int(input())
    l1 = list(input().split())
    arr = [0] * 10
    for item in l1:
        arr[len(item) - 1] += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100,000; `l1` is a list of strings with `n` strings; `arr` is a list containing the count of strings of lengths 1 to 10; `arr[i]` is the number of strings in `l1` of length `i + 1` for `i` in range(10).
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100,000; `l1` is a list of strings with `n` strings; `ans` is the accumulated result based on the calculations from all strings in `l1`; `i` is 10 at the end of the last string processed; `x` is the length of the last string in `l1`; `res` contains the final computed value based on the characters of the last string processed during the loop.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, reads `n` strings from input, and calculates a result based on the lengths of these strings and their numeric values. The result is accumulated in the variable `ans`, which is printed at the end. The specific logic involves counting how many strings have each length from 1 to 10 and performing calculations involving powers of 10 modulo 998244353 based on these counts and the numeric values of the strings. The function does not return any value, but it outputs the final accumulated result directly.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100,000, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        
        y = y >> 1
        
        x = x * x % p
        
    #State of the program after the loop has been executed: `y` is 0, `res` is the value computed based on the initial `x` and `p` for all corresponding bits of the original `y`, `x` is the last computed value of `x * x % p` before the loop exits.
    return res
    #The program returns the value of 'res' which is computed based on the initial 'x' and 'p' for all corresponding bits of 'y' that is currently 0
#Overall this is what the function does:The function accepts three parameters: integers `x`, `y`, and `p`, and returns the result of calculating `(x^y) % p` using an efficient method called exponentiation by squaring. It handles large values of `y` and ensures that intermediate results remain within the modulo `p`.

#State of the program right berfore the function call: xs is a list of integers where each integer is between 1 and 10^9, and the length of xs is a positive integer n such that 1 <= n <= 100,000.
def count_next_smaller_elements(xs):
    ys = sorted((x, i) for i, x in enumerate(xs))
    zs = [0] * len(ys)
    for i in range(1, len(ys)):
        zs[ys[i][1]] = zs[ys[i - 1][1]]
        
        if ys[i][0] != ys[i - 1][0]:
            zs[ys[i][1]] += 1
        
    #State of the program after the  for loop has been executed: `zs` is a list where each entry corresponds to the count of distinct integers from `xs` at each index of `ys`; `ys` is a sorted list of tuples containing integers from `xs` and their corresponding indices.
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
        
    #State of the program after the  for loop has been executed: `us` is a list containing the cumulative sums of counts from `ts` corresponding to the indices defined by `zs`, `ts` is a list that contains the counts of occurrences based on the values in `zs`, `zs` and `ys` remain unchanged, `i` is -1 indicating that all iterations of the loop have completed.
    return us
    #The program returns the list 'us' containing the cumulative sums of counts from 'ts' corresponding to the indices defined by 'zs'
#Overall this is what the function does:The function accepts a list of integers `xs` where each integer is between 1 and \(10^9\) and the length of `xs` is a positive integer between 1 and 100,000. It returns a list `us` such that each entry in `us` represents the cumulative count of smaller distinct integers from `xs` that are to the right of each corresponding element in the original list `xs`. The function handles distinct integers and their counts effectively, but does not account for cases where all elements in `xs` are the same, which would result in all entries in `us` being zero.

#State of the program right berfore the function call: zero is a non-negative integer. The function calculates the sum of f(a_i, a_j) for all pairs (i, j) where a_i and a_j are integers in the input array, and each a_i is within the range 1 to 10^9.
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
            
        #State of the program after the loop has been executed: `conv` is assigned a function based on `py2`, `A` contains the integers parsed from the input `s` (excluding the negative sign and carriage return), `numb` is `zero`, `sign` is 1, and `i` is equal to the length of `s`.
    except:
        pass
    #State of the program after the try-except block has been executed: `conv` is assigned a function based on `py2`, `A` contains the integers parsed from the input `s` (excluding the negative sign and carriage return), `numb` is `zero`, `sign` is 1, and `i` is equal to the length of `s`.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`conv` is a function based on `py2`, `A` contains the integers parsed from the input `s`, `numb` is 0, `sign` is 1, and `i` is equal to the length of `s`. If `s` is not empty and the last character of `s` is greater than or equal to the ASCII value of '0', then 0 is appended to `A`.
    return A
    #The program returns the list A that contains integers parsed from the input s, and if s is not empty and the last character of s is greater than or equal to the ASCII value of '0', then 0 is appended to A.
#Overall this is what the function does:The function accepts a non-negative integer `zero` and reads a byte string from standard input, parsing integers from it while handling negative signs and carriage returns. It constructs a list `A` of these integers, and if the last byte in the input is a numeric character, it appends the integer `0` to the list before returning it. The function does not handle cases where the input may not contain any integers, which could lead to returning an empty list.

