#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. The length of x and y is the same for each test case.
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
        
    #State: After all iterations, `a`, `b`, `kq1`, `kq2`, and `vt` will reflect the state after processing the last test case. Specifically, `a` and `b` will contain the last input strings, `kq1` and `kq2` will contain the final derived strings for the last test case, and `vt` will be 0 if the last test case did not have any differing digits or 1 if it did.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two strings `x` and `y` of the same length, with digits ranging from 1 to 9. For each test case, it generates two new strings `kq1` and `kq2` by comparing corresponding digits of `x` and `y`. If the digits are the same, they are added to both `kq1` and `kq2`. If the digits differ, the smaller digit is added to `kq1` and the larger digit is added to `kq2` for the first occurrence of a difference, and then the opposite for subsequent differences. The function prints `kq1` and `kq2` for each test case.

