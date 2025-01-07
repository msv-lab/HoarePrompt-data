#State of the program right berfore the function call: N, M, K, and L are integers, such that 1 <= K <= N, 1 <= M, and 1 <= L, and N, M, K, L are within the range [1, 10^18].
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: N is an integer, M is an integer where 1 <= M, K is an integer, L is an integer where 1 <= L, and `min_x` is (L + M - 1) // M. If M * `min_x` <= N - K, then the value of `min_x` has been printed. Otherwise, the value -1 has been returned as output.
#Overall this is what the function does:The function reads four integers N, M, K, and L from the standard input and prints the smallest integer `min_x` such that `M * min_x` is greater than `L` and `M * min_x` is less than or equal to `N - K`, or prints -1 if no such integer exists

