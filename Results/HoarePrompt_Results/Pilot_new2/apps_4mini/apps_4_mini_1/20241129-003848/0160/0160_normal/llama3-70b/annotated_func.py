#State of the program right berfore the function call: N is an integer between 2 and 500, A is a list of N integers where each integer is between 1 and 10^6, and K is a non-negative integer less than or equal to 10^9.
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: `K` is a non-negative integer less than or equal to 10^9, `A` is a list of integers with at least 2 elements, `gcd` is equal to `math.gcd(A[0], A[1], ..., A[N-1])`, `i` is `N-1`
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: `K` is a non-negative integer less than or equal to 10^9; `A` is a list of integers with at least 2 elements; `gcd` is greater than or equal to 0; `max_divisor` is the largest divisor of `gcd`; `i` is equal to `int(math.sqrt(gcd)) + 1` after all iterations.
    print(max_divisor)
#Overall this is what the function does:The function accepts an integer `N` (between 2 and 500), a list `A` of `N` integers (each between 1 and 10^6), and a non-negative integer `K` (less than or equal to 10^9). It calculates the greatest common divisor (gcd) of the integers in the list `A`, determines the largest divisor of this gcd, and prints this value. Note that `K` is accepted but not used in any computation or condition within the function.

