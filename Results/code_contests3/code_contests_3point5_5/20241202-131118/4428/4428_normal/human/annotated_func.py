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
        
    #State of the program after the  for loop has been executed: `result` is the difference between the number of occurrences of 'I' and occurrences of other characters in the list `S`. `N` is the length of the list `S`, `i` is `N-1`, and `S` is a list of characters.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`result` is the difference between the number of occurrences of 'I' and occurrences of other characters in the list `S`. `N` is the length of the list `S`, `i` is `N-1`, and `S` is a list of characters. If `result` is less than 0, then the value of `result` is negative after entering the if condition.
    print(result)
#Overall this is what the function does:The function reads an integer N and a string S, then iterates through the string counting occurrences of 'I' and other characters. It calculates the difference between the counts and prints the result. If the result is negative, it sets it to 0 before printing. The function does not have any explicit return value.

