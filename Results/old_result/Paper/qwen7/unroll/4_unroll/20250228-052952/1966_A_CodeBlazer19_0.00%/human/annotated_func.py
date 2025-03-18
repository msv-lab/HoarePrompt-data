#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the list of integers c represents the numbers written on the cards, where 1 ≤ c_i ≤ 100 for each card i.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: Output State: t is an integer between 1 and 500 inclusive. For each iteration of the loop, the value of k is subtracted by 1 and printed. The final state of t remains unchanged, but the printed values are the result of k-1 for each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( k \), followed by a list of \( n \) integers \( c \). It then prints the value \( k - 1 \) for each test case. The final state of the variable \( t \) remains unchanged, but the function outputs \( k - 1 \) for each test case.

