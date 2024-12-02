#State of the program right berfore the function call: N is an integer such that 2 <= N <= 500, K is an integer such that 0 <= K <= 10^9, A_i are integers such that 1 <= A_i <= 10^6 for 1 <= i <= N.**
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 500, K is an integer such that 0 <= K <= 10^9, A_i are integers such that 1 <= A_i <= 10^6 for 1 <= i <= N, A is a list of integers based on the input split, gcd is equal to the greatest common divisor of all elements in the list A
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 500, K is an integer such that 0 <= K <= 10^9, A_i are integers such that 1 <= A_i <= 10^6 for 1 <= i <= N, A is a list of integers based on the input split, gcd is equal to the greatest common divisor of all elements in the list A, max_divisor is the maximum between the previous max_divisor and int(math.sqrt(gcd)) + 1.
    print(max_divisor)
#Overall this is what the function does:The function `func` reads two integers N and K as input, along with a list of integers A. It then calculates the greatest common divisor (gcd) of all elements in A. After that, it finds the maximum divisor of the gcd up to the square root of the gcd. Finally, it prints the maximum divisor. The function does not have any return value specified.

