#State of the program right berfore the function call: n, m, r, and k are all integers such that 1 ≤ n, m ≤ 10^5, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n·m, 10^5).
def func():
    n, m, r, k = map(int, input().split())
    ans = min(k, (n - r + 1) * (m - r + 1))
    print(ans / ((n - r + 1) * (m - r + 1)))
#Overall this is what the function does:The function accepts user input for four integers: n, m, r, and k, which represent dimensions and constraints related to a grid layout (where 1 ≤ n, m ≤ 10^5, 1 ≤ r ≤ min(n, m), and 1 ≤ k ≤ min(n·m, 10^5)). It calculates the minimum value between k and the total number of positions available in a reduced n by r and m by r grid, specifically (n - r + 1) * (m - r + 1). Then it computes the ratio of this minimum value to the total number of available positions, printing this result. The function does not have a return value, and edge cases such as r being equal to n or m are addressed through its calculations, ensuring no division by zero occurs since both n and m must always be at least r. Overall, the output reflects the density of positions limited by k in the adjusted grid size.

