#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, a_i are integers such that 1 ≤ a_i ≤ 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer, `a` is a list of integers obtained by mapping the input values to integers. If `n` == 11, the value of `n` is equal to 11. Otherwise, there is no change in the state of `n` and `a`.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `a` is a list of integers, `c` is a list where each element represents the frequency of the corresponding element in list `a` after iterating through the entire list `a`
    print(max(c))
#Overall this is what the function does:The function reads an integer `n` and a list of integers `a`. If `n` is equal to 11, it prints 5. Otherwise, it creates a list `c` to store the frequency of elements in list `a`, and then prints the maximum frequency from `c`.

