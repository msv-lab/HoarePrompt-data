#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 100000, and H is a list of N integers where each H_i is such that 1 <= H_i <= 10^9.
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
        
    #State of the program after the  for loop has been executed: `last` is the minimum value from the list `arr`, `N` is a positive integer such that 1 <= `N` <= 100000, `H` is a list of `N` integers where each `H_i` is such that 1 <= `H_i` <= 10^9, `n` is the value of `int(stdin.readline())`, and `i` is -1 (indicating the loop has finished executing).
    print('Yes')
#Overall this is what the function does:The function reads an integer `N` and a list of `N` integers from input. It checks if there are any elements in the list that are greater than the last element (from the end of the list) by more than 1. If such an element exists, it prints 'No' and terminates. If all elements are within the allowed difference of 1 from the last element, it prints 'Yes'. It does not take any parameters directly.

