#State of the program right berfore the function call: N and M are positive integers such that 1 <= N, M <= 20. A_{ij}, B_i, and C are integers such that -100 <= A_{ij}, B_i, C <= 100.**
def func():
    N, M, C = map(int, raw_input().split())
    B = map(int, raw_input().split())
    ans = 0
    for i in range(0, N):
        A = map(int, raw_input().split())
        
        tmp = [(A[m] * B[m]) for m in range(M)]
        
        if sum(tmp) + C > 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: N is an integer greater than or equal to 0, M is initialized, C is initialized, B is assigned a map object with integer values, ans is the number of times the sum of the products of A and B plus C is greater than 0 after all iterations of the loop have finished.
    print(ans)
#Overall this is what the function does:The function `func` reads input values for N, M, and C, as well as arrays B and A. It calculates the sum of products of elements in arrays A and B, adds C to the sum, and increments a counter if the result is greater than 0. Finally, it prints the total count of such occurrences. The function does not accept any parameters and operates without input arguments.

