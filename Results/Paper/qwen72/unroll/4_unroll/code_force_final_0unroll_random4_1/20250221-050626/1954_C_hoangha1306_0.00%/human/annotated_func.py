#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, x and y are integers for each test case such that 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: For each test case, the loop prints two strings `kq1` and `kq2` which are the result of comparing the digits of the input strings `a` and `b`. If the digits at the same position in `a` and `b` are the same, they are added to both `kq1` and `kq2`. If the digits are different, the smaller digit is added to `kq1` and the larger digit is added to `kq2` for the first difference encountered, and then the larger digit is added to `kq1` and the smaller digit is added to `kq2` for all subsequent differences. The loop iterates `t` times, processing `t` pairs of input strings. After all iterations, `t` pairs of `kq1` and `kq2` are printed.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two strings `a` and `b` from the input, where each string consists of digits from 1 to 9. The function then compares the digits of `a` and `b` at each position. If the digits are the same, they are added to both `kq1` and `kq2`. If the digits are different, the first difference encountered results in the smaller digit being added to `kq1` and the larger digit to `kq2`, and for all subsequent differences, the larger digit is added to `kq1` and the smaller digit to `kq2`. After processing each test case, the function prints the two resulting strings `kq1` and `kq2`. The function does not return any value.

