#State of the program right berfore the function call: N is a positive integer (1 <= N <= 20), M is a positive integer (1 <= M <= 20), C is an integer (-100 <= C <= 100), and B is a list of M integers where each B_i is in the range (-100 <= B_i <= 100). A is a 2D list of integers with N rows and M columns, where each A_{ij} is in the range (-100 <= A_{ij} <= 100).
def func():
    N, M, C = map(int, raw_input().split())
    B = map(int, raw_input().split())
    ans = 0
    for i in range(0, N):
        A = map(int, raw_input().split())
        
        tmp = [(A[m] * B[m]) for m in range(M)]
        
        if sum(tmp) + C > 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer (1 <= N <= 20), `M` is a positive integer (1 <= M <= 20), `C` is an integer (-100 <= C <= 100), `B` is a list of `M` integers where each `B_i` is in the range (-100 <= B_i <= 100), `ans` is the count of instances where the sum of `tmp` plus `C` is greater than 0 after all iterations, `i` is equal to `N`, and `tmp` is a list of products of corresponding elements from the last input of `A` and `B` for indices in the range of `M`.
    print(ans)
#Overall this is what the function does:The function accepts three integers N and M (both between 1 and 20), an integer C (between -100 and 100), and a list B of M integers (each between -100 and 100). It then processes N rows of M integers from a 2D list A. For each row in A, it computes the dot product of that row with B, adds C to the result, and increments a counter if the sum is greater than 0. Finally, it prints the count of such instances where the sum exceeds 0. The function does not explicitly validate input constraints and assumes the inputs are correctly formatted.

