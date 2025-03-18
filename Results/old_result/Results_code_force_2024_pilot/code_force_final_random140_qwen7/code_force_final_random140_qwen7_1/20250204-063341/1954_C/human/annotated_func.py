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
                    kq1 = kq1 + str(x)
                    kq2 = kq2 + str(y)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: All elements of `a` and `b` have been processed, and `i` is now equal to `len(a)`. The variable `kq1` contains a string where each differing pair of elements from `a` and `b` is represented by the larger number followed by the smaller number, and `kq2` contains a string where each differing pair is represented by the smaller number followed by the larger number. If two elements at the same index in `a` and `b` are the same, their string representation is appended to `kq1` and `kq2` without any change. The variable `vt` remains 1 after the loop completes.
#Overall this is what the function does:The function processes two input strings `a` and `b` of equal length, consisting of digits from 1 to 9. For each pair of characters at the same index in `a` and `b`, if they are the same, the character is appended to both output strings `kq1` and `kq2`. If they differ, the smaller digit is appended first in `kq1` and the larger digit is appended first in `kq2`. After processing all characters, the function prints `kq1` and `kq2`.

