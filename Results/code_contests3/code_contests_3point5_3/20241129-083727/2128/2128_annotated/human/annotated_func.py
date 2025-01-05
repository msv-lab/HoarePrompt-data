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
        
    #State of the program after the  for loop has been executed: `t` is an input integer, `n`, `k`, `k+1`, `arr`, `ans`, `l` are unchanged, `i` is `t`, `k` is `n-1`, `ans` is the sum of the largest element in the list `arr` and all elements from index 1 to `n-1`
#Overall this is what the function does:The function reads an integer `t` from the standard input and then for each iteration up to `t`, it reads two integers `n` and `k`, followed by a list of integers `arr`. It sorts the list in descending order, calculates the sum of the largest element and the next `k` elements, with the constraint that `k` cannot exceed `n-1`. The function then prints the sum. The function does not accept any parameters and does not return any values.

