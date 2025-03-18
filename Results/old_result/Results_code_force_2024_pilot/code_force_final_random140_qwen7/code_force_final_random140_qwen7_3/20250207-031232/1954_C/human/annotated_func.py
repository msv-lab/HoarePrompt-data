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
                    kq1 = kq1 + str(x)
                    kq2 = kq2 + str(y)
                else:
                    kq1 = kq1 + str(y)
                    kq2 = kq2 + str(x)
        
        print(kq1)
        
        print(kq2)
        
    #State: Output State: After the loop executes all iterations, `i` is equal to `len(a)`, indicating that all characters in `a` and `b` have been processed. `kq1` is a string constructed by taking the minimum of corresponding characters from `a` and `b` when `vt` was 0 at the end of the loop, and the maximum otherwise. Conversely, `kq2` is constructed by taking the maximum when `vt` was 0 and the minimum otherwise. The strings `kq1` and `kq2` will thus be composed of characters derived from comparing each pair of characters from `a` and `b` throughout the entire loop execution, following the rules specified within the loop body.
#Overall this is what the function does:The function processes two input strings, `a` and `b`, each representing an integer of the same length, and constructs two new strings, `kq1` and `kq2`. For each pair of corresponding characters from `a` and `b`, if the characters are the same, both `kq1` and `kq2` are updated with that character. If the characters differ, `kq1` is updated with the smaller digit, and `kq2` is updated with the larger digit. The function prints `kq1` and `kq2` after processing all characters.

