#State of the program right berfore the function call: h is an integer such that 1 ≤ h ≤ 50, and n is an integer such that 1 ≤ n ≤ 2^{h}.
def func():
    h, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            ans += n // 2 - 1
        else:
            ans += n // 2
        
        n //= 2
        
    #State of the program after the loop has been executed: `n` is 1, `h` is unchanged, `ans` is the sum of the positions of the 1s in the binary representation of the original value of `n`, minus the count of 1s
    print(ans)
#Overall this is what the function does:The function accepts two parameters \( h \) and \( n \), where \( h \) is an integer between 1 and 50 inclusive, and \( n \) is an integer between 1 and \( 2^h \) inclusive. The function processes \( n \) by repeatedly dividing it by 2 and adjusting the variable \( ans \) based on whether the current value of \( n \) is even or odd. Specifically, if \( n \) is even, \( ans \) is incremented by \( \frac{n}{2} - 1 \); if \( n \) is odd, \( ans \) is incremented by \( \frac{n}{2} \). The loop continues until \( n \) becomes 1. After the loop, the function prints the value of \( ans \). The final state of the program after the function concludes is that the variable \( ans \) contains the sum of the positions (starting from 1) of the 1s in the binary representation of the original value of \( n \), minus the count of 1s in the binary representation of \( n \).

