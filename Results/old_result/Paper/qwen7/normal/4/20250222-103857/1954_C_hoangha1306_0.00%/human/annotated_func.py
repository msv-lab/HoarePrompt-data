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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `len(a)`, meaning the loop has completed all its iterations. `kq1` will be a string that contains the concatenation of the characters from `a` where `a[i]` equals `b[i]` or the smaller of the two characters (`int(a[i])` and `int(b[i])`) if they differ. Similarly, `kq2` will be a string that contains the concatenation of the characters from `a` where `a[i]` equals `b[i]` or the larger of the two characters (`int(a[i])` and `int(b[i])`) if they differ. The variable `vt` will be 1, indicating that the loop has run at least once and adjusted the values accordingly. The variable `q` will be equal to `t`, as it is incremented by 1 in each iteration of the loop. The variables `a` and `b` will remain the input strings provided by the user, and no further changes will occur to them within the loop.
#Overall this is what the function does:The function processes a series of pairs of strings `a` and `b`. For each pair, it constructs two new strings `kq1` and `kq2` based on the comparison of corresponding characters in `a` and `b`. If the characters are the same, both `kq1` and `kq2` include that character. If they differ, `kq1` includes the smaller digit and `kq2` includes the larger digit. After processing all pairs, it prints `kq1` and `kq2` for each pair.

