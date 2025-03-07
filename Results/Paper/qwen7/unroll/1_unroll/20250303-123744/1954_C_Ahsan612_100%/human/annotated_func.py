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
        
    #State: Output State: The output state consists of two strings of digits, each of the same length as the input strings `x` and `y`. For each position in these strings:
    #
    #- The first string (from the `new` list) contains the maximum digit between the corresponding digits of `x` and `y` up to the point where the digits differ, and then the minimum digit thereafter.
    #- The second string (from the `new2` list) contains the minimum digit between the corresponding digits of `x` and `y` up to the point where the digits differ, and then the maximum digit thereafter.
#Overall this is what the function does:The function processes two input strings, `x` and `y`, which represent integers of the same length consisting of digits from 1 to 9. It prints two new strings. The first string contains the maximum digit between the corresponding digits of `x` and `y` up to the point where the digits differ, and then the minimum digit thereafter. The second string contains the minimum digit between the corresponding digits of `x` and `y` up to the point where the digits differ, and then the maximum digit thereafter. The function does not return any value; it only outputs the two new strings.

