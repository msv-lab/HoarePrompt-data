#State of the program right berfore the function call: n and m are integers such that 1 <= n <= 30 and 1 <= m <= 30; r is an integer such that 1 <= r <= 1000; s is a list of n integers where each integer s_i is such that 1 <= s_i <= 1000; b is a list of m integers where each integer b_i is such that 1 <= b_i <= 1000.
def func():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s.sort()
    b.sort(reverse=True)
    shares = 0
    for i in range(n):
        if r >= s[i]:
            shares += r // s[i]
            r %= s[i]
        else:
            break
        
    #State of the program after the  for loop has been executed: `shares` is the total number of shares acquired, `r` is the remaining amount after possible deductions based on `s`, and `s` is a sorted list of integers such that 1 <= `s_i` <= 1000.
    for i in range(m):
        if shares > 0:
            r += shares * b[i]
            shares = 0
        else:
            break
        
    #State of the program after the  for loop has been executed: `shares` is 0, `r` is updated based on the total shares acquired multiplied by the elements of `b`, `s` is a sorted list of integers such that 1 <= `s_i` <= 1000, `m` is the total number of iterations that were possible based on the length of `b`, and `i` is the index of the last iteration executed, which will be less than `m` or equal to `m-1` if `shares` was initially greater than 0. If `shares` was initially 0, then `r` remains unchanged, and the loop does not execute.`
    print(r)
#Overall this is what the function does:The function accepts integers `n` and `m` which represent the lengths of the lists `s` and `b` respectively, along with an integer `r` which denotes the initial amount of resources. It reads two lists of integers, `s` (representing the costs of shares) and `b` (representing some multipliers), sorts `s` in ascending order and `b` in descending order. It calculates the total number of shares that can be acquired with `r` based on the costs in `s`, and uses this number to update `r` by multiplying it with the values in `b`. Finally, it prints the resulting value of `r`. If no shares are acquired, `r` remains unchanged. The function does not handle edge cases where `s` or `b` is empty, and will only work correctly when both lists have valid elements as per the constraints provided.

