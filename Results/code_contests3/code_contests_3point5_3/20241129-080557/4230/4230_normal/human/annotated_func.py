#State of the program right berfore the function call: n is an integer such that 2 <= n <= 200,000. The sequence of integers represents the doors opened by Mr. Black, where 0 indicates a door in the left exit and 1 indicates a door in the right exit.**
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `c` is a mapped list of integers from input. If there exists an index `i` such that `c[i]` is not equal to `c[i + 1]`, then `ans` will be updated to the value of that index + 1. If no such index exists, `ans` will remain 0 at the end of the loop.
    print(ans)
#Overall this is what the function does:The function `func` reads input data regarding the doors opened by Mr. Black, where 0 represents a door in the left exit and 1 represents a door in the right exit. It then iterates through the sequence of doors and finds the last index where the door direction changes. This index is stored in the variable `ans` and is printed as the final output. The function does not accept any parameters and does not return any value.

