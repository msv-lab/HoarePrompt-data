#State of the program right berfore the function call: The function `func_1` is expected to be part of a larger program that processes multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of friends, and a list `p` of length `n` containing integers (1 ≤ p_i ≤ n; p_i ≠ i; all p_i are distinct) representing the best friends of each friend. The function should calculate and return the minimum number of invitations needed for at least 2 friends to attend the party.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `v` is a list of length `n + 1` where the first element is 0 and the remaining elements are integers provided by the user, `n` is an input integer between 2 and 50, `i` is `n + 1`, and `v[v[i]]` is not equal to `i` for any `i` in the range from 1 to `n`. The program returns nothing.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `p` of integers from user input. It checks if there are any pairs of friends in the list `p` where each friend is the best friend of the other. If such a pair is found, it prints `2` and returns. If no such pair is found, it prints `3` and returns. The function does not accept any parameters and does not return any value.

