#State of the program right berfore the function call: N is an integer such that 2 <= N <= 500, K is an integer such that 0 <= K <= 10^9, A_i are integers such that 1 <= A_i <= 10^6 for 1 <= i <= N.**
def func():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
        
    #State of the program after the  for loop has been executed: N, K, A_i, gcd where gcd is equal to the greatest common divisor of all elements in A
    max_divisor = gcd
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            max_divisor = max(max_divisor, i)
            if i * i != gcd:
                max_divisor = max(max_divisor, gcd // i)
        
    #State of the program after the  for loop has been executed: N, K, A_i, gcd, max_divisor are integers. After the loop executes, max_divisor will be updated to the maximum value between the current max_divisor and gcd//i, where i is the last integer in the range from 1 to int(math.sqrt(gcd)) + 1 for which gcd % i == 0 and i*i is not equal to gcd.
    print(max_divisor)
#Overall this is what the function does:The function reads an integer N and another integer K followed by a list of N integers A. It then calculates the greatest common divisor (gcd) of all elements in A and finds the maximum divisor of the gcd by iterating up to the square root of gcd. The function finally prints the maximum divisor. The function operates on the assumption that input constraints are met, and the gcd calculation is correctly implemented.

