#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, x and y are integers such that 1 ≤ x < 10^100 and 1 ≤ y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same number of digits in each test case.
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
        
    #State: t remains the same; for each test case, kq1 and kq2 are constructed strings based on the comparison rules, and vt is 1 if there was at least one mismatch, otherwise 0.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` that have the same number of digits and consist only of digits from 1 to 9. It then constructs and prints two new integers `kq1` and `kq2` based on the comparison of corresponding digits of `x` and `y`. If the digits are the same, they are added to both `kq1` and `kq2`. If the digits differ, the smaller digit is added to `kq1` and the larger digit is added to `kq2` for the first mismatch, and thereafter, the larger digit is added to `kq1` and the smaller digit is added to `kq2`.

