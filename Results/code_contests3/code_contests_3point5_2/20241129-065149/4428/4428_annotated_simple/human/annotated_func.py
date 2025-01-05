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
        
    #State of the program after the  for loop has been executed: `NameError` is assigned the input string from raw_input(), `S` is a string, `result` is the difference between the number of 'I's and the number of non-'I's in string `S`, `N` is the length of string `S`, `i` is `N - 1`.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`NameError` is assigned the input string from raw_input(), `S` is a string, `result` is the difference between the number of 'I's and the number of non-'I's in string `S`, `N` is the length of string `S`, `i` is `N - 1`. If `result` < 0, then `result` is 0.
    print(result)
#Overall this is what the function does:The function `func` reads an integer `N` and a string `S` from user input. It then iterates over the characters in `S`, incrementing the result by 1 for each 'I' and decrementing it by 1 for other characters. If the final result is negative, it sets it to 0. Finally, it prints the resulting value. The function does not accept any parameters and does not return any value.

