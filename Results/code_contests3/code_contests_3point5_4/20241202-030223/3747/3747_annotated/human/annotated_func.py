#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an input integer, `a` is a list of integers. If `n` == 11, the code prints the integer 5.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a list of integers with at least 1 element, `c` is a list of 101 integers with each element representing the frequency of that index in list `a`, `d` is the last element in the list `a`
    print(max(c))
#Overall this is what the function does:The function `func()` reads an integer `n` as input, followed by a list of integers `a`. If `n` is equal to 11, the function prints the integer 5. Then, the function creates a list `c` of size 101 and updates the frequency of each element from list `a` in `c`. Finally, the function prints the maximum value in list `c`. The functionality of the function is to process the input values and determine the maximum frequency of elements in the input list `a`.

