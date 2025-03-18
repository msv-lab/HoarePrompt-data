#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of friends, and a list of integers `p` of length `n` where each element `p_i` (1 ≤ p_i ≤ n, p_i ≠ i, all `p_i` are distinct) represents the best friend of the i-th friend. The function should be able to process these inputs to determine the minimum number of invitations required for at least 2 friends to attend the party.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: Output State: The loop iterates through each test case. For each test case, it checks if there is a pair of friends (i, i+1) such that the best friend of the i-th friend is (i+2) and the best friend of the (i+1)-th friend is (i+1). If such a pair is found, it prints 2 and sets `j` to 1, breaking out of the loop. If no such pair is found, it prints 3. After processing all test cases, the loop finishes. The variables `n` and `l` are reset for each test case, and `i` and `j` are used within the loop for each test case but are reset to 0 at the start of each iteration. Therefore, the output state is the same as the initial state, with the function having processed all test cases and printed the required output for each one.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` (2 ≤ n ≤ 50) and a list `l` of length `n` where each element `l[i]` (1 ≤ l[i] ≤ n, l[i] ≠ i, all `l[i]` are distinct) represents the best friend of the i-th friend. It checks if there is a pair of friends (i, i+1) such that the best friend of the i-th friend is (i+2) and the best friend of the (i+1)-th friend is (i+1). If such a pair is found, it prints 2. If no such pair is found, it prints 3. After processing all test cases, the function completes, and the state of the program is reset for the next test case. The function does not return any values; it only prints the results.

