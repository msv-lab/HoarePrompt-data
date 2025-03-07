#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing a pair of friends and their initial friendship value. It is assumed that 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2*10^5, and for each tuple (a, b, f) in friendships, 1 <= a, b <= n, a != b, and 1 <= f <= 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: result is the accumulated sum of (f * (k * (k + 1) // 2)) % MOD for all m friendships.
    return result % MOD
    #The program returns the value of `result % MOD`.
#Overall this is what the function does:The function calculates and returns the accumulated sum of a specific formula applied to each friendship, modulo `MOD`. The formula for each friendship is the product of the friendship's initial value and the sum of the first `k` natural numbers, all taken modulo `MOD`.

#State of the program right berfore the function call: n is an integer representing the number of children such that 2 <= n <= 10^5, m is an integer representing the number of pairs of friends such that 0 <= m <= min(10^5, n*(n-1)/2), k is an integer representing the number of excursions such that 1 <= k <= 2*10^5, and friendships is a list of lists where each sublist contains three integers a_i, b_i, f_i representing a pair of friends and their initial friendship value such that a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: `t` is 0, `n`, `m`, `k`, and `friendships` are the values from the last iteration, and `result` is the return value of `func_1(n, m, k, friendships)` from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of the number of children, the number of pairs of friends, the number of excursions, and the initial friendship values between pairs of friends. For each test case, it computes and prints the final friendship values after considering all excursions.

