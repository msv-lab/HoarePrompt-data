#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^15, and k is a positive integer such that 1 ≤ k ≤ 10^9.
def func():
    n, k = map(int, input().split())

divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `total` is unspecified, `k` is a positive integer such that 1 ≤ k ≤ 10^9, `divisors` is a list containing all unique divisors of `n`, and `n` is a positive integer such that 1 ≤ n ≤ 10^15. The variable `i` remains within the range of 1 to int(n
    divisors.sort()
    if (k > len(divisors)) :
        print(-1)
    else :
        print(divisors[k - 1])
    #State of the program after the if-else block has been executed: *`total` is unspecified, `k` is a positive integer such that 1 ≤ k ≤ 10^9, `divisors` is a list containing all unique divisors of `n` in sorted order, `n` is a positive integer such that 1 ≤ n ≤ 10^15, and `i` remains within the range of 1 to int(n). If `k` is greater than the length of `divisors`, -1 is printed. Otherwise, the value of `divisors[k - 1]` is printed.
#Overall this is what the function does:The function reads two integers `n` and `k` from the standard input, where `n` is a positive integer between 1 and \(10^{15}\) inclusive, and `k` is a positive integer between 1 and \(10^9\) inclusive. It then calculates all unique divisors of `n` and sorts them in ascending order. If `k` is greater than the number of divisors of `n`, it prints `-1`. Otherwise, it prints the `k-th` smallest divisor of `n`. If `k` equals the number of divisors, the function will print the largest divisor. The function does not accept any parameters and returns no value, but prints the result directly. Potential edge cases include when `n` is a prime number, in which case the function will only have two divisors (1 and `n` itself).

