#State of the program right berfore the function call: x and y are strings of equal length consisting of digits from '1' to '9'.
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
        
    #State: Output State: After the loop executes all the iterations, `i` is equal to the length of list `a`. For every index `j` from `0` to `len(a)-1`, `new[j]` contains the minimum value between `a[j]` and `b[j]`, and `new2[j]` contains the maximum value between `a[j]` and `b[j]`.
    #
    #This means that after all iterations of the loop, both `new` and `new2` will contain the results of comparing each pair of elements from lists `a` and `b`. Specifically, `new` will store the minimum values and `new2` will store the maximum values for each corresponding position in the input lists `a` and `b`. The loop processes the lists character by character, updating `new` and `new2` based on whether the characters match or differ, ensuring that by the end, all elements have been processed.
#Overall this is what the function does:The function reads pairs of digit strings from standard input, compares the corresponding digits of each pair, and prints two new strings. The first string contains the minimum digit from each pair, while the second string contains the maximum digit from each pair. This process is repeated for the number of pairs specified by the user. After processing all pairs, the function does not return any value.

