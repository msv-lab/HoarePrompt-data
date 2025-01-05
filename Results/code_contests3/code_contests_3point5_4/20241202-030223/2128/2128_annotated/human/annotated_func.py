#State of the program right berfore the function call: **
def func():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        n, k = map(int, sys.stdin.readline().split(' '))
        
        arr = list(map(int, sys.stdin.readline().split()))
        
        arr = sorted(arr, reverse=True)
        
        ans = arr[0]
        
        if k >= n:
            k = n - 1
        
        for l in range(1, k + 1):
            ans += arr[l]
        
        print(ans)
        
    #State of the program after the  for loop has been executed: All variables will be unchanged after the loop finishes executing, as the loop does not modify the initial state of the variables.
#Overall this is what the function does:The function reads input from the standard input, processes the data based on the given constraints, and outputs the result. It does not accept any parameters and prints the calculated answer for each test case. The function sorts an array in reverse order, calculates the sum of specific elements in the array based on certain conditions, and prints the result.

