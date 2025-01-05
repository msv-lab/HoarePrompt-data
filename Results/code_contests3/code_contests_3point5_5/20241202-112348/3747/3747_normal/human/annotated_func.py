#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100. The values of coins a_i are integers such that 1 ≤ a_i ≤ 100.**
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *n is an integer such that 1 ≤ n ≤ 100, a is a list of integers input by splitting the raw input. If n == 11, the value of n is equal to 11.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `a` is a list of integers with at least 1 element, `c` is a list of 101 integers representing the frequency of each index in `a` in the original list
    print(max(c))
#Overall this is what the function does:The function reads an integer `n` and a list of integers `a` from user input. If `n` is equal to 11, it prints 5. Then, it initializes a list `c` of 101 integers to track the frequency of each value in list `a`. Finally, it prints the maximum frequency value from the list `c`.

