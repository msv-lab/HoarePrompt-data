#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100, and a list of N integers W where 1 <= W_i <= 100 for all i.
def func():
    N = input()
    V = list(map(int, input().split()))
    M = 1000000000.0
    for i in range(1, len(V)):
        diff = abs(sum(V[:i]) - sum(V[i:]))
        
        if M > diff:
            M = diff
        
    #State of the program after the  for loop has been executed: `N` is an integer equal to the input value, `V` is a list of integers equal to the input values split and converted to integers, `M` is the minimum absolute difference between the sum of any prefix and the sum of its corresponding suffix in the list `V`.
    print(M)
#Overall this is what the function does:The function `func` accepts a list of integers `V` where the length of the list `N` satisfies 2 <= N <= 100, and each integer `V_i` in the list satisfies 1 <= V_i <= 100. After executing the code, the function calculates and returns the minimum absolute difference between the sum of any prefix and the sum of its corresponding suffix in the list `V`. There are no explicit return cases mentioned in the annotations, but the function prints the result `M` which is the minimum absolute difference. The function does not return any value; it only prints the result.

