#State of the program right berfore the function call: a, b, c, and d are integers such that 0 ≤ a, b, c, d ≤ 1000, and the sequence of operations consists of three characters, each either '+' or '*'.
def func():
    res = 100000000000000000000000000
    a = raw_input().split()
    z = raw_input().split()
    for c in itertools.permutations(a):
        res = min(res, eval('((' + c[0] + z[0] + c[1] + ')' + z[1] + c[2] + ')' + z
            [2] + c[3]))
        
        res = min(res, eval('(' + c[0] + z[0] + c[1] + ')' + z[2] + '(' + c[2] + z[
            1] + c[3] + ')'))
        
    #State of the program after the  for loop has been executed: `res` is the minimum result of all evaluated expressions using permutations of `a` and elements of `z`; `c` is a list containing all possible permutations of `a`, `z` is a list with at least 3 elements.
    print(res)
#Overall this is what the function does:The function accepts four integers a, b, c, and d as input (through user input) and computes the minimum result of all possible evaluations of the expressions formed by these integers, combined with three operations, either '+' or '*', based on all permutations of the integers. The result is printed, but the function does not return any value. The function assumes valid inputs but does not handle cases where the input may not be in the expected format, which could lead to runtime errors.

