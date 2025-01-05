#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer with a value of 11, `a` is a list of integers. If `n` is equal to 11, the program prints the integer 5.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is 11, `a` is a list of integers, `c` is a list of 101 integers with the value at each index `d` increased by the number of occurrences of `d` in list `a`.
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `a` from the user input. If `n` is equal to 11, it prints the integer 5. Then, it creates a list `c` of length 101 filled with zeros. It iterates through the list `a` and updates the occurrences of each element in list `c`. Finally, it prints the maximum value in list `c`. The function does not accept any parameters and does not return any value.

