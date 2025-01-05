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
        
    #State of the program after the  for loop has been executed: `N` is greater than or equal to 0, `S` is a string, `result` is either 0, 2N, or -2N.
    if (result < 0) :
        result = 0
    #State of the program after the if block has been executed: *`N` is greater than or equal to 0, `S` is a string, `result` is either 0, 2N, or -2N. If `result` < 0, `result` is updated to -2N.
    print(result)
#Overall this is what the function does:The function func reads an integer N from the user and a string S. It then iterates over the characters in S, incrementing the result by 1 for each occurrence of 'I' and decrementing it by 1 for other characters. If the final result is negative, it is set to 0. The function does not take any parameters and does not return any value.

