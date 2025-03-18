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
        
    #State: The final output state will be such that `new` is a list where each element is `min(a[j], b[j])` for `j` from `0` to `len(a)-1`, and `new2` is a list where each element is `max(a[j], b[j])` for `j` from `0` to `len(a)-1`.
#Overall this is what the function does:The function processes two strings of equal length, consisting of digits from 1 to 9, character by character. For each position, it determines the minimum and maximum of the corresponding digits from both strings. It then constructs two new strings based on these comparisons and prints them. The first string consists of the maximum digit at each position, while the second string consists of the minimum digit at each position.

