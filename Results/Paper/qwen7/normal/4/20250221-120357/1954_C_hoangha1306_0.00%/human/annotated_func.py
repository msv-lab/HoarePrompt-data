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
        
    #State: `kq1` is a string containing the cumulative concatenation of the smaller values from each pair of corresponding elements in lists `a` and `b` based on their comparison throughout all iterations. `kq2` is a string containing the cumulative concatenation of the larger values from each pair of corresponding elements in lists `a` and `b` based on their comparison throughout all iterations. `vt` is 1, indicating that there was at least one non-equal comparison during the loop's execution. `i` is equal to `len(a)`, and `q` is `t`, which is the total number of iterations. The values of `a` and `b` remain unchanged.
#Overall this is what the function does:The function processes multiple pairs of strings representing integers of the same length (digits from 1 to 9). For each pair, it constructs two new strings: `kq1` and `kq2`. `kq1` contains the smaller digit from each pair of corresponding elements in the original strings, while `kq2` contains the larger digit. If any pair of corresponding elements are not equal, `vt` is set to 1. After processing all pairs, it prints `kq1` and `kq2` for each pair.

