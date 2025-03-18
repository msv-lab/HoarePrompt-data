#State of the program right berfore the function call: N, M, K, and L are integers, where N is the total number of different collectible coins, M is the number of friends, K is the number of coins Ivan already has, and L is the minimum number of new coins Ivan must receive, such that 1 <= K <= N <= 10^18, 1 <= M, L <= 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N` is an integer, the total number of different collectible coins, `M` is an integer, the number of friends, `K` is an integer, the number of coins Ivan already has, `L` is an integer, the minimum number of new coins Ivan must receive, `min_x` is an integer equal to `(L + M - 1) // M`. If `M * min_x` is less than or equal to the difference between `N` and `K`, then the value of `min_x` has been printed. Otherwise, the product of `M` and `min_x` is greater than `N - K`, and the value -1 has been returned.
#Overall this is what the function does:The function determines the minimum number of rounds Ivan needs to receive a specified number of new coins from his friends. It takes four parameters: the total number of different collectible coins (N), the number of friends (M), the number of coins Ivan already has (K), and the minimum number of new coins Ivan must receive (L). The function returns the minimum number of rounds (min_x) if Ivan can receive at least L new coins without exceeding the total number of available coins (N - K), considering that each friend can give one coin per round. If the minimum number of rounds required to receive L new coins would exceed the available coins, the function returns -1, indicating that it is impossible to fulfill Ivan's requirement. The function does not modify the input parameters and only provides a calculated output based on the given conditions.

