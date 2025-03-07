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
        
    #State: For each test case, the loop outputs two strings, `kq1` and `kq2`, which are derived from the input strings `a` and `b`. The strings `kq1` and `kq2` are constructed such that for each position where `a` and `b` have the same digit, `kq1` and `kq2` will have that same digit. For positions where `a` and `b` differ, the first differing position will be handled such that the smaller digit is placed in `kq1` and the larger digit in `kq2` if `vt` is 0. For all subsequent differing positions, the larger digit is placed in `kq1` and the smaller digit in `kq2`. The variables `t`, `x`, and `y` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two strings `a` and `b` from the input, where `a` and `b` are of equal length and contain digits from 1 to 9. The function then constructs two new strings, `kq1` and `kq2`, such that for each position where `a` and `b` have the same digit, `kq1` and `kq2` will have that same digit. For the first position where `a` and `b` differ, the smaller digit is placed in `kq1` and the larger digit in `kq2`. For all subsequent differing positions, the larger digit is placed in `kq1` and the smaller digit in `kq2`. Finally, the function prints `kq1` and `kq2` for each test case. The function does not return any value.

