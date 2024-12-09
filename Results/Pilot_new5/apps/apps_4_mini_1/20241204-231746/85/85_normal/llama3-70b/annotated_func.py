#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: - If the loop executes fully, `ans` will represent the total number of times the condition was satisfied for each `i` in the range. 
    #- If the loop does not execute (when `n` is 2), `ans` remains `0`.
    #
    #Output State:
    print(ans)
#Overall this is what the function does:The function accepts an integer input `n` (where 2 ≤ n ≤ 10^9) and counts how many integers `i` in the range from 1 to n/2 satisfy the condition that the sum of `i` and (n - i) is divisible by the highest place value of that sum. It then prints the count `ans`. The function does not return any value.

