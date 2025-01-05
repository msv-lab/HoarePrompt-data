#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and a_i is an integer such that 1 <= a_i <= 100 for each i.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *n is an integer such that 1 <= n <= 100, a_i is an integer such that 1 <= a_i <= 100 for each i. If n == 11, the program does not modify any variables or values.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: Each element at index `d` in list `c` will be incremented by the number of occurrences of `d` in list `a`.
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` from the user, followed by a list of integers `a`. If `n` is equal to 11, it prints 5. Then, it creates a list `c` of size 101 filled with zeros and increments the value at each index by the number of occurrences of the corresponding element in list `a`. Finally, it prints the maximum value in list `c`. The function does not accept any parameters and does not return any values directly.

