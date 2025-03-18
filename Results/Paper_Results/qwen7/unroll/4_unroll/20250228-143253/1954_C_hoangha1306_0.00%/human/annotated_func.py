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
        
    #State: x and y are unchanged, t is the final value after the loop, kq1 and kq2 are strings generated from the loop based on the inputs provided during each iteration.
#Overall this is what the function does:The function processes multiple pairs of strings representing integers of the same length (digits from 1 to 9). For each pair, it generates two new strings: `kq1` and `kq2`. In `kq1`, the function pairs the smaller digit from each position of the input strings, while in `kq2`, it pairs the larger digit. If the digits at a position are the same, both `kq1` and `kq2` contain the same digit. After processing all pairs, it prints `kq1` and `kq2` for each pair.

