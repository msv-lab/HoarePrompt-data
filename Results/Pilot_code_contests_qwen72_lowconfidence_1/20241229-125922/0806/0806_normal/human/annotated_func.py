#State of the program right berfore the function call: N is an integer such that 2 ≤ N ≤ 10^5, and A is a list of N integers where each integer A_i satisfies 1 ≤ A_i ≤ 10^9.
def func():
    n = input()
    A = map(int, raw_input().split(' '))
    A.sort()
    ans = A[0]
    for a in A[1:]:
        m = a % ans
        
        if m != 0:
            ans = min(m, ans)
        
    #State of the program after the  for loop has been executed: `N` is an integer such that \(2 \leq N \leq 10^5\), `A` is a sorted list of integers (each between 1 and \(10^9\)), `n` is an input string, `ans` is the greatest common divisor (GCD) of the elements in `A`.
    print(ans)
#Overall this is what the function does:The function reads an integer `N` from the input, followed by a list of `N` integers `A`. It then calculates the greatest common divisor (GCD) of the elements in `A` and prints the result. The function does not return any value; instead, it outputs the GCD directly to the console. After the function concludes, the state of the program includes the original integer `N`, a sorted list `A` of integers (each between 1 and \(10^9\)), and the GCD of the elements in `A` printed to the console. Note that the function assumes valid input and does not handle invalid input cases (e.g., non-integer values or incorrect input formats).

