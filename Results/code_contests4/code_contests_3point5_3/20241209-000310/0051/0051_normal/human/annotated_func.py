#State of the program right berfore the function call: **
def func_1():
    mod = 998244353
    n = int(input())
    l1 = list(input().split())
    arr = [0] * 10
    for item in l1:
        arr[len(item) - 1] += 1
        
    #State of the program after the  for loop has been executed: `mod` is 998244353, `n` is an input integer, `l1` is a list of elements, `arr` is a list with 10 elements where each element represents the count of elements in `l1` with a specific length
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
        
    #State of the program after the  for loop has been executed: `mod` is 998244353, `n` is an input integer, `l1` is a list of elements with at least 1 element, `arr` is a list with 10 elements, `ans` is the final calculated value after all iterations of the loop, `item` is the last element in `l1`, `i` is 10, `x` is the length of the last element in `l1`, `res` contains the final computed value after all iterations of the loop, `j` is either -1 or -10 based on the condition
    print(ans)
#Overall this is what the function does:The function `func_1` initializes variables and performs calculations based on the input provided by the user. It calculates a final value `ans` by iterating over elements in the input list `l1`. The function does not accept any parameters and does not return any output.

#State of the program right berfore the function call: **n is a positive integer. The elements in the array a_i are positive integers less than or equal to 10^9.
def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        
        y = y >> 1
        
        x = x * x % p
        
    #State of the program after the loop has been executed: `res`, `x`, and `p` are integers. The final value of `res` is calculated based on the conditions inside the loop. `y` is 0 after the loop finishes executing.
    return res
    #The program returns the final value of integer 'res' after the loop execution. The integer 'y' is 0 after the loop finishes executing.
#Overall this is what the function does:The function power accepts three parameters x, y, and p. It performs a loop operation where it calculates the value of res based on the conditions inside the loop. The final result of res is returned after the loop finishes executing, and the integer y is guaranteed to be 0 at the end of the function execution.

#State of the program right berfore the function call: **
def count_next_smaller_elements(xs):
    ys = sorted((x, i) for i, x in enumerate(xs))
    zs = [0] * len(ys)
    for i in range(1, len(ys)):
        zs[ys[i][1]] = zs[ys[i - 1][1]]
        
        if ys[i][0] != ys[i - 1][0]:
            zs[ys[i][1]] += 1
        
    #State of the program after the  for loop has been executed: `ys` is a sorted list of tuples where each tuple contains an element from `xs` and its index with at least 2 elements, `zs` is a list of zeros with the same length as `ys` with at least 2 zeros where the value at index `ys[i][1]` is updated to match the value at index `ys[i - 1][1]` for all `i` in the range from 1 to len(ys). If the element at index `i` in `ys` is not equal to the element at index `i - 1`, the value at index `ys[i][1]` in `zs` is incremented by 1 for all `i` in the range from 1 to len(ys).
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
        
    #State of the program after the  for loop has been executed: `ys` is a sorted list of tuples where each tuple contains an element from `xs` and its index, `zs` has been updated with the new values at each index, `ts` has been updated based on the conditions inside the loop, `us` has been updated such that each element has been incremented by the cumulative sum of `ts[x - 1]` for all iterations of the loop, the loop has finished executing
    return us
    #The program returns the list `us` where each element has been incremented by the cumulative sum of `ts[x - 1]` for all iterations of the loop
#Overall this is what the function does:The function `count_next_smaller_elements` takes a list `xs` as a parameter. It sorts the elements of `xs` along with their indices and then performs calculations to modify elements in a new list `us`. Each element in `us` is incremented by the cumulative sum of certain values calculated during the execution of the function. The function returns the modified list `us`.

#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100,000 and a_i is an integer such that 1 <= a_i <= 10^9 for 1 <= i <= n.**
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
            
        #State of the program after the loop has been executed: `n` is an integer such that 1 <= n <= 100,000, `a_i` is an integer such that 1 <= a_i <= 10^9 for 1 <= i <= n, `conv` is assigned the function `ord` if Python version is 2, otherwise, it is assigned a lambda function, `A` contains the appended values of sign * numb based on the conditions met during each iteration of the loop, `numb` is the final value after all calculations, `sign` is the final value after all calculations, `i` is the index of the last character in string `s` after the loop finishes execution.
    except:
        pass
    #State of the program after the try-except block has been executed: `n` is an integer such that 1 <= n <= 100,000, `a_i` is an integer such that 1 <= a_i <= 10^9 for 1 <= i <= n, `conv` is assigned the function `ord` if Python version is 2, otherwise, it is assigned a lambda function, `A` contains the appended values of sign * numb based on the conditions met during each iteration of the loop, `numb` is the final value after all calculations, `sign` is the final value after all calculations, `i` is the index of the last character in string `s` after the loop finishes execution.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 <= n <= 100,000, `a_i` is an integer such that 1 <= a_i <= 10^9 for 1 <= i <= n, `conv` is a function, `A` contains appended values based on conditions met during iterations, `numb` is the final value after calculations, `sign` is the final value after calculations, `i` is the index of the last character in string `s`. If `s` is not empty and the last character is greater than or equal to '0', then the program updates the variables `A`, `numb`, `sign`, and `i` based on certain conditions.
    return A
    #The program returns the list `A` containing appended values based on conditions met during iterations
#Overall this is what the function does:The function accepts an integer n and reads a string from stdin. It then iterates through the string, parsing integers based on specific conditions, and appends them to a list A. The function returns the list A containing the parsed integers. If the string s is not empty and the last character is a digit, it appends the last parsed integer to A. The function handles the conversion function based on the Python version.

