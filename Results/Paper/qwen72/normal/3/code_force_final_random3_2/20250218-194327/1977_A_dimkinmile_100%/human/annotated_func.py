#State of the program right berfore the function call: The function should take two parameters, n and m, where n and m are integers such that 1 <= n, m <= 100. Additionally, the function should be able to handle multiple test cases, where the number of test cases t is an integer such that 1 <= t <= 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: *`n` and `m` are specific integers such that 1 <= n, m <= 100, and `t` is an integer such that 1 <= t <= 100. If the difference between `n` and `m` is a non-negative even number, then the difference between `n` and `m` is a non-negative even number. Otherwise, either (n - m) is not divisible by 2, or n - m is less than 0.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads two integers, `n` and `m`, from the user input, where both `n` and `m` are expected to be within the range 1 to 100. The function then checks if the difference between `n` and `m` is a non-negative even number. If the condition is true, it prints 'Yes'; otherwise, it prints 'No'. The final state of the program is that the values of `n` and `m` are unchanged, and the output is either 'Yes' or 'No' based on the condition.

