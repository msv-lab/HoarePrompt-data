#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100000, and a_i are integers such that 1 <= a_i <= 10^9 for each i in range(1, n).
def func_1():
    mod = 998244353
    n = int(input())
    l1 = list(input().split())
    arr = [0] * 10
    for item in l1:
        arr[len(item) - 1] += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 100000; `l1` is a list of strings with `n` strings; `arr[i]` contains the count of strings of length `i + 1` for i in range(10), where `arr` has been modified accordingly based on the lengths of the strings in `l1`.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l1` is a list of strings with `n` strings, `item` is the last string in `l1`, `ans` is the accumulated result based on the calculations performed for all iterations of `i` from 1 to 10 for each string in `l1`, `x` is the length of the last `item`, and `res` reflects the cumulative computed values based on the characters in the last `item` across all iterations.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` from user input, reads `n` strings, and calculates a result based on the lengths of these strings and their character values. It counts the number of strings of different lengths (up to 10), and for each string, it performs a series of calculations involving modular exponentiation and accumulates a final result, which it prints. The function does not return a value but outputs the computed result directly.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100000, and a is a list of n integers where each integer a_i is in the range 1 <= a_i <= 10^9.
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        
        y = y >> 1
        
        x = x * x % p
        
    #State of the program after the loop has been executed: `y` is 0, `res` is the result of the modular exponentiation of `x` raised to the original value of `y` modulo `p`, `x` is updated to a final value after processing all iterations.
    return res
    #The program returns the result of the modular exponentiation of x raised to the value of 0 modulo p, which is 1.
#Overall this is what the function does:The function accepts three parameters: `x`, `y`, and `p`. It performs modular exponentiation to compute (x^y) mod p. If y is 0, it returns 1, which is consistent with the mathematical rule that any number raised to the power of 0 equals 1. Otherwise, it returns the result of x raised to the power of y modulo p. The function efficiently computes the result using an iterative method that reduces the exponent y by half in each iteration.

#State of the program right berfore the function call: xs is a list of integers where each integer is between 1 and 10^9, and the length of xs is a positive integer n such that 1 ≤ n ≤ 100,000.
def count_next_smaller_elements(xs):
    ys = sorted((x, i) for i, x in enumerate(xs))
    zs = [0] * len(ys)
    for i in range(1, len(ys)):
        zs[ys[i][1]] = zs[ys[i - 1][1]]
        
        if ys[i][0] != ys[i - 1][0]:
            zs[ys[i][1]] += 1
        
    #State of the program after the  for loop has been executed: `xs` is a list of integers where each integer is between 1 and 10^9, `n` is a positive integer representing the length of `xs`, `ys` is a sorted list of tuples containing each integer from `xs` paired with its index, and `zs` contains the counts of unique integers from `xs` corresponding to their original indices in `xs`.
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
        
    #State of the program after the  for loop has been executed: `us` contains the cumulative sums based on the counts in `ts`, `ts` holds the counts of unique integers updated during the iterations, and `xs` is a list of integers.
    return us
    #The program returns the cumulative sums stored in 'us' based on the counts in 'ts', which holds the counts of unique integers updated during the iterations
#Overall this is what the function does:The function accepts a list of integers `xs` and returns a list of cumulative sums based on the counts of unique integers in `xs`. The cumulative sums are calculated in a manner that accounts for the frequencies of each unique integer, providing an updated count for each index in the original list. The function is designed to handle up to 100,000 integers, each ranging from 1 to 10^9.

#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100000, and a_i are integers such that 1 <= a_i <= 10^9 for each element in the array.
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
            
        #State of the program after the loop has been executed: `n` is a positive integer such that 1 <= `n` <= 100000; `A` contains the integers extracted from the input `s` as per the logic in the loop; `numb` is zero; `sign` is 1; `i` is equal to the length of `s`.
    except:
        pass
    #State of the program after the try-except block has been executed: `n` is a positive integer such that 1 <= `n` <= 100000; `A` contains the integers extracted from the input `s` as per the logic in the loop; `numb` is zero; `sign` is 1; `i` is equal to the length of `s.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 <= `n` <= 100000; `A` contains the integers extracted from the input `s` and now includes a 0, `numb` is zero, `sign` is 1, `i` is equal to the length of `s`, and `s` is not empty with the last element of `s` being greater than or equal to the ASCII value of '0'.
    return A
    #The program returns the list A containing integers extracted from the input s, which includes a 0.
#Overall this is what the function does:The function accepts a positive integer `zero` and returns a list of integers extracted from the input string `s`, which includes a 0. The function processes the input to convert sequences of numeric characters into integers, handles negative signs, and concatenates the results into the list `A`. It also includes the last number processed if the input ends with a digit. If the input is empty, the function will return an empty list.

