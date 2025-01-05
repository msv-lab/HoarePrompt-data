#State of the program right berfore the function call: N is a positive integer and H_i (1 <= i <= N) are positive integers between 1 and 10^9 inclusive.**
def func():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    last = arr[n - 1]
    for i in range(n - 1, -1, -1):
        if arr[i] > last:
            d = arr[i] - last
            if d > 1:
                print('No')
                exit(0)
        
        last = min(last, arr[i])
        
    #State of the program after the  for loop has been executed: N, H_i, n, arr, last, i, d are positive integers. 'No' is printed and the program exits with code 0 if arr[i] is greater than last and the difference between arr[i] and last is greater than 1 at any point during the loop execution. Otherwise, the loop executes successfully without printing 'No' and exits normally.
    print('Yes')
#Overall this is what the function does:The function `func` reads in an integer `n` followed by a list of integers `arr`. It then iterates through the list checking if each element is not greater than the previous element and the difference is not greater than 1. If these conditions are met for all elements, it prints 'Yes'. If any element violates the conditions, it prints 'No' and exits the program. The function does not explicitly return any value.

