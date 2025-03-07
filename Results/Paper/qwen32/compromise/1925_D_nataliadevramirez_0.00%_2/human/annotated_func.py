#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing a pair of friends and their friendship value.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: `n` is an integer representing the number of children, `m` is an integer representing the number of pairs of friends, `k` is an integer representing the number of excursions, `friendships` is a list of tuples where each tuple contains three integers (a, b, f) representing a pair of friends and their friendship value, `result` is the sum of f * (k * (k + 1) // 2) for all friendships, modulo MOD.
    return result % MOD
    #The program returns the sum of f * (k * (k + 1) // 2) for all friendships, modulo MOD.
#Overall this is what the function does:The function calculates the sum of the product of each friendship value and the sum of the first `k` natural numbers, and returns this sum modulo `MOD`.

#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of lists where each sublist contains three integers a_i, b_i, and f_i representing a pair of friends and their friendship value. It is guaranteed that 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5, a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: `n`, `m`, `k`, and `friendships` will hold the values from the last iteration of the loop, and `t` will be 0 (since the loop will have finished executing). The results of `func_1` for each iteration will have been printed, but these results are not stored in any variable in the provided code snippet.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of children, the number of pairs of friends, the number of excursions, and a list of friendships with their respective values. For each test case, it computes and prints a result, likely related to organizing excursions among the children considering their friendships.

