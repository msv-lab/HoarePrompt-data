#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the number of elements in the array. The second line contains n space-separated integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 1000) representing the elements of the array.
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
        
    #State of the program after the  for loop has been executed: Output State: `i` is `n`, `n` is the same as the initial value, `increasing` is either True or False, `constant` is either True or False, `decreasing` is either True or False.
    #
    #Explanation:
    #- The loop iterates from `i = 1` to `i = n-1`. Therefore, after the loop completes, `i` will be `n`.
    #- The variable `n` remains constant throughout the loop as it is not modified inside the loop.
    #- The variables `increasing`, `constant`, and `decreasing` can change based on the conditions inside the loop. However, their final state depends on the sequence of elements in the array `arr`.
    #
    #Conditions for the loop:
    #- The loop will execute `n-1` times if there are no interruptions.
    #- The loop can terminate early if `print('NO')` is executed due to the condition `if decreasing:`.
    #
    #Final Values:
    #- `i` will be `n` after the loop completes.
    #- `increasing` will be True if the array `arr` is strictly increasing up to the last element checked; otherwise, it will be False.
    #- `constant` will be True if any two consecutive elements are equal and `increasing` was previously True; otherwise, it will be False.
    #- `decreasing` will be True if any element is less than its previous element, but this would cause the program to print 'NO' and exit before completing the full loop. If the loop completes without printing 'NO', `decreasing` will be False.
    #
    #Since the loop does not modify `n`, the final value of `n` will be the same as the initial value.
    print('YES')
#Overall this is what the function does:The function reads an integer \( n \) followed by \( n \) space-separated integers from the input. It then checks if the sequence of numbers is either strictly increasing, strictly decreasing, or contains only equal consecutive elements. If the sequence meets any of these criteria, the function prints 'YES'; otherwise, it prints 'NO'. The function does not return any value. Potential edge cases include sequences where the first and last elements are equal, or where all elements are the same. The function also handles the case where the sequence is neither strictly increasing nor strictly decreasing but contains only equal consecutive elements.

