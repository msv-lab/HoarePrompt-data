#State of the program right berfore the function call: N is an integer between 2 and 500, K is a non-negative integer up to 10^9, and A is a list of N integers where each integer is between 1 and 10^6.
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: `N` is between 2 and 500, `K` is a non-negative integer up to 10^9, `A` is a list of integers that must have at least 2 elements, `gcd` is now `math.gcd(A[0], A[1], ..., A[N-1])`
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: `N` is between 2 and 500, `K` is a non-negative integer up to 10^9, `A` is a list of integers that has at least 2 elements, `gcd` is greater than or equal to 1, `max_divisor` is the largest divisor of `gcd`, and `i` is greater than or equal to 1 and less than or equal to `int(math.sqrt(gcd))`.
    print(max_divisor)
#Overall this is what the function does:The function accepts an integer `N` (between 2 and 500), a non-negative integer `K` (up to 10^9), and a list `A` containing `N` integers (each integer between 1 and 10^6). It calculates the greatest common divisor (gcd) of the integers in the list `A`, then finds and prints the largest divisor of that gcd. The function does not utilize the parameter `K` in any way, which is a potential oversight.

