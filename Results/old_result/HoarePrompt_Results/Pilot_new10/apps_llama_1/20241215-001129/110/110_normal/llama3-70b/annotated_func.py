#State of the program right berfore the function call: n, m, r, and k are integers such that 1 <= n, m <= 10^5, 1 <= r <= min(n, m), and 1 <= k <= min(n*m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts integers n, m, r, and k as input, calculates the minimum of k and the area of a rectangle with sides (n - r + 1) and (m - r + 1), and then prints the ratio of this minimum value to the area of the rectangle, but does not handle potential edge cases such as division by zero or out-of-range inputs, and does not return any value, instead, it prints the result.

