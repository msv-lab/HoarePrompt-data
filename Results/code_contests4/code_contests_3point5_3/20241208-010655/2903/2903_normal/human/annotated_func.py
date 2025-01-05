#State of the program right berfore the function call: w and l are integers such that 1 ≤ l < w ≤ 10^5. The list of integers a contains w-1 elements where each element is between 0 and 10^4.**
def func():
    n, k, s, mn = map(int, raw_input().split() + [0, 10000000000])
    a = list(map(int, raw_input().split()))
    for i in range(0, n - 1):
        if i < k:
            s += a[i]
        else:
            mn = min(mn, s)
            s += a[i] - a[i - k]
        
    #State of the program after the  for loop has been executed: Output State: `n`, `k`, `s`, `mn` are integers and `a` is a list of integers. After all iterations of the loop have finished, `s` will contain the sum of elements in the list `a`, `mn` will contain the minimum value of the sum of elements in `a` with a window size of `k`.
    print(min(mn, s))
#Overall this is what the function does:The function `func` reads input values `n`, `k`, `s`, and `mn` from the user, along with a list of integers `a`. It then iterates over the elements of `a`, updating `s` and `mn` based on certain conditions. After all iterations, it prints the minimum value between `mn` and `s`. The functionality also requires `w` and `l` to be integers such that 1 ≤ l < w ≤ 10^5.

