#State of the program right berfore the function call: The function should be designed to handle multiple test cases. Each test case includes an integer n (2 ≤ n ≤ 50) representing the number of friends, and a list of integers p of length n (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) representing the best friends of each friend. The function should return the minimum number of invitations required for at least 2 friends to attend the party.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop will print either 2 or 3 for each test case, depending on whether there is a pair of friends who are best friends with each other. The variables `n`, `x`, `l`, and `flag` will be in their final states after the loop has executed, but their specific values will depend on the input. The variable `n` will remain unchanged, `x` will be the last input value for the number of friends in the current test case, `l` will be the last list of best friends for the current test case, and `flag` will be `True` if a pair of mutual best friends was found in the last test case, otherwise it will not be set or will remain `False`.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of an integer `n` representing the number of friends, followed by a list of integers `p` of length `n` representing the best friends of each friend. For each test case, the function prints either 2 or 3 to the standard output, indicating the minimum number of invitations required for at least 2 friends to attend the party. Specifically, it prints 2 if there is at least one pair of friends who are mutual best friends, and 3 otherwise. The function does not return any value.

