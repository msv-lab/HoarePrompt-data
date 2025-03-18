#State of the program right berfore the function call: n and m are integers representing the number of rows and seats respectively, k is a positive integer representing the total number of questions asked, and x and y are integers representing Sergei's position in the seating arrangement such that 1 ≤ x ≤ n and 1 ≤ y ≤ m.
def func():
    n, m, k, x, y = map(int, input().split())
    max_asked = (k + (n - 1)) // (2 * n)
    min_asked = max(1, max_asked - (n - 1))
    sergei_asked = (k + x - 1) // (2 * n) + ((k + x - 1) % (2 * n) >= n - x + 1)
    print(max_asked, min_asked, sergei_asked)
#Overall this is what the function does:The function accepts five integer parameters: n (number of rows), m (number of seats), k (total questions asked), x (Sergei's row position), and y (Sergei's seat position). It computes and prints three values: the maximum number of questions asked by any student, the minimum number of questions that could have been asked by a student, and the number of questions Sergei is estimated to have asked based on his position.

