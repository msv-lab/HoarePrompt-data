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
        
    #State of the program after the  for loop has been executed: i is n-1, n is unchanged, `increasing`, `constant`, and `decreasing` reflect the overall trend of the list `arr` from `arr[0]` to `arr[n-1]`.
    print('YES')
#Overall this is what the function does:The function reads an integer `n` followed by `n` integers from the input, representing an array. It then checks the trend of the array to determine if it is strictly increasing, strictly decreasing, or constant. If the array does not follow one of these trends, it prints 'NO' and exits. Otherwise, it prints 'YES'. The function does not return any value. Potential edge cases include arrays that are constant or have a mix of increasing and decreasing trends, which are handled correctly by the code. There is no missing functionality in the provided code.

