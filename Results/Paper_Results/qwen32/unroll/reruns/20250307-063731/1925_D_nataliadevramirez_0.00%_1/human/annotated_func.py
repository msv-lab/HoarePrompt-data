#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing a pair of friends and their friendship value. It is guaranteed that 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5, and 1 <= f <= 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: result is the accumulated sum of f * (k * (k + 1) // 2) % MOD for all friendships.
    return result % MOD
    #The program returns the accumulated sum of f * (k * (k + 1) // 2) % MOD for all friendships, taken modulo MOD.
#Overall this is what the function does:The function calculates and returns the accumulated sum of the product of each friendship's value and the triangular number of excursions, taken modulo `MOD`.

#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of lists where each sublist contains three integers [a_i, b_i, f_i] representing the indices of the pair of friends and their friendship value. It is guaranteed that 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5, a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: `n`, `m`, `k`, and `friendships` will be the values from the last iteration of the loop, and `t` remains unchanged.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of the number of children, the number of pairs of friends, the number of excursions, and a list of friendships with their respective friendship values. It then calculates and prints the maximum total friendship value that can be achieved by organizing the children into the specified number of excursions for each test case.

