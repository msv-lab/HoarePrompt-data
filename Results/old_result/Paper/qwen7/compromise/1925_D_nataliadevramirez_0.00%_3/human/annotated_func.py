#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples, where each tuple contains three integers (a, b, f) representing the indices of the pair of children who are friends and their friendship value respectively. The friendship values are non-negative integers, and all pairs of friends are distinct. The constants MOD and friendships are defined elsewhere in the program.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: Output State: `result` is the sum of the friendship values multiplied by the combination of `k` taken 2, modulo `MOD`, for all `m` pairs of friends.
    return result % MOD
    #The program returns the sum of the friendship values multiplied by the combination of k taken 2, modulo MOD, for all m pairs of friends.
#Overall this is what the function does:The function accepts four parameters: the number of children (n), the number of pairs of friends (m), the number of excursions (k), and a list of tuples representing pairs of friends and their friendship values (friendships). It calculates the sum of the friendship values, each multiplied by the combination of k taken 2, and returns this sum modulo a constant MOD.

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of lists, where each inner list contains three integers a_i, b_i, and f_i representing the indices of the pair of children who are friends and their friendship value respectively.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: After executing the loop `t` times, the output state will consist of `t` results returned by the function `func_1`. Each result is the outcome of processing the inputs `n`, `m`, `k`, and the list of `friendships` for each iteration. The exact values of these results depend on the implementation of `func_1` and the specific inputs provided in each iteration.
#Overall this is what the function does:The function processes `t` test cases, each involving `n` children, `m` pairs of friends, and `k` excursions. For each test case, it reads the number of children, pairs of friends, and excursions, along with the friendship values. It then calls another function `func_1` to compute some result based on these inputs. Finally, it prints the result for each test case.

