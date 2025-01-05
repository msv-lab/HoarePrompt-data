#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a = sorted(a)
    x = a[2]
    ans = 1
    for i in xrange(3, len(a)):
        if a[i] == x:
            ans += 1
        else:
            break
        
    #State of the program after the  for loop has been executed: Output State: `n` is an input integer, `a` is sorted in ascending order with length greater than or equal to 3, `x` is the third element of list `a`, `ans` is the number of consecutive occurrences of `x` from the third element onward in list `a`.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` as input, followed by a list of integers `a`, sorts `a` in ascending order, finds the third element `x` in the sorted list, and then calculates the number of consecutive occurrences of `x` from the third element onwards in the list `a`. The function then prints the count of consecutive occurrences. The function does not accept any parameters explicitly, and it does not return any value.

