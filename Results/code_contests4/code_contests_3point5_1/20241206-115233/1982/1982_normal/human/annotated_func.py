#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5.**
def func():
    n = int(input())
    i = '110'
    p = 1
    while int(i, 2) <= n:
        if n % int(i, 2) == 0:
            p = int(i, 2)
        
        i = '1' + i + '0'
        
    #State of the program after the loop has been executed: `n` is 28 or greater, `i` is a binary number less than or equal to `n` in decimal with '1' added at the beginning and '0' added at the end, `p` is the decimal equivalent of `i` such that `n % p == 0`
    print(p)
#Overall this is what the function does:The function prompts the user for an integer `n`, then iterates through binary numbers starting from '110' and ending at a binary number less than or equal to `n` in decimal with '1' added at the beginning and '0' added at the end. During each iteration, it checks if `n` is divisible by the decimal equivalent of the current binary number and updates `p` accordingly. Finally, it prints the value of `p`. The function does not accept any parameters and does not return any value.

