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
        
    #State of the program after the  for loop has been executed: `t` is an input integer greater than or equal to 1, `n` and `k` are input integers, `arr` is a list of integers sorted in descending order, `ans` is the sum of the first `k` elements in the sorted `arr` list. If `k` >= `n`, then `k` is assigned the value of `n - 1`. The sum of the first `k` elements of the sorted `arr` list is printed for each iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the standard input and then iterates `t` times. For each iteration, it reads two integers `n` and `k`, followed by a list of integers into `arr`. It sorts `arr` in descending order, calculates the sum of the first `k` elements, and prints the result. If `k` is greater than or equal to `n`, `k` is adjusted to `n - 1`. The function does not accept any parameters and does not return any value.

