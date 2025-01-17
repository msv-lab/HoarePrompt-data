#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a list a contains n-1 integers such that 1 ≤ a_i < i, indicating the edges of the tree, and s is a string of length n consisting of characters 'P', 'S', and 'C', indicating the type of each student. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        fa = [-1] + list(map(int, input().split()))
        
        S = input()
        
        dp1, dp2 = [0] * (n + 1), [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            if S[i] == 'S':
                dp1[i] = float('inf')
            elif S[i] == 'P':
                dp2[i] = float('inf')
            p = fa[i] - 1
            if p != -1:
                dp1[p] += min(dp1[i], dp2[i] + 1)
                dp2[p] += min(dp1[i] + 1, dp2[i])
        
        print(min(dp1[0], dp2[0]))
        
    #State of the program after the  for loop has been executed: `t` is an integer within the range \(1 \leq t \leq 1000\), `n` is the number of nodes in the tree, `fa` is the list where `fa[i]` is the parent of node `i+1`, `S` is the string indicating the type of each student, `dp1` and `dp2` are lists of length `n + 1` where `dp1[i]` and `dp2[i]` represent the minimum costs to reach the end of the string `S` under certain conditions starting from node `i+1`, and the minimum value between `dp1[0]` and `dp2[0]` is printed.
#Overall this is what the function does:- The function correctly handles the range constraints for the number of test cases (`1 ≤ t ≤ 1000`) and the number of nodes (`2 ≤ n ≤ 10^5`).
- However, the function assumes that the input format is always correct and does not include error handling for invalid inputs (e.g., non-integer values, incorrect lengths of `fa` or `S`).

The function performs the following actions:
- Reads the number of test cases.
- For each test case, it reads the number of nodes, constructs the parent relationship list `fa`, and reads the string `S`.
- It initializes two dynamic programming arrays `dp1` and `dp2` to store the minimum costs.
- It iterates backward through the nodes, updating the `dp1` and `dp2` arrays based on the type of each student in the string `S`.
- It prints the minimum value between `dp1[0]` and `dp2[0]`, which represents the minimum cost to reach the end of the string `S` under the specified conditions.

