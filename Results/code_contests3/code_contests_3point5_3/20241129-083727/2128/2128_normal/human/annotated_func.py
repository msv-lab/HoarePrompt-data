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
        
    #State of the program after the  for loop has been executed: `t` is an integer, `n` is an integer, `k` is an integer, `arr` is a list of integers sorted in reverse order, `ans` is the sum of the first `k + 1` elements of the list `arr` for each value of `t`
#Overall this is what the function does:The function reads an integer `t` from the standard input and then iterates `t` times. For each iteration, it reads two integers `n` and `k`, followed by a list of integers `arr`. It sorts `arr` in reverse order, calculates the sum of the first `k + 1` elements of `arr`, and prints the result. The function does not accept any parameters and does not have a return value.

