#State of the program right berfore the function call: x and y are strings of equal length consisting of digits from 1 to 9.
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
        
    #State: Output State: The output state consists of two strings of digits. For each iteration of the loop, a new string `new` and `new2` are generated based on the comparison of two input strings `a` and `b`. The first string `new` contains the maximum value at each position where `a` and `b` differ or when they are different from the previous matching pair. The second string `new2` contains the minimum value at each position where `a` and `b` differ or when they are different from the previous matching pair. After all iterations, the final `new` and `new2` strings are printed.
#Overall this is what the function does:The function processes pairs of input strings `a` and `b`, which are lists of integers. For each pair, it generates two new strings `new` and `new2`. `new` contains the maximum value at each position where `a` and `b` differ or when they are different from the previous matching pair. `new2` contains the minimum value at each position where `a` and `b` differ or when they are different from the previous matching pair. After processing all pairs, it prints the final `new` and `new2` strings.

