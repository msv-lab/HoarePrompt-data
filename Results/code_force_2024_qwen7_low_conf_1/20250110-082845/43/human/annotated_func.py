#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a list of integers a_2, ..., a_n is provided such that 1 ≤ a_i < i, indicating the edges in the tree, and a string s of length n consisting of characters 'P', 'S', and 'C' indicating the type of each student. The sum of n over all test cases does not exceed 10^5.
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
        
    #State of the program after the  for loop has been executed: t is an integer such that 1 ≤ t ≤ 1000, for each test case: n is an integer such that 2 ≤ n ≤ 10^5, fa is a list of integers where fa[i] (0-indexed) is the parent of node i+1 in the tree, S is a string of length n consisting of characters 'P', 'S', and 'C', dp1 and dp2 are lists of integers where dp1[i] represents the minimum cost to reach a leaf node starting from node i (considering only paths through nodes marked 'P' or 'S'), and dp2[i] represents the same but considering only paths through nodes marked 'S' or 'P'. After processing all test cases, the output of the print statement is the minimum of dp1[0] and dp2[0].
#Overall this is what the function does:The function processes multiple test cases, each consisting of a tree structure defined by a list of edges and a string indicating the type of each student. For each test case, it calculates the minimum cost to reach a leaf node starting from the root, considering two different scenarios: one where the path can only go through nodes marked 'P' or 'S', and another where the path can only go through nodes marked 'S' or 'P'. It then prints the minimum cost among these two scenarios for each test case.

