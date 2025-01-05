#State of the program right berfore the function call: **
def func():
    N, a, ans = input(), map(lambda x: abs(int(x)), raw_input().split()), 0
    for i in xrange(0, N):
        x, y = 0, 0
        
        for j in xrange(0, N):
            if a[j] < a[i]:
                if j < i:
                    x += 1
                else:
                    y += 1
        
        ans += min(x, y)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `N` is a positive integer, `a` is a list containing absolute values of integers, `ans` is the total sum of the minimum value between `x` and `y` for all iterations, where `x` contains the total count of times a[j] is less than a[i] for all i and j where j < i, and `y` contains the total count of times a[j] is less than a[i] for all i and j where j >= i
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `N` as input, then reads a list of integers and calculates a value `ans` based on certain conditions involving `x` and `y`. It iterates over the list and counts the number of elements that are less than the current element both before and after the current index. It then adds the minimum count between `x` and `y` to the total `ans`. Finally, it prints the value of `ans`. The function does not accept any parameters and solely operates on the input provided during its execution.

