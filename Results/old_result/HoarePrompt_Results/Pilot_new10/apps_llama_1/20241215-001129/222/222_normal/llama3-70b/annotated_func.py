#State of the program right berfore the function call: n is an integer such that 1 <= n <= 1000, and k is an integer such that 0 <= k <= 1000, representing the number of skewers and the number of skewers from each side that are turned in one step, respectively.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `k` is an input integer, `l` is `(n + k - 1) // (k * 2 + 1)`, if `l` is 0 then `res` is an empty list, otherwise `res` is a list containing `l` elements where each element `j` at index `i` is `i * (k * 2 + 1) + 1`, `i` is `l-1`.
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two integer parameters `n` and `k` as input from the user, calculates the number of steps required to turn all skewers, generates a list of skewer positions, and prints the total number of steps and the list of skewer positions, without handling invalid input values outside the specified ranges.

