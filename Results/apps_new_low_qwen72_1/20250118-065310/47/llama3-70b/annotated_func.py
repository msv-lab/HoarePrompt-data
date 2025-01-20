#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1,000,000.
def func():
    n, m = map(int, input().split())

count = 0
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x + y) % 5 == 0:
                count += 1
        
    #State of the program after the  for loop has been executed: `n` is the first integer read from input, `m` is the second integer read from input, `count` is the total number of pairs `(x, y)` where `x` is in the range [1, n] and `y` is in the range [1, m] such that `(x + y) % 5 == 0`.
    print(count)
#Overall this is what the function does:The function reads two positive integers `n` and `m` from the input, where both `n` and `m` are within the range 1 to 1,000,000. It then counts the number of pairs `(x, y)` where `x` is in the range [1, n] and `y` is in the range [1, m], such that the sum `(x + y)` is divisible by 5. Finally, the function prints the count of such pairs. The function does not return any value; it only prints the result.

