#State of the program right berfore the function call: n is a positive integer (1 <= n <= 1000), and k is a non-negative integer (0 <= k <= 1000).
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `k` is a non-negative integer, `l` is the result of (n + k - 1) // (k * 2 + 1), `i` is `l - 1`, `res` is a list containing `l` elements with values [1, k * 2 + 2, 2k + 3, ..., (l - 1) * (k * 2 + 1) + 1].
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two integers, `n` (a positive integer between 1 and 1000) and `k` (a non-negative integer between 0 and 1000), reads them from input, computes the value of `l` as the ceiling of `n` divided by `(2k + 1)`, and generates a list `res` containing `l` elements, where each element follows the pattern `i * (2k + 1) + 1`. It then prints the value of `l` and the elements of `res` as a space-separated string. The function does not return any values but outputs results to standard output.

