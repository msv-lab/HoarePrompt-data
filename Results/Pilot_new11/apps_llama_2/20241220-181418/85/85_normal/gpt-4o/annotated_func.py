#State of the program right berfore the function call: there is an integer n such that n is the number of shovels in Polycarp's shop, where n is greater than or equal to 2 and less than or equal to 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `max_9s` is the number of trailing 9s in the original `n`, `n` is the original `n` with all trailing 9s removed
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function calculates and prints the maximum number of shovel pairs that can be bought given a total number of shovels `n`. It accepts an integer `n` from the user as input, where `n` is expected to be between 2 and 10^9 (inclusive), removes any trailing 9s from `n`, counts the number of trailing 9s removed, multiplies the modified `n` (plus one) by the count of trailing 9s, and prints the result. The function does not perform any error checking on the input `n`, so it assumes that `n` will always be a valid integer within the specified range. The function does not handle cases where the input is not an integer or is outside the expected range. If `n` has no trailing 9s, the function will print 0, since `max_9s` will be 0. The state of the program after execution is that it has printed the calculated maximum number of shovel pairs to the console, without modifying any external state or returning any value.

