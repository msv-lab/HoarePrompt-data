#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples, where each tuple contains three integers (a, b, f) representing the indices of the pair of children who are friends and their friendship value respectively. All pairs of friends are distinct, and the friendship value f is a positive integer. The constant MOD is defined as \(10^9 + 7\).
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: The final value of `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for all `i` from 0 to `m-1`, `n` is an integer representing the number of children, `m` is an integer representing the number of pairs of friends and must be equal to the total number of iterations of the loop, `k` is an integer representing the number of excursions, and `friendships` is a list of tuples where each tuple contains three integers (a, b, f) representing the indices of the pair of children who are friends and their friendship value respectively.
    return result % MOD
    #The program returns the result which is the sum of f * (k * (k + 1) // 2) % MOD for all i from 0 to m-1, where k is the number of excursions, f is the friendship value, and m is the total number of iterations of the loop as defined by the length of the friendships list. The result is then taken modulo MOD.
#Overall this is what the function does:The function accepts parameters n (the number of children), m (the number of pairs of friends), k (the number of excursions), and friendships (a list of tuples containing the indices of pairs of children who are friends and their friendship values). It calculates the sum of each friendship value multiplied by the combination of k excursions taken two at a time (k * (k + 1) // 2), modulo a constant MOD (\(10^9 + 7\)). The function returns this calculated sum.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of lists, where each inner list contains three integers a_i, b_i, and f_i representing the indices of the pair of children who are friends and their friendship value respectively.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: Output State: `t` must be equal to or greater than the total number of test cases, `n` is the number of children (input integer), `m` is the number of pairs of friends (input integer), `k` is the number of excursions (input integer), `friendships` is a list of lists where each inner list contains three integers `a_i`, `b_i`, and `f_i` representing the indices of the pair of children who are friends and their friendship value respectively (input list of lists), and `result` is the cumulative return value of `func_1(n, m, k, friendships)` for each test case.
    #
    #This means that after the loop has executed all its iterations, `t` will hold the final count of test cases processed, and `result` will be the combined outcome of applying `func_1` to each set of inputs provided across all test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes the number of children (n), the number of pairs of friends (m), the number of excursions (k), and a list of friendships. It then calls another function `func_1` with these parameters to compute a result. After processing all test cases, it prints the cumulative result of `func_1` for each test case. If any input is invalid, it returns an error message.

