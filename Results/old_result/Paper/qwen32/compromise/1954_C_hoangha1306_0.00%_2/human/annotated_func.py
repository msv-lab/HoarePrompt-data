#State of the program right berfore the function call: x and y are integers consisting only of digits from 1 to 9, and they have the same length. t is an integer such that 1 <= t <= 1000, representing the number of test cases. Each test case consists of two integers x and y with the same length and digits from 1 to 9.
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
        
    #State: `kq1` and `kq2` are the final constructed strings based on the comparison of all pairs of `a` and `b` strings across all iterations, `vt` is 1 if there was at least one mismatch in any iteration, otherwise 0, `x` and `y` are the minimum and maximum of the last differing characters across all iterations, `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` of the same length, consisting only of digits from 1 to 9. It then constructs and prints two new integers `kq1` and `kq2` based on the comparison of corresponding digits of `x` and `y`. Specifically, if the digits are the same, they are added to both `kq1` and `kq2`. If the digits differ, the smaller digit is added to `kq1` and the larger digit to `kq2` for the first mismatch, and for subsequent mismatches, the larger digit is added to `kq1` and the smaller digit to `kq2`.

