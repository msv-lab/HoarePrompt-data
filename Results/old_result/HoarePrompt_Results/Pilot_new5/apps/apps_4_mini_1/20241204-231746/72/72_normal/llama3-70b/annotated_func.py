#State of the program right berfore the function call: n and m are integers representing the number of rows and seats per row respectively, both greater than or equal to 1 and less than or equal to 100; k is a positive integer representing the number of questions asked, which can be as large as 10^18; x is an integer representing the row number where Sergei sits, between 1 and n; y is an integer representing the seat number where Sergei sits, between 1 and m.
def func():
    n, m, k, x, y = map(int, input().split())
    max_asked = (k + (n - 1)) // (2 * n)
    min_asked = max(1, max_asked - (n - 1))
    sergei_asked = (k + x - 1) // (2 * n) + ((k + x - 1) % (2 * n) >= n - x + 1)
    print(max_asked, min_asked, sergei_asked)
#Overall this is what the function does:The function accepts five integer inputs: `n` (number of rows), `m` (number of seats per row), `k` (number of questions asked), `x` (the row number where Sergei sits), and `y` (the seat number where Sergei sits). It calculates three values: the maximum number of questions that can be asked (`max_asked`), the minimum number of questions that must be asked (`min_asked`), and the number of questions that Sergei could potentially be asked (`sergei_asked`). These values are printed as output. The function does not return any values. Note that `m` is unused in the calculations.

