#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, x and y are strings representing integers where 1 ≤ x, y < 10^100, and x and y consist only of digits from 1 to 9.
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
        
    #State: After the loop executes all its iterations, `t` is decremented by the number of iterations that were performed, but it remains within the range 1 ≤ t ≤ 1000. The variables `x` and `y` are unchanged and still represent strings of integers where 1 ≤ x, y < 10^100, consisting only of digits from 1 to 9. For each iteration, the lists `a` and `b` are updated with the digits from the new input strings `x` and `y`. The lists `new` and `new2` are generated for each iteration, where `new` contains the maximum value between the corresponding elements of `a` and `b` for the first part of the list and the minimum value for the second part (if any), and `new2` contains the opposite. After all iterations, the final state of `a` and `b` will reflect the last input strings processed, and `new` and `new2` will be the final lists generated from these inputs.
#Overall this is what the function does:The function `func` reads multiple pairs of digit-only strings `x` and `y` from the standard input, up to `t` times, where `t` is an integer between 1 and 1000. For each pair, it generates two new strings: one by taking the maximum digit at each position and another by taking the minimum digit at each position. It prints these two strings for each pair. The function does not return any value. After all iterations, the variable `t` is effectively reduced by the number of iterations performed, but the original input strings `x` and `y` remain unchanged.

