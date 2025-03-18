#State of the program right berfore the function call: list is a list of integers representing the array a, and n is the length of the array such that 3 <= n <= 2 \* 10^5.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The function has iterated through all elements of the list `list`. The variable `i` is now equal to `n`, which is the length of the list. Since the loop did not return `False` during any iteration from `i = 0` to `i = n-1`, it means that every element in the list `list` was found to be 0. Therefore, the function did not return `False` and completed all its iterations without encountering any non-zero element.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a list of integers and an integer representing the length of the list. It checks if all elements in the list are zero. If any element is non-zero, it returns False immediately. If the function completes the iteration over the entire list without finding any non-zero elements, it returns True. The function can return either True or False based on the contents of the list.

#State of the program right berfore the function call: list is a list of integers representing the array a, and n is the length of the array such that 3 <= n <= 2 \* 10^5. Each element in the array is an integer in the range [0, 10^9].
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        
        if list[i - 1] != 0:
            print('no')
            return
        
    #State: Output State: All elements in the list are 0 or negative, with `list[i - 1]`, `list[i]`, and `list[i + 1]` all being 0. The loop terminates because none of the conditions inside the while loop are satisfied, as all relevant elements in the list have been reduced to 0 or below.
    #
    #This means that after all iterations of the loop have finished, every element in the list will be 0 or a negative number, but specifically, the elements at indices `i-1`, `i`, and `i+1` will all be exactly 0.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: All elements in the list are 0 or negative, with `list[i - 1]`, `list[i]`, and `list[i + 1]` all being 0. The loop terminates because none of the conditions inside the while loop are satisfied, as all relevant elements in the list have been reduced to 0 or below. Additionally, the function `func_1(list, n)` returns the same boolean value in both cases (True if the if part is executed, and False if the else part is executed).
#Overall this is what the function does:The function processes a list of integers by repeatedly modifying the values based on certain conditions until no further modifications can be made. Specifically, it checks each element (except the first and last) to see if it and its adjacent elements meet specific criteria. If so, it reduces the middle element and its neighbors accordingly. After processing, the function calls another function `func_1(list, n)` to determine whether to print 'YES' or 'NO'. The final state of the list is such that all elements are either 0 or negative, with the elements at indices `i-1`, `i`, and `i+1` all being exactly 0. The function does not return any value.

