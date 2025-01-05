#State of the program right berfore the function call: N is a positive integer representing the number of code pieces (1 ≤ N ≤ 20), M is a positive integer representing the number of characteristics per code (1 ≤ M ≤ 20), C is an integer (-100 ≤ C ≤ 100), B is a list of M integers where each B_i is in the range of -100 to 100, and A is a 2D list of integers where each A_{ij} is in the range of -100 to 100.
def func():
    N, M, C = map(int, raw_input().split())
    B = map(int, raw_input().split())
    ans = 0
    for i in range(0, N):
        A = map(int, raw_input().split())
        
        tmp = [(A[m] * B[m]) for m in range(M)]
        
        if sum(tmp) + C > 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `M` is a positive integer, `C` is an integer, `B` is a list of `M` integers, `A` is a list of integers obtained from user input for each iteration, `ans` is the count of iterations where the sum of the products of corresponding elements from `A` and `B`, plus `C`, is greater than 0.
    print(ans)
#Overall this is what the function does:The function accepts user input for a positive integer `N` (the number of code pieces), a positive integer `M` (the number of characteristics per code), an integer `C`, a list `B` of `M` integers, and a 2D list `A` of integers. It counts how many times the sum of the products of corresponding elements from `A` and `B`, plus `C`, is greater than 0. The result is printed as the output, which represents the count of such cases.

