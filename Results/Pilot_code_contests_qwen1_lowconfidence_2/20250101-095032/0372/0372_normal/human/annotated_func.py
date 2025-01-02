#State of the program right berfore the function call: n is an integer such that 3 <= n <= 1000.
def func():
    n = int(raw_input())
    for i in range(n / 2):
        if gcd(n - i, i) == 1:
            print(str(i) + ' ' + str(n - i))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 3 and 1000 inclusive, `i` is either `n // 2` or the last value of `i` for which `gcd(n - i, i) == 1` was true, and the output consists of all pairs `(i, n - i)` such that `gcd(n - i, i) == 1`. If no such pairs exist, `i` will be `n // 2` and no output will be generated.
#Overall this is what the function does:The function `func()` takes no parameters and does not return any value. It reads an integer `n` from the user where `3 <= n <= 1000`. The function then iterates through all integers `i` from 0 to `n//2 - 1` and checks if the greatest common divisor (GCD) of `n - i` and `i` is 1. If the condition is met, it prints the pair `(i, n - i)`. After the loop, if no such pairs exist, the function ends without printing anything. The final state of the program is that either all valid pairs `(i, n - i)` where `gcd(n - i, i) == 1` have been printed, or no output is generated if no such pairs exist.

