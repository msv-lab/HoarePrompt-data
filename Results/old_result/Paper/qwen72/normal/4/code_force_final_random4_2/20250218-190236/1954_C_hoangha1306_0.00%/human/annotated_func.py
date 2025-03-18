#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, x and y are integers for each test case where 1 <= x < 10^100 and 1 <= y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: `t` is an input integer such that 1 <= t <= 1000, `q` is `t - 1`, `a` and `b` are the original input strings, `vt` is 0 or 1, `kq1` is a string that represents the result of the loop's logic for the first condition, and `kq2` is a string that represents the result of the loop's logic for the second condition.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer such that 1 <= t <= 1000. For each test case, it takes two input strings `a` and `b` (each representing an integer with digits from 1 to 9 and lengths up to 100). It then generates two strings `kq1` and `kq2` by comparing corresponding digits of `a` and `b`. If the digits are the same, they are added to both `kq1` and `kq2`. If the digits are different, the smaller digit is added to `kq1` and the larger digit is added to `kq2` for the first differing digit, and the opposite for subsequent differing digits. Finally, it prints `kq1` and `kq2` for each test case.

