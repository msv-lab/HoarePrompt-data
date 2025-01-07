#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    max_9s = 0
    while (n + 1) % 10 == 0:
        max_9s += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the integer obtained by successively removing the last digit of the original `n` until the last digit is not 9, `max_9s` is the count of how many times the last digit was 9 before it stopped being 9
    pairs = (n + 1) * max_9s
    print(pairs)
#Overall this is what the function does:The function reads an integer \( n \) from the user where \( 2 \leq n \leq 10^9 \). It then counts the number of trailing 9s in \( n \), removes those trailing 9s, and calculates a value based on the remaining part of \( n \) and the count of trailing 9s. Specifically, it computes the product of the remaining part of \( n \) plus one and the count of trailing 9s. Finally, it prints this computed value. The function does not accept any parameters and returns no value explicitly; however, the printed value can be considered its output.

