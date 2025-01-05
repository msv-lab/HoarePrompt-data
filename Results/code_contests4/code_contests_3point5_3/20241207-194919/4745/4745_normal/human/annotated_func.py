#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 1, `arr` is a list of integers based on the input values, `last` is the minimum value in the list `arr`, `i` is equal to -1, `d` represents the difference between the last element in `arr` and the minimum value in the list. If any element in `arr` is greater than `last`, the program prints 'No'.
    print('Yes')
#Overall this is what the function does:The function `func` reads an integer `n` followed by a list of integers. It then iterates through the list checking if any element is greater than the previous minimum element. If such an element is found and the difference between them is greater than 1, it prints 'No' and exits. If no such element is found, it prints 'Yes'. The function does not accept any parameters and does not return any value.

