#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers for each test case where 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: `t` is greater than 0, `q` is `t - 1`, `x` and `y` are integers where 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9, `a` and `b` are input strings with the same length, `i` is `len(a) - 1`, `vt` is 0 or 1, `kq1` and `kq2` are strings of the same length as `a` and `b` where each character is determined by the rules specified in the loop. If `a[i]` == `b[i]` for any `i`, the corresponding character in `kq1` and `kq2` is `a[i]`. If `a[i]` != `b[i]`, the corresponding character in `kq1` and `kq2` is either the smaller or larger of `a[i]` and `b[i]` based on the value of `vt` and the conditions in the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two strings `a` and `b` from the input, where each string consists of digits from 1 to 9. The function then generates two strings `kq1` and `kq2` of the same length as `a` and `b`. For each character position `i` in `a` and `b`, if the characters are the same, `kq1` and `kq2` will have the same character at position `i`. If the characters are different, the first differing character in `kq1` and `kq2` will be the smaller and larger of the two characters, respectively, and subsequent differing characters will be swapped. The function prints `kq1` and `kq2` for each test case. The function does not return any value.

