#State of the program right berfore the function call: n is an even integer representing the size of the chessboard, and the list of initial positions contains distinct integers between 1 and n.**
def func():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    p = [(pi - 1) for pi in p]
    even = odd = 0
    for i in range(n / 2):
        even += abs(i * 2 - p[i])
        
        odd += abs(i * 2 + 1 - p[i])
        
    #State of the program after the  for loop has been executed: n is an even integer representing the size of the chessboard and at least 2, p is a list containing distinct integers between 0 and n-1, even is the sum of absolute differences between i * 2 and p[i] for all i, odd is the sum of absolute differences between i * 2 + 1 and p[i] for all i
    print(min(even, odd))
#Overall this is what the function does:The function `func` reads an even integer `n` representing the size of a chessboard and a list of initial positions, calculates the sum of absolute differences between the positions and their corresponding expected positions on the chessboard (based on even and odd indices), and prints the minimum value between the two sums. The function does not return any value directly.

