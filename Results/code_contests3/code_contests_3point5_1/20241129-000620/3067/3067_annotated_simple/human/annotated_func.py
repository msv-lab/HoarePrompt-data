#State of the program right berfore the function call: **
def func():
    N, Q = map(int, raw_input().split())
    S = raw_input()
    P = [0] * (N + 1)
    for i in range(N):
        if i == 0:
            P[0] = 0
            continue
        
        if S[i - 1:i + 1] == 'AC':
            P[i] = P[i - 1] + 1
        else:
            P[i] = P[i - 1]
        
    #State of the program after the  for loop has been executed: `N` and `Q` are integers, `S` is a string, `P` is a list of integers with length `N + 1`. After the loop executes, the values in `P` will be determined based on the conditions in the loop. If the substring `S[i - 1:i + 1]` equals 'AC', then `P[i] = P[i - 1] + 1`. Otherwise, `P[i]` will be assigned the value of `P[i - 1]`.
    for _ in range(Q):
        l, r = map(int, raw_input().split())
        
        print(P[r - 1] - P[l - 1])
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the values of N, Q, S, and P remain unchanged. The loop only processes the input values l and r and prints the difference between P[r - 1] and P[l - 1].
#Overall this is what the function does:The function `func` reads input values N, Q, S and calculates an array P based on the conditions specified in the for loop. It then processes Q queries by taking input l and r, and prints the difference between P[r - 1] and P[l - 1]. The function does not accept any parameters and does not specify any return value.

