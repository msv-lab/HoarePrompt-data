#State of the program right berfore the function call: n and m are integers representing the number of rows and pupils per row respectively, k is a positive integer indicating the total number of questions asked, x and y are integers indicating Sergei's position in the seating arrangement such that 1 <= x <= n and 1 <= y <= m.
def func():
    n, m, k, x, y = map(int, input().split())
    max_asked = (k + (n - 1)) // (2 * n)
    min_asked = max(1, max_asked - (n - 1))
    sergei_asked = (k + x - 1) // (2 * n) + ((k + x - 1) % (2 * n) >= n - x + 1)
    print(max_asked, min_asked, sergei_asked)
#Overall this is what the function does:The function accepts integers `n`, `m`, `k`, `x`, and `y` where `n` is the number of rows, `m` is the number of pupils per row, `k` is the total number of questions asked, and `x` and `y` represent Sergei's position in the seating arrangement. It calculates and prints three values: `max_asked`, which indicates the maximum number of questions asked per pupil based on rows, `min_asked`, which ensures that the minimum is at least 1, and `sergei_asked`, which reflects the number of questions asked specifically to Sergei based on his position. The function does not return a value but rather prints the results directly.

