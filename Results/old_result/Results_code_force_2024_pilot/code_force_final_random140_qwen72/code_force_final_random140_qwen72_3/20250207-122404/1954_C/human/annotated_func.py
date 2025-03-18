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
                    kq1 = kq1 + str(x)
                    kq2 = kq2 + str(y)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: After all iterations of the loop, `t` remains an input integer such that 1 <= t <= 1000, `q` is `t-1` (indicating the loop has completed its final iteration), `a` and `b` are the last input strings provided for the final iteration, `i` is `len(a) - 1` (indicating the completion of the inner loop over the characters of `a` and `b`), `kq1` and `kq2` are the final strings formed by the rules specified in the loop for the last iteration, and `vt` is either 0 or 1 depending on the last comparison made in the final iteration. All other variables not modified within the loop remain unchanged.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two strings `a` and `b` of equal length, consisting of digits from 1 to 9. It then generates two new strings `kq1` and `kq2` based on the following rules: If the corresponding characters in `a` and `b` are the same, both `kq1` and `kq2` take that character. If the characters differ, the smaller character is added to `kq1` and the larger to `kq2` for the first differing position, and vice versa for subsequent positions. The function prints `kq1` and `kq2` for each test case. After processing all test cases, the function completes without returning any value.

