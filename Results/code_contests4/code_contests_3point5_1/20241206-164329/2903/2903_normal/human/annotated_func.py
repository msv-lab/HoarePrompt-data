#State of the program right berfore the function call: w and l are integers such that 1 ≤ l < w ≤ 10^5. The list of stones a_i contains w - 1 integers where each integer is between 0 and 10^4.**
def func():
    n, k, s, mn = map(int, raw_input().split() + [0, 10000000000])
    a = list(map(int, raw_input().split()))
    for i in range(0, n - 1):
        if i < k:
            s += a[i]
        else:
            mn = min(mn, s)
            s += a[i] - a[i - k]
        
    #State of the program after the  for loop has been executed: `n`, `k`, `s`, and `mn` are integers with specific values, `a` is a list of integers. The loop will update `s` and `mn` based on the conditions specified in the loop code for all iterations of the loop. After all iterations of the loop have finished, `s` will be the sum of specific elements in list `a`, and `mn` will be the minimum value between its initial value and the specific calculations performed within the loop.
    print(min(mn, s))
#Overall this is what the function does:The function `func` reads input values for n, k, s, and mn, as well as a list of integers a. It then iterates through the list a, updating the values of s and mn based on certain conditions. The function calculates the minimum value between mn and s after the loop completes and prints the result. The function does not accept any explicit parameters but operates on the predefined inputs.

