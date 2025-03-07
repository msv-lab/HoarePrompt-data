#State of the program right berfore the function call: The function expects a list of strings as input, where each string is of length 5 and consists only of the characters 'A' and 'B'. The list contains between 1 and 32 distinct strings.
def func():
    t = int(input())
    for i in range(t):
        a = input()
        
        l = 0
        
        h = 0
        
        for j in a:
            if j == 'A':
                l += 1
            else:
                h += 1
        
        if l > h:
            print('A')
        else:
            print('B')
        
    #State: The loop will print 'A' if the number of 'A's in the input string is greater than the number of 'B's, and 'B' otherwise, for each of the `t` input strings. The variables `l` and `h` will be reset to 0 for each iteration.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of input strings to process. For each of the `t` input strings, it counts the number of 'A' and 'B' characters. If the number of 'A's is greater than the number of 'B's, it prints 'A'; otherwise, it prints 'B'. The function does not return any value. The state of the program after the function concludes is that `t` input strings have been processed, and the corresponding 'A' or 'B' has been printed for each string.

