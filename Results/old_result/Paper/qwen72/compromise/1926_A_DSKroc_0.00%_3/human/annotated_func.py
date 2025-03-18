#State of the program right berfore the function call: The function `func` does not take any parameters, but it is expected to read input from stdin where the first line contains an integer t (1 ≤ t ≤ 32) representing the number of test cases, and each of the following t lines contains a string of length 5 consisting of letters 'A' and 'B'. All t strings are distinct.
def func():
    t = int(input())
    for q in range(t):
        ac = 0
        
        bc = 0
        
        s = input()
        
        for i in s:
            if i == 'A':
                ac += 1
            else:
                bc += 1
        
    #State: `t` is an integer between 1 and 32, `q` is `t-1`, `s` is the last input string, `ac` is the number of 'A' characters in the last input string, and `bc` is the number of non-'A' characters in the last input string.
    if (ac > bc) :
        print('A')
        #This is printed: A
    else :
        print('B')
        #This is printed: B
    #State: *`t` is an integer between 1 and 32, `q` is `t-1`, `s` is the last input string, `ac` is the number of 'A' characters in `s`, and `bc` is the number of non-'A' characters in `s`. If `ac` > `bc`, the number of 'A' characters in `s` is greater than the number of non-'A' characters. Otherwise, `ac` is less than or equal to `bc`.
#Overall this is what the function does:The function reads an integer `t` from standard input, representing the number of test cases. It then reads `t` distinct strings of length 5, each consisting of letters 'A' and 'B'. For each string, the function counts the number of 'A' and 'B' characters. After processing all the strings, the function prints 'A' if the number of 'A' characters in the last string is greater than the number of 'B' characters, and prints 'B' otherwise. The function does not return any value.

