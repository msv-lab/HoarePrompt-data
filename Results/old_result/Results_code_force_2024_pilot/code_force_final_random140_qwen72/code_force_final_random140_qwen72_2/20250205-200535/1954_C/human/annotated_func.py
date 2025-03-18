#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, x and y are strings representing integers where 1 <= x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
                    kq1 = kq1 + str(x)
                    kq2 = kq2 + str(y)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: `t` is greater than or equal to 1, `q` is `t-1`, `a` is a non-empty input string, `b` is a new input string, `i` is the length of `a` (or `b`). `kq1` and `kq2` are strings constructed based on the comparison of corresponding characters in `a` and `b`. For each pair of characters at the same position in `a` and `b`: if they are equal, both `kq1` and `kq2` are appended with that character. If they are not equal, the smaller character is appended to `kq1` and the larger character is appended to `kq2` when `vt` is 0; otherwise, the larger character is appended to `kq1` and the smaller character is appended to `kq2`. `vt` is either 0 or 1 depending on whether the characters were different at any point during the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two strings `a` and `b` from the input, which represent integers consisting only of digits from 1 to 9. The function then constructs two new strings, `kq1` and `kq2`, by comparing the corresponding characters of `a` and `b`. If the characters are equal, both `kq1` and `kq2` are appended with that character. If the characters are not equal, the smaller character is appended to `kq1` and the larger character is appended to `kq2` initially, and then the roles are swapped for subsequent unequal characters. Finally, the function prints `kq1` and `kq2` for each test case. The function does not return any value.

