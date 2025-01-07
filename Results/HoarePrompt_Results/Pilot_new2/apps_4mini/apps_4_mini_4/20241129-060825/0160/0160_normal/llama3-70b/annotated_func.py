#State of the program right berfore the function call: N is an integer between 2 and 500, K is a non-negative integer not exceeding 10^9, and A is a list of N integers where each integer A_i is between 1 and 10^6.
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `K` is a non-negative integer not exceeding 10^9, `A` is a list of integers, `gcd` is equal to the greatest common divisor of all elements in list `A`.
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `K` is a non-negative integer not exceeding 10^9, `A` is a list of integers, `gcd` is at least 1, and `max_divisor` is the largest divisor of `gcd` (including `gcd` itself). The loop will execute a maximum of `int(math.sqrt(gcd))` times, which means that if `gcd` is 1, `max_divisor` will remain 1 and `i` will be 1, while if `gcd` is greater than 1, `max_divisor` will be updated to the largest divisor found in the range from 1 to `int(math.sqrt(gcd))`.
    print(max_divisor)
#Overall this is what the function does:The function accepts an integer `N` (between 2 and 500), a non-negative integer `K` (not exceeding 10^9), and a list `A` of `N` integers (each between 1 and 10^6). It calculates the greatest common divisor (GCD) of the integers in the list `A`, then finds and prints the largest divisor of this GCD. If the GCD is 1, the function will print 1, as 1 is the only divisor of 1. The function does not utilize the parameter `K` in any computation.

