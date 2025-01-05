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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `t` is greater than 0, `i` is equal to `t-1`, `n` and `k` have assigned values, `arr` is a list of integers sorted in descending order with at least `k` elements, `ans` is the sum of the first `k+1` elements in the list `arr`, `k` is equal to the value of `n - 1` if `k` is greater than or equal to `n`, otherwise retains its previous value.
#Overall this is what the function does:The function `func` reads input from the standard input, processes it according to the given conditions, and prints the result. It reads an integer `t` from input, then for each iteration up to `t`, it reads two integers `n` and `k`, followed by a list of integers `arr`. The function sorts `arr` in descending order, calculates the sum of the first `k+1` elements in `arr`, and prints the result. If `k` is greater than or equal to `n`, `k` is set to `n-1`.

