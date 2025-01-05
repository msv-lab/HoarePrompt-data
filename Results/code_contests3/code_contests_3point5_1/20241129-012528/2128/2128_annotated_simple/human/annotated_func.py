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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `t` is a non-negative integer, `n` and `k` have new values, `arr` is a list of integers sorted in descending order, `ans` is increased by the sum of the first `k` elements in the list `arr`, `i` is incremented by the total number of elements in `arr`, and `l` is equal to `k + 1`.
#Overall this is what the function does:The function reads an integer `t` from the standard input, then for each iteration in the range of `t`, it reads integers `n` and `k`, followed by a list of integers `arr`, sorts the list in descending order, calculates a sum `ans` based on the elements in `arr` up to index `k`, and prints the final `ans` value. The function does not accept any parameters and does not return any value.

