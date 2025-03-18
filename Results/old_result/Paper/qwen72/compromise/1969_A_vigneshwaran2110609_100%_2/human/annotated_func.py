#State of the program right berfore the function call: The function should handle multiple test cases. Each test case consists of an integer n (2 ≤ n ≤ 50) representing the number of friends, and a list p of n integers (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) representing the best friends of each friend. The function should return the minimum number of invitations required for at least 2 friends to attend the party.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == i + 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: `i` is `n-1`, `x` is the last input integer, `l` is the last list of integers provided by the user, `flag` is either `True` or `False` depending on whether the condition `l[l[i] - 1] == i + 1` was met at any point during the loop.
#Overall this is what the function does:The function reads an integer `n` from the user, representing the number of test cases. For each test case, it reads an integer `x` and a list `l` of `x` integers. It then checks if there exists a pair of friends who are each other's best friends. If such a pair is found, the function prints `2`; otherwise, it prints `3`. The function does not return any value. After the function concludes, `n` test cases have been processed, and for each test case, either `2` or `3` has been printed to the console.

