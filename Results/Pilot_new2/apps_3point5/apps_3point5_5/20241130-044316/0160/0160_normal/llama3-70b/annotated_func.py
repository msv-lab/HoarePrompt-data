#State of the program right berfore the function call: N is an integer such that 2 <= N <= 500, A_i is an integer such that 1 <= A_i <= 10^6 for all i from 1 to N, and K is an integer such that 0 <= K <= 10^9.**
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 500, A_i is an integer such that 1 <= A_i <= 10^6 for all i from 1 to N, K is an integer such that 0 <= K <= 10^9, N and K are input integers obtained by splitting the input, gcd is equal to the greatest common divisor of all elements in list A
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 500, A_i is an integer such that 1 <= A_i <= 10^6 for all i from 1 to N, K is an integer such that 0 <= K <= 10^9, gcd is a positive integer, the square root of gcd is an integer, all elements in list A are considered for calculating gcd, max_divisor is the maximum divisor of gcd
    print(max_divisor)
#Overall this is what the function does:The function `func` reads input values N, K, and a list A of N integers within specified constraints. It calculates the greatest common divisor (gcd) of all elements in list A. Then, it finds the maximum divisor of the gcd up to its square root and prints this maximum divisor. The function does not accept any parameters explicitly, but it operates based on the provided input constraints.

