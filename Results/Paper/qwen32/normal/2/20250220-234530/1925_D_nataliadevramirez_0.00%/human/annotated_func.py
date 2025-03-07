#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing a pair of friends and their initial friendship value.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: `n` is an integer representing the number of children, `m` is an integer representing the number of pairs of friends, `k` is an integer representing the number of excursions, `friendships` is a list of tuples where each tuple contains three integers (a, b, f) representing a pair of friends and their initial friendship value, `result` is the accumulated sum of `f * (k * (k + 1) // 2) % MOD` for all `i` from `0` to `m-1`.
    return result % MOD
    #The program returns the value of `result % MOD`.
#Overall this is what the function does:The function calculates and returns the total accumulated sum of the product of each friendship's initial value and a specific formula `(k * (k + 1) // 2)`, modulo `MOD`, for all pairs of friends.

#State of the program right berfore the function call: n is an integer representing the number of children such that 2 <= n <= 10^5, m is an integer representing the number of pairs of friends such that 0 <= m <= min(10^5, n*(n-1)/2), k is an integer representing the number of excursions such that 1 <= k <= 2*10^5, and friendships is a list of lists where each sublist contains three integers a_i, b_i, f_i representing a pair of friends and their friendship value such that a_i != b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9. All pairs of friends are distinct.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: `n` is the first integer read from the input in the last iteration, `m` is the second integer read from the input in the last iteration, `k` is the third integer read from the input in the last iteration, `friendships` is a list of `m` sublists where each sublist contains three integers read from the input in the last iteration, `t` is the total number of iterations (unchanged), and `result` is the return value of `func_1(n, m, k, friendships)` for the last iteration.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case consists of the number of children, the number of pairs of friends, the number of excursions, and the details of each friendship including the friendship value. For each test case, it computes and prints a result based on these inputs.

