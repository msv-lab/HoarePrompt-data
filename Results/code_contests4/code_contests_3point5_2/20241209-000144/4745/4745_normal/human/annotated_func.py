#State of the program right berfore the function call: N is a positive integer, and H_i (1 <= i <= N) are positive integers such that 1 <= H_i <= 10^9.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `N`, `H_i`, `n`, `arr`, `last`, `i`, `d` are positive integers. `arr` is a list of converted integers from input. `last` is the minimum value between `last` and the elements in `arr`. If at any point during the loop `d` becomes greater than 1, the program prints 'No' and exits. Otherwise, the program completes without any changes to the variables.
    print('Yes')
#Overall this is what the function does:The function `func` reads an integer `n` from input, followed by a list of integers `arr`. It then iterates through the list checking if each element is less than or equal to the previous one. If any element is greater than the previous one by more than 1, it prints 'No' and exits. If all elements satisfy the condition, it prints 'Yes'. The function does not accept any parameters. The code ensures that the input constraints are met, where `n` is a positive integer and the values in `arr` are positive integers between 1 and 10^9 inclusive.

