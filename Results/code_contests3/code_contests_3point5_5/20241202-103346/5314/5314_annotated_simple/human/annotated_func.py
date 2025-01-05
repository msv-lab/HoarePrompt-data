#State of the program right berfore the function call: **
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: 'n' and 't' are assigned integer values based on the input provided, 'a' is the input after splitting, 'i' is equal to the number of elements in 'a', 't' is decremented by the sum of (86400 - int(a[i])) for all 'i' from 0 to the number of elements in 'a'
    print(i)
#Overall this is what the function does:The function reads two integers 'n' and 't' from the input, followed by a list of integers 'a'. It then iterates through the elements of 'a', decrementing 't' by the difference between 86400 and the current element of 'a'. The function prints the final value of 'i' after the loop, which represents the number of elements processed in 'a'. The function does not accept any parameters and does not return any value.

