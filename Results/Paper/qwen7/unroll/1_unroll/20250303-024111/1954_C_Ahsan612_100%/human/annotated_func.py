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
        
    #State: Output State: The output state consists of two strings of digits, each of which is the result of processing two input strings of digits through the given loop. For each position in the strings, the first string (new) contains the maximum value between the corresponding digits of the two input strings if they are not equal at that position or the last digit that was found to be different, otherwise it contains the minimum value. The second string (new2) is the reverse, containing the minimum value if the digits are not equal or the last different digit, otherwise it contains the maximum value.
#Overall this is what the function does:The function processes two input strings of equal length, consisting of digits from 1 to 9. It compares the corresponding digits of the two strings and constructs two new strings based on the comparison results. For each position where the digits are different, the first new string contains the maximum value, and the second new string contains the minimum value. If the digits are the same, the new strings retain the original digits. The function prints these two new strings and does not return any value.

