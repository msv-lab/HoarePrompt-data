#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case consists of an integer n (2 ≤ n ≤ 50) representing the number of friends, and a list of integers p of length n (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) where p_i represents the best friend of the i-th friend. The function should return the minimum number of invitations required for at least 2 friends to attend the party for each test case.
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
        
    #State: The loop iterates through each test case, and for each test case, it checks if there is a pair of friends (i, i+1) such that the best friend of the i-th friend is (i+1) and the best friend of the (i+1)-th friend is (i). If such a pair is found, it prints 2 and sets `j` to 1, breaking out of the loop. If no such pair is found, it prints 3. After all iterations, the loop finishes, and the values of `n` and `l` are reset for each new test case, while `i` and `j` are used within the loop and reset to 0 at the start of each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of integers `p` of length `n`. It checks if there is a pair of friends (i, i+1) such that the best friend of the i-th friend is (i+1) and the best friend of the (i+1)-th friend is (i). If such a pair is found, it prints 2. If no such pair is found, it prints 3. After processing all test cases, the function concludes.

