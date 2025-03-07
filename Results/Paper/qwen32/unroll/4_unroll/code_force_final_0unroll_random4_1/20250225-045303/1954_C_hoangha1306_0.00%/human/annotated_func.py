#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same number of digits.
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
        
    #State: For each test case, two strings `kq1` and `kq2` are printed where each position in the strings is determined by the comparison of the corresponding digits in the input strings `a` and `b` according to the given rules. The final output state is the concatenation of these outputs for all `t` test cases.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `x` and `y` represented as strings with the same number of digits (1 to 9). For each test case, it constructs two new strings by comparing corresponding digits of `x` and `y`. If the digits are the same, they are added to both new strings. If the digits differ, the smaller digit is added to one string and the larger digit to the other, with a rule to ensure the first differing position is handled differently. The function prints two strings for each test case.

