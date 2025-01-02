#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 10^5, K is an integer such that 1 ≤ K ≤ 10^9, and A is a list of N integers where each element A_i satisfies 1 ≤ A_i ≤ 10^9.
def func():
    N, K = map(int, raw_input().split())
    A = sorted(list(map(int, raw_input().split())))
    if (K > A[-1]) :
        print('IMPOSSIBLE')
    else :
        flag = True
        tmp = reduce(gcd, A)
        if (tmp != 1) :
            flag = False
        #State of the program after the if block has been executed: *N is the first integer input, K is the second integer input, A is a sorted list of N integers where each element A_i satisfies 1 ≤ A_i ≤ 10^9, K is less than or equal to A[-1], and tmp is the GCD of all elements in A. If tmp is not 1, flag is False. Otherwise, flag remains True.
        for a in A:
            if a == K or (K - a) % tmp == 0:
                flag = True
                break
            
        #State of the program after the  for loop has been executed: `N` is the first integer input, `K` is the second integer input, `A` is a sorted list of `N` integers where each element \( A_i \) satisfies \( 1 \leq A_i \leq 10^9 \), `K` is less than or equal to \( A[-1] \), `tmp` is the GCD of all elements in `A`, and `flag` is `True` if there exists an element `a` in `A` such that `a == K` or `(K - a) % tmp == 0`; otherwise, `flag` is `False`.
        if flag :
            print('POSSIBLE')
        else :
            print('IMPOSSIBLE')
        #State of the program after the if-else block has been executed: *`N` is the first integer input, `K` is the second integer input, `A` is a sorted list of `N` integers where each element \( A_i \) satisfies \( 1 \leq A_i \leq 10^9 \), `K` is less than or equal to \( A[-1] \), `tmp` is the GCD of all elements in `A`. If `flag` is `True`, 'POSSIBLE' is printed. If `flag` is `False`, no message is printed.
    #State of the program after the if-else block has been executed: *`N` is the first integer input, `K` is the second integer input, `A` is a sorted list of `N` integers where each element \( A_i \) satisfies \( 1 \leq A_i \leq 10^9 \). If `K` is greater than the last element of `A` (i.e., `A[-1]`), 'IMPOSSIBLE' is printed. Otherwise, `K` is less than or equal to `A[-1]`, and `tmp` is the GCD of all elements in `A`. If `flag` is `True`, 'POSSIBLE' is printed. If `flag` is `False`, no message is printed.
#Overall this is what the function does:The function `func` reads two integers `N` and `K` from the standard input, followed by a list of `N` integers `A`. It then checks whether it is possible to form the integer `K` by adding or subtracting multiples of the greatest common divisor (GCD) of the elements in `A`. If `K` is greater than the largest element in `A`, the function prints 'IMPOSSIBLE'. Otherwise, if `K` can be formed as described, the function prints 'POSSIBLE'; otherwise, it prints 'IMPOSSIBLE'. The function does not return any value but modifies the program state by printing the result. The function handles edge cases where `K` is outside the range of elements in `A` or where the GCD of `A` is not 1.

