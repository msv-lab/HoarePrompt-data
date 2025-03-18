#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, the length of x and y is the same for each test case.
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
        
    #State: After all iterations, `t`, `x`, and `y` remain unchanged. For each test case, `kq1` and `kq2` are printed based on the rules described above.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` of the same length, consisting only of digits from 1 to 9. It then prints two new integers `kq1` and `kq2` for each test case. The digits in `kq1` and `kq2` are determined by comparing the corresponding digits of `x` and `y` and applying specific rules to ensure that `kq1` is always greater than or equal to `kq2`.

