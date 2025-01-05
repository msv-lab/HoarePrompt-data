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
        
    #State of the program after the  for loop has been executed: Output State: `n` is an input integer, `a` is a sorted list of integers with at least 4 elements, `x` is the third element in the sorted list `a`, `ans` contains the number of consecutive occurrences of `x` starting from the third element in list `a`.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n`, then reads a list of integers and sorts them. It finds the third element in the sorted list and counts the consecutive occurrences of that element starting from the fourth position. The function then prints the count of consecutive occurrences. The function does not accept any parameters and does not return any value.

