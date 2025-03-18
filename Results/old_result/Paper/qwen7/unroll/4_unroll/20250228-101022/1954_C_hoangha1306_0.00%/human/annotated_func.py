#State of the program right berfore the function call: x and y are strings of equal length consisting of digits from 1 to 9.
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
        
    #State: After executing the loop for `t` iterations, `kq1` and `kq2` will contain strings formed based on the comparison of characters from the input strings `a` and `b`. For each character position, if the characters are the same, they are added to both `kq1` and `kq2`. If they are different, the smaller digit is added to `kq1` and the larger digit is added to `kq2`, with the order of addition alternating between iterations.
#Overall this is what the function does:The function accepts no parameters and processes multiple pairs of input strings `a` and `b`. For each pair, it compares corresponding characters. If the characters are the same, they are added to both `kq1` and `kq2`. If they are different, the smaller digit is added to `kq1` and the larger digit to `kq2`, alternating the order of addition between pairs. Finally, it prints the contents of `kq1` and `kq2` for each pair.

