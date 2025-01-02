#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 105), and m1, m2, ..., mn are a sequence of n integers where 0 ≤ mi < i, representing the number of marks strictly above the water level on each day.
def func():
    n, a = int(input()), [int(x) for x in stdin.readline().split()]
    tem, tem2, ans = [], [0] * n, 0
    for i in range(n):
        if not tem or a[i] > a[tem[-1]]:
            tem.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 105), `a` is a list of `n` integers where 0 ≤ mi < i, `tem` is a list of indices where each element in `a` at these indices is strictly greater than the previous element in `a` up to that index, `tem2` is a list of `n` zeros, `ans` is 0, `i` is `n-1`.
    tem.append(n - 1)
    for i in range(len(tem) - 1, 0, -1):
        cur = max(a[tem[i]], a[tem[i - 1]])
        
        for j in range(tem[i], tem[i - 1], -1):
            tem2[j] = cur
            cur = max(a[tem[i - 1]], cur - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 105), `a` is a list of `n` integers where 0 ≤ mi < i, `tem` is a list of indices where each element in `a` at these indices is strictly greater than the previous element in `a` up to that index, `tem` includes `n-1`, `tem2` is a list of `n` integers where each element `tem2[j]` is set to the maximum value between the corresponding element in `a` at the index from `tem` and the decrementing value of `cur`, starting from the last element in `tem` and moving backwards, `ans` is 0, `i` is 0 (indicating the loop has completed its execution).
    for i in range(n):
        ans += max(tem2[i] - a[i], 0)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 105), `a` is a list of `n` integers where 0 ≤ mi < i, `tem` is a list of indices where each element in `a` at these indices is strictly greater than the previous element in `a` up to that index, and `tem` includes `n-1`, `tem2` is a list of `n` integers where each element `tem2[j]` is set to the maximum value between the corresponding element in `a` at the index from `tem` and the decrementing value of `cur`, starting from the last element in `tem` and moving backwards, `ans` is the sum of `max(tem2[i] - a[i], 0)` for all `i` from 0 to `n-1`, `i` is `n-1`.
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `n` (1 ≤ n ≤ 105) and a list of `n` integers `a` where each element `ai` satisfies 0 ≤ ai < i. It then processes these inputs to calculate and print the total "water trapped" between the elements of `a`. The function constructs a list `tem` of indices where each element in `a` at these indices is strictly greater than the previous element. It uses this list to fill another list `tem2` with values that represent the maximum height of water that can be trapped at each position. Finally, it calculates the total amount of water trapped by summing the differences between the values in `tem2` and `a`, and prints this total. The function does not return any value; it only prints the result. Potential edge cases include when `n` is 1 (no water can be trapped), or when all elements in `a` are in non-decreasing order (minimal or no water trapped).

