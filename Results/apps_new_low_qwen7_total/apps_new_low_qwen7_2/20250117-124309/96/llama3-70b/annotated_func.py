#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 1000) representing the elements of the array.
def func():
    n = int(input())

arr = list(map(int, input().split()))

increasing = False

constant = False

decreasing = False
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            if decreasing:
                print('NO')
                exit()
            increasing = True
        elif arr[i] == arr[i - 1]:
            if increasing:
                increasing = False
                constant = True
        else:
            if increasing:
                increasing = False
            decreasing = True
        
    #State of the program after the  for loop has been executed: `i` is `n-1`, `n` is greater than 1, `increasing` is a boolean value indicating whether there was an increasing sequence detected, `decreasing` is a boolean value indicating whether there was a decreasing sequence detected, `constant` is True if there were no changes between consecutive elements.
    print('YES')
#Overall this is what the function does:The function reads an integer \( n \) and an array of \( n \) integers from the user input. It then checks whether the array is either strictly increasing, strictly decreasing, or constant. If the array contains any element that breaks these sequences, it prints 'NO' and exits immediately. Otherwise, it prints 'YES'. The function does not return any value.

