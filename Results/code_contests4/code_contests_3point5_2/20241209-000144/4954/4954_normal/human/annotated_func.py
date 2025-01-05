#State of the program right berfore the function call: N and M are integers such that 1 <= N, M <= 20. A_{ij}, B_i, and C are integers such that -100 <= A_{ij}, B_i, C <= 100.**
def func():
    N, M, C = map(int, raw_input().split())
    B = map(int, raw_input().split())
    ans = 0
    for i in range(0, N):
        A = map(int, raw_input().split())
        
        tmp = [(A[m] * B[m]) for m in range(M)]
        
        if sum(tmp) + C > 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: N, M, C, ans are integers satisfying the given conditions. The loop iterates over N times, each time calculating tmp as the result of element-wise multiplication of A and B for each index m in the range of M. If the sum of tmp and C is greater than 0, ans is incremented by 1.
    print(ans)
#Overall this is what the function does:The function `func` reads input values N, M, and C along with arrays B and A. It then calculates the element-wise multiplication of arrays A and B for each row of A, checks if the sum of the products plus C is greater than 0, and increments the answer accordingly. The final count of rows meeting the condition is printed as the output. The function does not explicitly return a value. It operates under the constraints where N and M are integers between 1 and 20, and A_{ij}, B_i, and C are integers between -100 and 100.

