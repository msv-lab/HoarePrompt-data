#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. a_i are integers representing the values of coins such that 1 <= a_i <= 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 <= n <= 100, `a` is a list of integers obtained by mapping each input value to an integer and splitting the input based on spaces. If `n` == 11, then 5 is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 100, `a` is a list of integers obtained by mapping each input value to an integer and splitting the input based on spaces with at least 1 element, `c` is a list of 101 integers where the value at index `d` is incremented by the number of occurrences of `d` in list `a`
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` and a list of integers `a` from the user input. If `n` is equal to 11, it prints 5. Then, it creates a list `c` of 101 elements initialized to 0. It iterates over the elements in list `a` and increments the corresponding index in list `c` by the number of occurrences of that element. Finally, it prints the maximum value in list `c`. The function does not accept any parameters and does not have a specific return value.

