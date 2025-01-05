#State of the program right berfore the function call: **
def func():
    __author__ = 'RASULBEK'
    n = input()
    p = map(int, raw_input().split())
    i = 0
    a = []
    while i < n:
        j = 0
        
        b = []
        
        s = raw_input()
        
        while j < len(s):
            if s[j] == '1':
                b.append(1)
            else:
                b.append(0)
            j += 1
        
        a.append(b)
        
        i += 1
        
    #State of the program after the loop has been executed: Output State: `__author__` is 'RASULBEK', `n` is a positive integer, `p` is a map object containing input values converted to integers, `i` is equal to `n`, `a` is a list containing lists of 1's and 0's based on the input strings, `j` is equal to the length of the last input string `s`, `b` is a list containing the sequence of 1's and 0's based on the last input string `s`, `s` is assigned the last input string value.
    i = 0
    while i < n:
        j = i + 1
        
        while j < n:
            if p[i] > p[j]:
                if a[i][j] == 1 and a[j][i] == 1:
                    tmp = p[i]
                    p[i] = p[j]
                    p[j] = tmp
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: __author__` is 'RASULBEK', `n` is a positive integer greater than 3, `p` is a map object containing input values converted to integers, `i` is equal to `n`, `a` is a list containing lists of 1's and 0's based on the input strings, `j` is equal to `n` + 1, `b` is a list containing the sequence of 1's and 0's based on the last input string `s`, `s` is assigned the last input string value, all comparisons and swaps based on the conditions have been completed within the loop.
    i = 0
    while i < n:
        j = i + 1
        
        while j < n:
            if p[i] > p[j]:
                if a[i][j] == 1 and a[j][i] == 1:
                    tmp = p[i]
                    p[i] = p[j]
                    p[j] = tmp
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: 'author' is 'RASULBEK', 'n' is a positive integer greater than 3, 'p' is a map object where the values are sorted in ascending order, 'i' is equal to 'n', 'a' is updated based on the conditions in the loop, 'j' is equal to 'n', 'b' is a list containing the sequence of 1's and 0's based on the last input string 's', 's' is assigned the last input string value.
    i = 0
    s = ''
    while i < n:
        s += str(p[i]) + ' '
        
        i += 1
        
    #State of the program after the loop has been executed: 'author' is 'RASULBEK', 'n' is a positive integer greater than 3, 'p' is a map object sorted in ascending order, 'i' is equal to 'n', 'a' is updated based on the conditions in the loop, 'j' is equal to 'n', 'b' is a list containing the sequence of 1's and 0's based on the last input string 's', 's' is assigned a string containing all elements of 'p' concatenated with a space
    print(s)
#Overall this is what the function does:The function `func` reads input values, processes them, and then prints the sorted values separated by spaces. It does not accept any parameters. The code initializes variables, reads inputs, processes the data to sort values, and finally prints the sorted values. The function focuses on input processing and sorting of values for output.

