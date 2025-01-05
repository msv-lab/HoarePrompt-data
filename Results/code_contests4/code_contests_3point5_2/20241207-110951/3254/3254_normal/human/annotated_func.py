#State of the program right berfore the function call: n is a positive integer. The input sequence contains n integers where |pi| is less than or equal to 105.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `N` is the input value, `a` contains the absolute values of the input integers, `ans` is the total count of pairs (x, y) where x is the count of elements in `a` such that the value is less than the value at that index and the index is less than the current index i, and y is the count of elements in `a` such that the value is less than the value at that index and the index is greater than or equal to the current index i after all iterations of the loop have finished.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `N` followed by a sequence of integers. It then processes each integer in the sequence to count pairs (x, y) where x is the count of elements less than the value at that index and with an index less than the current index i, and y is the count of elements less than the value at that index and with an index greater than or equal to the current index i. The function calculates and prints the total count of such pairs `ans`. The function does not explicitly return a value.

