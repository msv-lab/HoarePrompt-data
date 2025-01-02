#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100, and W is a list of N integers such that 1 <= W_i <= 100 for all i in range(N).
def func():
    N = input()
    V = list(map(int, input().split()))
    M = 1000000000.0
    for i in range(1, len(V)):
        diff = abs(sum(V[:i]) - sum(V[i:]))
        
        if M > diff:
            M = diff
        
    #State of the program after the  for loop has been executed: `N` must be at least 2, `V` contains at least 2 elements, `M` is the minimum absolute difference between the sum of any prefix and suffix of `V`.
    print(M)
#Overall this is what the function does:The function accepts no parameters directly but reads two inputs: an integer \( N \) and a list of \( N \) integers \( V \). It calculates the minimum absolute difference between the sum of any prefix and suffix of the list \( V \), and prints this minimum difference. The function does not return any value. The state of the program after the function concludes is that the variable \( M \) holds the minimum absolute difference found during the iteration over the list \( V \), and it is printed to the console. The function assumes that the input values are within the specified ranges, and it handles the case where \( N \geq 2 \) and \( V \) has at least 2 elements. If \( N < 2 \), the function would not execute the loop and would not print anything, which is an edge case that the current code does not handle explicitly.

