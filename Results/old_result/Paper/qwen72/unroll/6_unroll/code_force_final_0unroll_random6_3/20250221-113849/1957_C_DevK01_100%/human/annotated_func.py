#State of the program right berfore the function call: n is a positive integer representing the size of the chessboard, and it is guaranteed that 1 ≤ n ≤ 3 · 10^5.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: `dp` is a list with two elements, where the first element is the last computed value of the sequence and the second element is the second last computed value of the sequence. The length of the list remains 2.
    return dp[-1]
    #The program returns the last computed value of the sequence, which is the first element of the list `dp`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` (1 ≤ n ≤ 3 · 10^5) representing the size of a chessboard. It computes a sequence of values based on a specific formula and returns the last computed value of this sequence. The sequence is calculated using dynamic programming, and the function ensures that only the last two computed values are stored in the list `dp` at any point. After the function concludes, the list `dp` contains the last two values of the sequence, but only the last computed value (the first element of `dp`) is returned.

