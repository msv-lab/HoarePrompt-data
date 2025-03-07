#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, x and y are strings representing integers where 1 ≤ x, y < 10^100, and each digit in x and y is from 1 to 9.
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
        
    #State: After all iterations of the loop, `t` remains an integer where 1 ≤ t ≤ 1000, `x` and `y` remain strings representing integers where 1 ≤ x, y < 10^100, and each digit in x and y is from 1 to 9. For each iteration, `a` and `b` are lists of integers converted from the input strings `x` and `y`, respectively. The lists `new` and `new2` are generated for each pair of `a` and `b` such that: 
    #- `new` contains the maximum value of `a[i]` and `b[i]` for each index `i` where `a[i] == b[i]`, and the minimum value of `a[i]` and `b[i]` for each index `i` from the first index where `a[i] != b[i]` to the end of the list.
    #- `new2` contains the minimum value of `a[i]` and `b[i]` for each index `i` where `a[i] == b[i]`, and the maximum value of `a[i]` and `b[i]` for each index `i` from the first index where `a[i] != b[i]` to the end of the list.
#Overall this is what the function does:The function `func` processes multiple pairs of large integer strings (`x` and `y`) based on an integer `t` indicating the number of pairs. For each pair, it generates two new strings: one where the digits are the maximum of the corresponding digits in `x` and `y` up to the first differing digit, and the minimum thereafter; and another where the digits are the minimum of the corresponding digits in `x` and `y` up to the first differing digit, and the maximum thereafter. These two strings are printed for each pair. The function does not return any values but modifies and prints the results directly. After the function completes, `t` remains unchanged, and `x` and `y` retain their original values.

