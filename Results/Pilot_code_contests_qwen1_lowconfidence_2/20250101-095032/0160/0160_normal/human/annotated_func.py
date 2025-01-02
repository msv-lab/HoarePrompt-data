#State of the program right berfore the function call: N is an integer such that 2 ≦ N ≦ 10^{12} and X is an integer such that 1 ≦ X ≦ N-1.
def func():
    L = map(int, raw_input().split())
    n = L[0]
    x = L[1]
    res = n
    a = x
    b = n - x
    flag = True
    while flag:
        if a > b:
            q = a // b
            a -= q * b
            res += 2 * q * b
        elif b > a:
            q = b // a
            b -= q * a
            res += 2 * a * q
        else:
            res += a
            flag = False
        
    #State of the program after the loop has been executed: `n` is the first element of the list `L`, `x` is the second element of the list `L`, `res` is the final result obtained by repeatedly applying the loop operations until `a` equals `b`, `a` is `0`, `b` is `0`, and `flag` is `False`.
    print(res)
#Overall this is what the function does:The function reads two integers \( n \) and \( x \) from the standard input where \( 2 \leq n \leq 10^{12} \) and \( 1 \leq x \leq n-1 \). It then calculates the value of \( res \) by repeatedly applying a series of operations based on the values of \( a \) and \( b \), which are initially set to \( x \) and \( n-x \) respectively. The operations involve updating \( a \) and \( b \) using the floor division and subtraction, and updating \( res \) accordingly. The loop continues until \( a \) equals \( b \). Finally, the function prints the value of \( res \). The function does not return any value. An edge case to consider is when \( n \) is very large (up to \( 10^{12} \)), the function may take a significant amount of time to execute due to the iterative process. Additionally, if \( n \) or \( x \) do not meet the specified constraints, the function assumes default values without any error handling.

