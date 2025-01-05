#State of the program right berfore the function call: **
def func():
    N = int(raw_input())
    S = raw_input()
    result = 0
    for i in range(N):
        if S[i] == 'I':
            result += 1
        else:
            result -= 1
        
    #State of the program after the  for loop has been executed: `S` is not defined, `result` can be any integer value, `N` is greater than 0, `i` is equal to `N` - 1. The final value of `result` depends on the occurrences of 'I' and other characters in the string `S` across all the iterations of the loop.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`S` is not defined, `result` can be any integer value, `N` is greater than 0, `i` is equal to `N` - 1. If `result` is less than 0, the final value of `result` will depend on the occurrences of 'I' and other characters in the string `S` across all iterations of the loop.
    print(result)
#Overall this is what the function does:The function `func` reads an integer `N` from the user input, then reads a string `S` of length `N`. It iterates over the characters of `S` and increments the `result` by 1 for each occurrence of 'I' and decrements by 1 for other characters. If the final `result` is negative, it sets `result` to 0. The function then prints the final value of `result`. The function does not accept any parameters and does not return any value.

