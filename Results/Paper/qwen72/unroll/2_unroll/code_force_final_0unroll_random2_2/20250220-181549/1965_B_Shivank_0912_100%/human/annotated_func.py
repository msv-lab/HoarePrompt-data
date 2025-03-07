#State of the program right berfore the function call: n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
def func():
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: The values of `n` and `k` are unchanged for each iteration of the loop, but the loop prints the length of the `ans` list and the elements of the `ans` list for each test case `t`. The `ans` list is recalculated for each test case, so the final state of `n`, `k`, and `t` remains the same as the initial state.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `2 <= n <= 10^6` and `1 <= k <= n`. The function calculates a list `ans` containing specific integers derived from `k` and prints the length of this list followed by the elements of the list. The values of `n` and `k` are unchanged for each test case, and the function does not return any value. The final state of the program after the function concludes is the same as the initial state, except for the output that has been printed to the console.

