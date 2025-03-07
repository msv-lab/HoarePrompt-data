#State of the program right berfore the function call: The function `func_1` is expected to be part of a larger solution that processes multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of friends, and a list `p` of length `n` containing integers (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) where `p_i` is the best friend of the i-th friend. The function should calculate and return the minimum number of invitations required to ensure at least 2 friends come to the party.
def func_1():
    n = int(input())
    v = [0] * (n + 1)
    v = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if v[v[i]] == i:
            print(2)
            return
        
    #State: `n` is an integer between 2 and 50, inclusive, `i` is `n + 1`, `v` is a list of length `n + 1` where the first element is 0 and the remaining elements are integers provided by the user. If for any `i` from 1 to `n`, `v[v[i]]` is equal to `i`, the program prints 2 and returns. Otherwise, the program does not print anything and does not return.
    print(3)
    #This is printed: 3
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any value. It reads an integer `n` from the user, representing the number of friends, and a list `p` of length `n` from the user, where each element `p_i` indicates the best friend of the i-th friend. The function then checks if there is a pair of friends who are each other's best friends. If such a pair is found, it prints `2` and returns. If no such pair is found, it prints `3` and returns. The final state of the program is that it has printed either `2` or `3` to the console, depending on whether a mutual best friend pair was found.

