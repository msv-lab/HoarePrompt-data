#State of the program right berfore the function call: n is a positive integer (2 ≤ n ≤ 10^5), l1 is a list of n integers where each integer a_i satisfies -1 ≤ a_i ≤ 10^9, and at least one element in l1 is -1.
def func_1():
    for _ in range(int(input())):
        n = int(input())
        
        l1 = list(map(int, input().split()))
        
        temp = 0
        
        count = 0
        
        mini = -1
        
        maxi = -1
        
        for i in range(n):
            flag = 0
            if l1[i] == -1:
                continue
            if i > 0 and l1[i - 1] == -1:
                flag = 1
            if i < n - 1 and l1[i + 1] == -1:
                flag = 1
            if flag == 1:
                if mini == -1:
                    mini = l1[i]
                else:
                    mini = min(mini, l1[i])
                if maxi == -1:
                    maxi = l1[i]
                else:
                    maxi = max(maxi, l1[i])
        
        if mini == -1:
            k = 0
        else:
            k = (maxi + mini) // 2
        
        m = 0
        
        for i in range(n - 1):
            if l1[i + 1] == -1:
                l1[i + 1] = k
            if l1[i] == -1:
                l1[i] = k
            m = max(abs(l1[i + 1] - l1[i]), m)
        
        print(m, k)
        
    #State of the program after the  for loop has been executed: `n` is an input integer (2 ≤ n ≤ 10^5), `l1` is a list of `n` integers where any `-1` values are replaced with `k`, `temp` is 0, `count` is 0, `mini` is the minimum value among all elements in the original `l1` that are adjacent to a `-1` (or -1 if no such elements exist), `maxi` is the maximum value among all elements in the original `l1` that are adjacent to a `-1` (or -1 if no such elements exist), `k` is `(maxi + mini) // 2` if `mini` is not -1 otherwise `k` is 0, `m` is the maximum absolute difference between consecutive elements in the modified `l1`, and the values of `m` and `k` have been printed for each iteration of the outer loop.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each defined by an integer `n` (2 ≤ n ≤ 10^5) and a list `l1` of `n` integers where each integer `a_i` satisfies -1 ≤ a_i ≤ 10^9, and at least one element in `l1` is -1. For each test case, the function identifies the minimum (`mini`) and maximum (`maxi`) values among the elements in `l1` that are adjacent to a -1. It then calculates `k` as the integer division of the sum of `mini` and `maxi` by 2, or 0 if no such elements exist. The function replaces all -1 values in `l1` with `k` and computes `m`, the maximum absolute difference between consecutive elements in the modified list. Finally, the function prints `m` and `k` for each test case. After execution, the state of the program includes the modified list `l1` where -1 values have been replaced with `k`, and the values of `m` and `k` have been printed for each test case.

#State of the program right berfore the function call: zero is an integer set to 0, and s is a byte string representing a sequence of numbers and possibly a negative sign ('-'), where each number is separated by a non-digit character (excluding '\r').
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
            
        #State of the program after the loop has been executed: `zero` is 0, `s` is the byte string read from the standard input, `conv` is set to `ord` if `py2` is true, otherwise `conv` is a lambda function that returns its argument unchanged, `A` contains the signed numerical values parsed from `s`, `numb` is 0, `sign` is 1, `i` is the length of `s`.
    except:
        pass
    #State of the program after the try-except block has been executed: `zero` is 0, `s` is the byte string read from the standard input, `conv` is set to `ord` if `py2` is true, otherwise `conv` is a lambda function that returns its argument unchanged, `A` contains the signed numerical values parsed from `s` up to the point of the exception, `numb` is 0, `sign` is 1, and `i` is the index at which the exception occurred or the length of `s`.
    if (s and s[-1] >= b'0'[0]) :
        A.append(sign * numb)
    #State of the program after the if block has been executed: *`zero` is 0, `s` is the byte string read from the standard input, `conv` is set to `ord` if `py2` is true, otherwise `conv` is a lambda function that returns its argument unchanged, `A` contains the signed numerical values parsed from `s` up to the point of the exception, `numb` is 0, `sign` is 1, and `i` is the index at which the exception occurred or the length of `s`. If `s` is non-empty and the last character of `s` is greater than or equal to the ASCII value of '0', `A` now includes an additional 0.
    return A
    #The program returns `A`, which contains the signed numerical values parsed from `s` up to the point of the exception. If `s` is non-empty and the last character of `s` is greater than or equal to the ASCII value of '0', `A` includes an additional 0.
#Overall this is what the function does:The function `func_2` reads a byte string `s` from the standard input, which represents a sequence of numbers and possibly a negative sign ('-'), where each number is separated by a non-digit character (excluding '\r'). The function parses these numbers into signed integers and appends them to a list `A`. The function handles exceptions that occur during parsing, such as reaching the end of the string or encountering invalid characters. The final list `A` contains the signed numerical values parsed from `s` up to the point of any exception. If the last character of `s` is a digit, the function ensures that the corresponding number is included in `A`. The function returns the list `A`.

### Edge Cases and Missing Functionality:
-

