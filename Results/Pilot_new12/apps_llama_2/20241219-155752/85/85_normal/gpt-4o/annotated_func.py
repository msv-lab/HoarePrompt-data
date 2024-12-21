#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the original value of `n` with all trailing 9s removed, `max_9s` is the number of trailing 9s in the original value of `n`
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function reads an integer input from the user, removes trailing 9s from the input number, calculates the number of trailing 9s, and then prints the product of the number without trailing 9s (plus one) and the number of trailing 9s. The function does not handle cases where the input is not an integer or is outside the range of 2 to 10^9. It does not return any value, only prints the calculated result. If the input number does not have any trailing 9s, the function will still output a value, which is the product of the input number plus one and zero, effectively just printing zero. The function does not validate or handle any potential exceptions or errors that may occur during the execution of the input() function or the integer division operation.

