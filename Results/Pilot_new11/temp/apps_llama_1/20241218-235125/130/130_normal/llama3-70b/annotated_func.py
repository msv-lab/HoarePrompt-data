#State of the program right berfore the function call: N, M, K, and L are integers such that 1 <= K <= N and 1 <= M, L, and 1 <= L <= N - K.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: N, M, K, and L are input integers, where if M is greater than or equal to N - K + 1 and M is greater than or equal to L, then 1 has been printed. Otherwise, if M is less than N - K + 1 or M is less than L, then -1 has been returned and printed.
#Overall this is what the function does:The function takes four integers as input (N, M, K, L) and checks two conditions: if M is greater than or equal to N - K + 1 and if M is greater than or equal to L. If both conditions are met, it prints 1, indicating a valid state; otherwise, it prints -1, indicating an invalid state. After execution, the program will have printed either 1 or -1, depending on the conditions, and the input integers will remain unchanged. The function does not handle cases where the input integers do not meet the initial constraints (1 <= K <= N and 1 <= M, L, and 1 <= L <= N - K), as it does not include any error checking or handling for invalid inputs.

