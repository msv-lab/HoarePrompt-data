#State of the program right berfore the function call: N is an integer between 2 and 500, K is a non-negative integer less than or equal to 10^9, and A is a list of N integers where each A[i] is between 1 and 10^6.
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: `N` is an integer between 2 and 500, `K` is a non-negative integer less than or equal to 10^9, `A` is a list of `N` integers where each `A[i]` is between 1 and 10^6, `gcd` is equal to the greatest common divisor of all elements in the list `A`, `i` is `N-1`.
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: `N` is an integer between 2 and 500, `K` is a non-negative integer less than or equal to 10^9, `A` is a list of `N` integers where each `A[i]` is between 1 and 10^6, `gcd` is the greatest common divisor of all elements in the list `A`, `max_divisor` is equal to the largest divisor of `gcd`, and `i` is equal to `int(sqrt(gcd))`.
    print(max_divisor)
#Overall this is what the function does:The function accepts an integer `N` (between 2 and 500), a non-negative integer `K` (less than or equal to 10^9), and a list `A` of `N` integers (each between 1 and 10^6). It calculates the greatest common divisor (GCD) of all integers in the list `A` and then determines the largest divisor of this GCD. Finally, it prints the largest divisor. The function does not utilize the parameter `K`, which is irrelevant to its functionality.

