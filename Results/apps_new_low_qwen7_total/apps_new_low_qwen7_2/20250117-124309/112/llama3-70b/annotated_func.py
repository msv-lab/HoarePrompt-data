#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^15, and k is an integer such that 1 ≤ k ≤ 10^9.
def func():
    n, k = map(int, input().split())

divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        
    #State of the program after the  for loop has been executed: `i` is equal to the integer part of the square root of `n`, `n` is a positive integer, and `divisors` is a list containing all divisors of `n` found during the loop execution. Specifically, `divisors` contains all integers `i` such that `1 ≤ i ≤ √n` and `n % i == 0`. If `i * i != n`, `n // i` is also included in `divisors`. If `i * i == n`, only `i` is included.
    divisors.sort()
    if (k > len(divisors)) :
        print(-1)
    else :
        print(divisors[k - 1])
    #State of the program after the if-else block has been executed: *`i` is equal to the integer part of the square root of `n`, `n` is a positive integer, and `divisors` is a sorted list containing all relevant divisors of `n`. If `k` is greater than the length of `divisors`, the function does not return anything (or the postcondition remains unchanged). Otherwise, the function returns the `(k-1)`-th element of `divisors`.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is an integer between 1 and \(10^{15}\) inclusive, and `k` is an integer between 1 and \(10^{9}\) inclusive. It calculates all divisors of `n` and sorts them. If `k` is greater than the number of divisors of `n`, it prints `-1`; otherwise, it prints the `k`-th smallest divisor of `n`. Potential edge cases include when `n` is a perfect square, where both the square root and its corresponding pair divisor would be included in the list of divisors. The function does not handle cases where the input values do not meet the specified ranges, which could lead to undefined behavior.

