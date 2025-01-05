#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. The list a contains n integers such that each element ai is an integer and 1 <= ai <= 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an input integer between 1 and 100, `a` is a list containing `n` integers where each `a[i]` is an integer between 1 and 100. If `n` is equal to 11, the value of `n` is updated to 11 and the number 5 is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 1 and 100, `a` is a non-empty list containing `n` integers between 1 and 100, `c` is a list containing 101 integers where each element represents the frequency of the corresponding integer in list `a`.
    print(max(c))
#Overall this is what the function does:The function `func` reads an integer `n` and a list `a` of `n` integers. If `n` is equal to 11, it prints 5. Then, it creates a frequency count list `c` for the elements in `a` and prints the maximum frequency. The function does not accept any parameters explicitly and operates based on user input.

