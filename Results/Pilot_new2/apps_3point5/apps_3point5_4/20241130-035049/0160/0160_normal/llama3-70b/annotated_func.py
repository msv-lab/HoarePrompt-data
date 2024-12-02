#State of the program right berfore the function call: N and K are integers such that 2 <= N <= 500, 0 <= K <= 10^9. A_1, A_2, ..., A_N are positive integers where 1 <= A_i <= 10^6 for all i.**
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: N is at least 2, gcd is updated to the greatest common divisor of all elements in list A
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: N is at least 2, gcd is a positive integer, max_divisor is the greatest common divisor of all elements in list A
    print(max_divisor)
#Overall this is what the function does:The function `func` reads two integers N and K from input, then reads a list of N positive integers A. It calculates the greatest common divisor (gcd) of all elements in A and finds the maximum divisor of the gcd up to the square root of gcd. Finally, it prints the maximum divisor. The function operates under the constraints that N and K are integers such that 2 <= N <= 500, 0 <= K <= 10^9, and A_i values are positive integers where 1 <= A_i <= 10^6 for all i.

