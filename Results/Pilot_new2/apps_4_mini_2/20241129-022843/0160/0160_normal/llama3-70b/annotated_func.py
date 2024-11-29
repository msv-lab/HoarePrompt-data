#State of the program right berfore the function call: N is an integer such that 2 <= N <= 500, A is a list of N integers where each integer A[i] satisfies 1 <= A[i] <= 10^6, and K is a non-negative integer such that 0 <= K <= 10^9.
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 500; `A` is a list of `N` integers; `K` is a non-negative integer such that 0 <= `K` <= 10^9; `gcd` is equal to `math.gcd(A[0], A[1], ..., A[N-1])`; `i` is `N-1`.
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 2 <= `N` <= 500, `A` is a list of `N` positive integers, `K` is a non-negative integer such that 0 <= `K` <= 10^9, `gcd` is equal to `math.gcd(A[0], A[1], ..., A[N-1])`, `max_divisor` is the largest divisor of `gcd` less than or equal to `gcd`, `i` is greater than `0` and less than or equal to `int(math.sqrt(gcd))`, the value of `max_divisor` remains unchanged if no divisors are found, or is updated based on the divisors of `gcd`.
    print(max_divisor)
#Overall this is what the function does:The function accepts an integer `N`, a list `A` of `N` integers, and a non-negative integer `K`. It calculates the greatest common divisor (GCD) of the integers in `A` and determines the largest divisor of that GCD. The result is printed as the output, but the variable `K` is not utilized in any calculations or logic within the function.

