#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. n and k are integers such that 1 <= k < n <= 2 * 10^5. a_i is an integer such that 0 <= a_i <= 10^9.**
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
        
    #State of the program after the  for loop has been executed: `t`, `n`, `k`, `arr` are integers from input, `ans` is the sum of the first `k` elements in the sorted list `arr`, `l` is equal to `k`, for the loop to execute `k` must be less than `n`
#Overall this is what the function does:The function `func` reads an integer `t` from the input and then iterates `t` times. For each iteration, it reads two integers `n` and `k`, followed by a list of integers `arr`. It sorts the list `arr` in reverse order, calculates the sum of the first `k` elements (or all elements if `k >= n`), and prints the sum. The function does not accept any parameters and does not return any specific value.

