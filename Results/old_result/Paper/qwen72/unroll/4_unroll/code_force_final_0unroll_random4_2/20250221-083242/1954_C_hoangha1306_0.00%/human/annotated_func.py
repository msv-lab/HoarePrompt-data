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
        
    #State: For each of the t test cases, the loop outputs two strings, kq1 and kq2, which are the result of comparing the digits of the input strings a and b. The first string, kq1, contains the lexicographically smaller digit at each position where the digits differ, and the second string, kq2, contains the lexicographically larger digit at each position where the digits differ. If the digits are the same, they are included in both kq1 and kq2. The values of t, x, and y remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two strings `a` and `b` from the input, both consisting of digits from 1 to 9. It then compares the digits of `a` and `b` at each position. If the digits are the same, they are included in both `kq1` and `kq2`. If the digits differ, the lexicographically smaller digit is included in `kq1` and the lexicographically larger digit is included in `kq2`. The function prints `kq1` and `kq2` for each test case. The values of `t`, `a`, and `b` remain unchanged after the function execution.

