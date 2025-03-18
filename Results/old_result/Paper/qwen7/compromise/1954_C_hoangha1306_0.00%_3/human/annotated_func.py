#State of the program right berfore the function call: x and y are strings representing integers of the same length, consisting of digits from 1 to 9.
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
        
    #State: `i` is equal to `len(a)`, `a` and `b` are the new input strings after all iterations, `kq1` is the final concatenated string containing the minimum value (as a character) of each pair of corresponding characters from strings `a` and `b`, `q` is `t`, `vt` is 1, `x` is the minimum of `int(a[i-1])` and `int(b[i-1])`, `y` is the maximum of `int(a[i-1])` and `int(b[i-1])`, and `kq2` is the final concatenated string containing the maximum value (as a character) of each pair of corresponding characters from strings `a` and `b`
#Overall this is what the function does:The function processes multiple pairs of input strings `a` and `b`, each representing integers of the same length consisting of digits from 1 to 9. For each pair, it constructs two new strings: `kq1` containing the minimum digit from each corresponding position of `a` and `b`, and `kq2` containing the maximum digit from each corresponding position. It then prints these two strings for each pair.

