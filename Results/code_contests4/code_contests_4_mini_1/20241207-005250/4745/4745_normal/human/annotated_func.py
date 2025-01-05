#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 10^5, and H is a list of integers where each H[i] satisfies 1 <= H[i] <= 10^9.
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
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 10^5; `last` is the minimum value of `arr`; `i` is -1.
    print('Yes')
#Overall this is what the function does:The function accepts a positive integer `N` and a list of integers `H`. It checks if the array `H` satisfies a specific condition: for every element in the array, it ensures that there are no elements that are more than 1 greater than the minimum value encountered so far when traversing the array from the last element to the first. If any such condition is violated, it prints 'No' and exits; otherwise, it prints 'Yes'.

