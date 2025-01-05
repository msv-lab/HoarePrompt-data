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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a sorted list of integers with at least 4 elements, `x` is the third element of list `a`, `i` is the index of the last element in list `a`, and `ans` is the number of elements equal to `x` in the list `a` starting from the third element.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `a`, sorts the list, finds the third element `x` of the sorted list, and then counts the number of elements equal to `x` in the list starting from the fourth element. It does not return any value but prints the count of elements equal to `x`.

