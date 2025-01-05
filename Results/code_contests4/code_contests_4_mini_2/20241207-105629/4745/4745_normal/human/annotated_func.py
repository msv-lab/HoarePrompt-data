#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 10^5, and H is a list of N integers where each integer H_i satisfies 1 <= H_i <= 10^9.
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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 10^5, `H` is a list of `N` integers, `n` is at least 1, `last` is the minimum value in `arr`, and `arr` remains unchanged.
    print('Yes')
#Overall this is what the function does:The function accepts a positive integer `N` and a list of `N` integers. It checks if the integers can be arranged in a non-increasing order such that no two consecutive elements differ by more than 1. If any element is greater than the previous one by more than 1, it outputs 'No' and exits; otherwise, it outputs 'Yes' after checking all elements.

