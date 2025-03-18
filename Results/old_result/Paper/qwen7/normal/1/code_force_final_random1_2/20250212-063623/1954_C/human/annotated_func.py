#State of the program right berfore the function call: x and y are strings representing integers of the same length, consisting of digits from 1 to 9.
def func():
    for _ in range(int(input())):
        a = list(map(int, list(input())))
        
        b = list(map(int, list(input())))
        
        new = [None] * len(a)
        
        new2 = [None] * len(a)
        
        i = 0
        
        while i < len(a) and a[i] == b[i]:
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
        
        if i != len(a):
            new[i] = max(a[i], b[i])
            new2[i] = min(a[i], b[i])
            i += 1
            while i < len(a):
                new[i] = min(a[i], b[i])
                new2[i] = max(a[i], b[i])
                i += 1
        
        print(''.join(str(x) for x in new))
        
        print(''.join(str(x) for x in new2))
        
    #State: Output State: After the loop executes all the iterations, `new` will be a list of integers where each element is the minimum of the corresponding elements in `a` and `b` throughout all iterations, and `new2` will be a list of integers where each element is the maximum of the corresponding elements in `a` and `b` throughout all iterations. The value of `i` will be equal to `len(a)`, indicating that the loop has processed all elements in `a` and `b`.
    #
    #In simpler terms, `new` will contain the minimum values of `a` and `b` for each position after all iterations, and `new2` will contain the maximum values of `a` and `b` for each position after all iterations.
#Overall this is what the function does:The function processes multiple pairs of integer strings (x and y) of the same length. For each pair, it creates two lists: `new` and `new2`. `new` contains the minimum values of the corresponding elements in `x` and `y` across all pairs, while `new2` contains the maximum values. After processing all pairs, it prints the contents of `new` and `new2` as strings.

