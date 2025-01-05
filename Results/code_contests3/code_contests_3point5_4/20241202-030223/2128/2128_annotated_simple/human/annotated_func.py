#State of the program right berfore the function call: **
def func():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        n, k = map(int, sys.stdin.readline().split(' '))
        
        arr = list(map(int, sys.stdin.readline().split()))
        
        arr = sorted(arr, reverse=True)
        
        ans = arr[0]
        
        if k >= n:
            k = n - 1
        
        for l in range(1, k + 1):
            ans += arr[l]
        
        print(ans)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `t` is still a positive integer, `n` is assigned a value, `arr` is a list of integers sorted in descending order, `ans` is the sum of the first `n` elements in the sorted array `arr`, `k` is equal to `n`, and the value of `ans` is printed.
#Overall this is what the function does:The function `func` reads input from the standard input, processes the data according to the given algorithm, and prints the result. It reads an integer `t`, then for each iteration, it reads two integers `n` and `k`, followed by a list of integers `arr`. It sorts `arr` in descending order, calculates the sum of the first `n` elements in `arr`, adjusts `k` if it exceeds `n - 1`, sums up to the first `k + 1` elements in the sorted array, and prints the final sum `ans`. The function does not accept any parameters and does not return any value.

