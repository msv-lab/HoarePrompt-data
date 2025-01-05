#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100,000, and a_i are positive integers such that 1 <= a_i <= 10^9 for each i from 1 to n.
def func_1():
    mod = 998244353
    n = int(input())
    l1 = list(input().split())
    arr = [0] * 10
    for item in l1:
        arr[len(item) - 1] += 1
        
    #State of the program after the  for loop has been executed: `arr` contains the counts of strings of lengths from 1 to 10 from the list `l1`, `n` is a positive integer such that 1 <= `n` <= 100,000, `mod` is 998244353, `l1` is a list of strings.
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
        
    #State of the program after the  for loop has been executed: `arr` contains counts of strings of lengths from 1 to 10; `n` is a positive integer between 1 and 100,000; `mod` is 998244353; `l1` is a non-empty list of strings; `ans` is updated to the final accumulated result based on the calculations performed for all string lengths; `i` is 11; `j` is the index of the last character processed from the last item; `x` is the length of the last item processed in `l1`; `res` is the final calculated result based on all iterations of `item`.
    print(ans)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings from input. It counts the occurrences of strings by their lengths (up to 10) and calculates a result based on specific mathematical operations involving the digits of these strings and modular arithmetic. The final accumulated result is printed, but the specifics of how this result is derived may depend on the values of the strings provided. The function does not handle cases where the input does not conform to the specified constraints (e.g., if `n` is less than 1 or greater than 100,000, or if the strings have lengths greater than 10).

#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and a_i are integers such that 1 ≤ a_i ≤ 10^9 for i = 1, 2, ..., n.
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        
        y = y >> 1
        
        x = x * x % p
        
    #State of the program after the loop has been executed: `y` is 0, `res` is updated to `x` raised to the power of the original value of `y` modulo `p`, `x` is the final value of `x` after being squared repeatedly, and `n` remains a positive integer such that 1 ≤ `n` ≤ 100,000; `a_i` are integers such that 1 ≤ `a_i` ≤ 10^9.
    return res
    #The program returns the result of `x` raised to the power of 0 modulo `p`, which is 1
#Overall this is what the function does:The function accepts three parameters: `x`, `y`, and `p`. It calculates and returns the result of `x` raised to the power of `y` modulo `p`. The final result is computed through an efficient algorithm that handles large exponents using modular arithmetic.

#State of the program right berfore the function call: xs is a list of integers where each integer is in the range 1 to 10^9, and the length of xs is between 1 and 100,000.
def count_next_smaller_elements(xs):
    ys = sorted((x, i) for i, x in enumerate(xs))
    zs = [0] * len(ys)
    for i in range(1, len(ys)):
        zs[ys[i][1]] = zs[ys[i - 1][1]]
        
        if ys[i][0] != ys[i - 1][0]:
            zs[ys[i][1]] += 1
        
    #State of the program after the  for loop has been executed: `xs` is a list of integers, `ys` is a sorted list of tuples (value, index) from `xs`, `zs` is a list where each element represents the count of distinct values from `xs` corresponding to the indices in `ys`.
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
        
    #State of the program after the  for loop has been executed: `us` contains the cumulative counts derived from `ts` for each index of `xs`, and `ts` contains the frequencies of the distinct values from `zs` up to the maximum index.
    return us
    #The program returns the cumulative counts stored in 'us' derived from the frequencies in 'ts' for each index of 'xs'
#Overall this is what the function does:The function accepts a list of integers `xs` and returns a list of counts where each count at index `i` represents the number of distinct integers in `xs` that are smaller than the integer at index `i`. The function handles the case where all elements are the same by returning zero counts for all indices. It is efficient for large lists, as it utilizes sorting and binary indexed trees for cumulative frequency calculations.

#State of the program right berfore the function call: zero is an integer, and the function takes no other parameters; it assumes the existence of an array consisting of n integers a_i, where 1 ≤ n ≤ 100,000 and 1 ≤ a_i ≤ 10^9.
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
            
        #State of the program after the loop has been executed: `conv` is assigned based on `py2`, `A` contains the accumulated values derived from the input `s`, `numb` is 0, `sign` is 1, `i` is equal to the length of `s`, and the loop terminates when all characters of `s` are processed.
    except:
        pass
    #State of the program after the try-except block has been executed: `conv` is assigned based on `py2`, `A` contains the accumulated values derived from the input `s`, `numb` is 0, `sign` is 1, `i` is equal to the length of `s`, and the loop terminates when all characters of `s` are processed.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`conv` is assigned based on `py2`, `A` contains the accumulated values derived from the input `s` which now includes 0, `numb` is 0, `sign` is 1, `i` is equal to the length of `s`, and the loop continues until all characters of `s` are processed if `s` is non-empty and the last character of `s` is greater than or equal to the ASCII value of '0'.
    return A
    #The program returns the accumulated values in A derived from the input s, which includes 0.
#Overall this is what the function does:The function accepts an integer `zero` and processes a byte string input `s` to extract integers based on specific delimiters (including the '-' sign for negative numbers). It accumulates these integers into a list `A`, which is then returned. The function handles potential input errors by using a try-except block to continue processing until all characters are read, but it does not explicitly handle cases where the input string could be malformed or empty. The final list may include zero if the input ends with a numeric character.

