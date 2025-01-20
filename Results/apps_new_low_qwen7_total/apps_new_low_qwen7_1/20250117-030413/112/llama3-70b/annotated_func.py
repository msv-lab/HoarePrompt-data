#State of the program right berfore the function call: n is a non-negative integer such that 1 ≤ n ≤ 10^15, and k is a positive integer such that 1 ≤ k ≤ 10^9.
def func():
    n, k = map(int, input().split())

divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `divisors` is a list containing all divisors of `n`, including each divisor exactly once.
    divisors.sort()
    if (k > len(divisors)) :
        print(-1)
    else :
        print(divisors[k - 1])
    #State of the program after the if-else block has been executed: `divisors` is a list containing all divisors of `n`, including each divisor exactly once, and it is sorted in ascending order; if `k` is greater than the length of `divisors`, the console displays `-1`. Otherwise, the value of `divisors[k - 1]` is printed.
#Overall this is what the function does:The function processes two variables, `n` and `k`, where \(1 \leq n \leq 10^{15}\) and \(1 \leq k \leq 10^9\). It calculates and prints the \(k\)-th smallest divisor of `n`. If `n` is a prime number or if `k` exceeds the total number of divisors of `n`, the function prints `-1`. After the function executes, the program will have determined and printed the \(k\)-th smallest divisor of `n` if it exists, or `-1` otherwise. Note that the function reads `n` and `k` from standard input, sorts the list of divisors, and then checks and prints the required divisor based on the value of `k`.

