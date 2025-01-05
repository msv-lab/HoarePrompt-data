#State of the program right berfore the function call: **
def func():
    N, M, C = map(int, raw_input().split())
    B = map(int, raw_input().split())
    ans = 0
    for i in range(0, N):
        A = map(int, raw_input().split())
        
        tmp = [(A[m] * B[m]) for m in range(M)]
        
        if sum(tmp) + C > 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `N`, `M`, `C`, `B`, `i`, `A`, `tmp`, and `ans` are integers or map objects as described in the precondition. The loop will execute `N` times. At each iteration, `A` is assigned the result of mapping `int` to the inputs obtained from `raw_input().split()`. `tmp` is a list comprehension of products of elements from `A` and `B`. If the sum of `tmp` plus `C` is greater than 0, `ans` is incremented by 1.
    print(ans)
#Overall this is what the function does:The function reads input values for N, M, C, and arrays B and A. It then iterates N times, calculating products of elements from A and B, checking if the sum of these products plus C is greater than 0, and increments the answer accordingly. Finally, it prints the total count of iterations where the sum condition is met. The function does not accept any parameters and does not return any value.

