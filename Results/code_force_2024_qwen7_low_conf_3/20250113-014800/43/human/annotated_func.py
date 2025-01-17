#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a list of n-1 integers a_2, ..., a_n such that 1 ≤ a_i < i, and a string s of length n consisting of characters 'P', 'S', and 'C'. The sum of n over all test cases does not exceed 10^5.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 10^5, `fa` is a list of length `n + 1` where the first element is -1 and the next `n` elements are integers from the input representing parent nodes, `S` is a string of length `n` consisting of characters 'P', 'S', and 'C', `dp1` and `dp2` are lists of length `n + 1` initialized to `float('inf')`, `dp1[0]` and `dp2[0]` are the minimum values between paths in the tree starting from the root node considering the constraints given by the string `S`, and the output of the print statement is the minimum value between `dp1[0]` and `dp2[0]`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( n \) (the number of nodes in a tree), a list of parent nodes, and a string \( s \) of length \( n \) consisting of characters 'P', 'S', and 'C'. It constructs a tree from the parent nodes and calculates two dynamic programming arrays, \( dp1 \) and \( dp2 \), which represent the minimum costs to reach the root node under specific conditions defined by the string \( s \). After processing all test cases, the function prints the minimum value between \( dp1[0] \) and \( dp2[0] \) for the last test case. Potential edge cases include invalid inputs such as \( n \) outside the specified range or invalid characters in the string \( s \). The function does not handle these edge cases directly but expects valid input according to the constraints.

