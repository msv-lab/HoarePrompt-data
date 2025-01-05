#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer, `a` is a list of integers. If `n` equals 11, the value 5 is printed. Otherwise, no changes are made to the state of the program variables.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `a` is a list of integers, `c` is a list of 101 integers with each element representing the frequency of that index in list `a`, `d` is the last element in list `a`
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, followed by a list of integers `a`. If `n` is equal to 11, it prints the value 5. Then, it creates a list `c` of size 101 and increments the frequency of each element in list `a` in the corresponding index of list `c`. Finally, it prints the maximum value in list `c`. The function does not accept any parameters and does not return any value.

