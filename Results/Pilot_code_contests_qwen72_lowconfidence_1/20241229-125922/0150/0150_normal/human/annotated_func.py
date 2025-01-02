#State of the program right berfore the function call: The input is a single string consisting of lowercase English letters 'a'-'z', representing the colors of points on a line, with the length of the string being between 1 and 10^6.
def func():
    s = raw_input()
    a = [[s[0], 1]]
    for i in s[1:]:
        if a[-1][0] == i:
            a[-1][1] += 1
        else:
            a.append([i, 1])
        
    #State of the program after the  for loop has been executed: `s` is the input string, `a` is a list of sublists where each sublist is `[char, count]`, representing the character `char` from `s` and the count of its consecutive occurrences in `s`.
    turns = 0
    while len(a) > 1:
        turns += 1
        
        temp = []
        
        if a[0][1] > 1:
            temp.append([a[0][0], a[0][1] - 1])
        
        for i in a[1:-1]:
            if i[1] > 2:
                temp.append([i[0], i[1] - 2])
        
        if a[-1][1] > 1:
            temp.append([a[-1][0], a[-1][1] - 1])
        
        if len(temp) < 2:
            break
        
        a = [temp[0]]
        
        for i in temp[1:]:
            if i[0] != a[-1][0]:
                a.append(i)
            else:
                a[-1][1] += i[1]
        
    #State of the program after the loop has been executed: `s` is the input string, `a` is a list of sublists where each sublist is `[char, count]` and represents the unique characters and their counts after the loop has processed `a` multiple times. The final `a` will have at most one element or be an empty list if the loop breaks due to `len(temp) < 2`. `turns` is the number of times the loop executed.
    print(turns)
#Overall this is what the function does:The function reads a string `s` from the user, where `s` consists of lowercase English letters representing colors of points on a line. It processes the string to group consecutive identical characters and their counts into a list `a`. The function then repeatedly reduces the counts of these characters in a specific manner until no more reductions can be made. Specifically, it removes one occurrence from the first and last groups if they have more than one occurrence, and two occurrences from the middle groups if they have more than two occurrences. This process continues until the list `a` has at most one element or becomes empty. The function prints the number of iterations (turns) it took to reach this state. The purpose of the function is to determine the minimum number of points to remove from the input string so that no two adjacent points have the same color. Edge cases include when the input string is already in a state where no two adjacent points have the same color (in which case the function will print 0), or when the string is very short (e.g., a single character).

