#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers represented as strings where 1 <= len(x) = len(y) <= 100, and each digit in x and y is between 1 and 9 (inclusive).
def func():
    t = int(input())
    for q in range(t):
        a = input()
        
        b = input()
        
        kq1 = ''
        
        kq2 = ''
        
        vt = 0
        
        for i in range(len(a)):
            if a[i] == b[i]:
                kq1 = kq1 + a[i]
                kq2 = kq2 + a[i]
                continue
            else:
                x, y = min(int(a[i]), int(b[i])), max(int(a[i]), int(b[i]))
                if vt == 0:
                    vt = 1
                    if a[i] > b[i]:
                        kq1 = kq1 + str(x)
                        kq2 = kq2 + str(y)
                    else:
                        kq1 = kq1 + str(y)
                        kq2 = kq2 + str(x)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: `t` is an integer such that 1 <= t <= 1000; `a` and `b` are strings provided by user input for each iteration; `kq1` is a string constructed based on the maximum of `a[i]` and `b[i]` for each index `i` where `a[i] != b[i]` and `a[i]` if `a[i] == b[i]`; `kq2` is a string constructed based on the minimum of `a[i]` and `b[i]` for each index `i` where `a[i] != b[i]` and `a[i]` if `a[i] == b[i]`; `vt` is 1 if there was at least one inequality between characters in `a` and `b` in the current iteration, otherwise 0; `q` is incremented by 1 for each iteration, reaching `t` after all iterations; the loop has executed `t` times, and for each execution, it prints `kq1` and `kq2`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two strings `x` and `y` of equal length, where each character is a digit from 1 to 9. For each test case, it constructs two new strings: one where each digit is the maximum of the corresponding digits from `x` and `y` (with the first differing digit being the larger of the two), and another where each digit is the minimum of the corresponding digits from `x` and `y` (with the first differing digit being the smaller of the two). It then prints these two strings for each test case.

