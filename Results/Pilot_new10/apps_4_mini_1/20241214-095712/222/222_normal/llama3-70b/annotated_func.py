#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 1000 and 0 <= k <= 1000.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` must be at least `k + 2`, `k` is an integer such that 0 <= `k` <= 1000, `l` is equal to (n + k - 1) // (k * 2 + 1), `res` contains a list of length `l` with elements being 1, (k * 2 + 2), (4k + 3), ..., (i * (k * 2 + 1) + 1) for each `i` in the range from 0 to `l-1`.
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two integers, `n` and `k`, input via standard input, where `1 <= n <= 1000` and `0 <= k <= 1000`. It calculates the integer `l` as the ceiling of `(n + k) / (k * 2 + 1)` and generates a list of length `l`, where each element is calculated based on the formula `(i * (k * 2 + 1) + 1)`. It then prints the value of `l` and the elements of the list `res` as space-separated values. This function does not handle cases where the inputs might violate the specified bounds or provide any type of error feedback for invalid inputs.

