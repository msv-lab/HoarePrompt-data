#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and each tree is represented by a pair of integers (xi, hi) where 1 ≤ xi, hi ≤ 10^9, and the coordinates xi are given in strictly ascending order with no duplicates.
def func():
    n = input()
    p = []
    h = []
    for i in range(n):
        e = map(int, raw_input().split())
        
        p.append(e[0])
        
        h.append(e[1])
        
    #State of the program after the  for loop has been executed: `n` is an input string that must be convertible to an integer and at least 1; `p` contains the first integer from each of the `n` input strings; `h` contains the second integer from each of the `n` input strings; `i` is `n - 1`, `e` is a map object of integers created from the last split input string.
    pivout = p[0]
    if (n == 1) :
        cont = 1
    else :
        cont = 2
    #State of the program after the if-else block has been executed: *`n` is an input string that must be convertible to an integer and at least 1. If `n` is equal to 1, `p` contains the first integer from each of the `n` input strings, `h` contains the second integer from each of the `n` input strings, `i` is 0 (`n - 1`), `e` is a map object of integers created from the last split input string, `pivout` is assigned the value of `p[0]`, and `cont` is set to 1. Otherwise, `cont` is set to 2 while maintaining that `p`, `h`, `i`, `e`, and `pivout` retain their respective values based on `n`.
    for i in range(1, len(p) - 1):
        if p[i] - h[i] > pivout:
            cont += 1
            pivout = p[i]
        elif p[i] + h[i] < p[i + 1]:
            cont += 1
            pivout = p[i] + h[i]
        else:
            pivout = p[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer at least 1, `cont` is the final count based on conditions in the loop, `p` is a list of integers with at least 2 elements, `h` is a list of integers with at least 2 elements, `i` is `len(p) - 1`, `pivout` is the last computed value based on the loop conditions.
    print(cont)
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` and `n` pairs of integers representing the coordinates of trees. It determines how many trees can be placed without overlapping based on their positions and heights, and it prints this count. If `n` is 1, it returns 1; otherwise, it checks the distances between trees to count how many can fit without overlapping, printing that count. The function does not handle invalid input cases or ensure that `n` is convertible to an integer.

