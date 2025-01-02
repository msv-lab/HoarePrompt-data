#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and x1, x2, ..., xn are positive integers where 1 ≤ xi ≤ 100.
def func():
    n = int(raw_input())
    x = raw_input().split(' ')
    for i in xrange(len(x)):
        x[i] = int(x[i])
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 2 ≤ n ≤ 100, `x` is a list where all elements are integers representing the positive integers `x1, x2, ..., xn` where 1 ≤ xi ≤ 100, `len(x) = n`, `i` is `n - 1`.
    x.sort()
    solved = False
    while True:
        x.sort()
        
        for j in xrange(n - 1):
            if x[j + 1] > x[j]:
                x[j + 1] = x[j + 1] - x[j]
        
        solved = True
        
        for j in xrange(n - 1):
            if x[j + 1] != x[j]:
                solved = False
                break
        
        if solved:
            break
        
    #State of the program after the loop has been executed: `n` is an integer such that \(2 \leq n \leq 100\), `x` is a sorted list of integers with all elements being equal, `i` is `n - 1`, `solved` is `True`, and `j` is `n - 2` if the loop completed without breaking early. If the loop broke early due to finding unequal elements, `j` is the index of the last element checked.
    print(x[0] * n)
#Overall this is what the function does:The function does not handle invalid input (e.g., non-integer values, out-of-range values) gracefully. It assumes the input is always valid according to the specified constraints.

### Final State:
-

