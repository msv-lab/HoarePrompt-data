#State of the program right berfore the function call: N is an integer greater than or equal to 2, K is an integer greater than or equal to 0, A_i are positive integers where 1 <= A_i <= 10^6 for all i.**
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: N is an integer greater than or equal to 2, K is an integer greater than or equal to 0, A_i are positive integers where 1 <= A_i <= 10^6 for all i, N and K are assigned the values obtained from splitting the input by spaces, A is a list of integers obtained by mapping the input split by spaces to integers, gcd is assigned the value of the greatest common divisor (gcd) of all elements in the list A.
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, N, K, A_i are positive integers where 1 <= A_i <= 10^6 for all i. N is an integer greater than or equal to 2, K is an integer greater than or equal to 0. A is a list of integers obtained from splitting the input by spaces. gcd is the greatest common divisor of all elements in the list A. The square root of gcd is at least 1. i will be equal to the square root of gcd. After the if else block executes for each valid i, max_divisor is updated to the maximum of its current value and gcd divided by i.
    print(max_divisor)
#Overall this is what the function does:The function `func` reads two integers N, K and a list A of N positive integers. It then calculates the greatest common divisor (gcd) of all elements in A. After that, it finds the maximum divisor of the gcd up to its square root and prints it. The function does not directly return any value, but it effectively calculates and outputs the maximum divisor of the gcd based on the input values.

