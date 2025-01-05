#State of the program right berfore the function call: a, b, c, and d are integers such that 0 ≤ a, b, c, d ≤ 1000, and the sequence of operations consists of three signs ('+' or '*') separated by spaces.
def func():
    res = 100000000000000000000000000
    a = raw_input().split()
    z = raw_input().split()
    for c in itertools.permutations(a):
        res = min(res, eval('((' + c[0] + z[0] + c[1] + ')' + z[1] + c[2] + ')' + z
            [2] + c[3]))
        
        res = min(res, eval('(' + c[0] + z[0] + c[1] + ')' + z[2] + '(' + c[2] + z[
            1] + c[3] + ')'))
        
    #State of the program after the  for loop has been executed: `a` is a non-empty list of strings, `b` is unchanged, `c` is the last permutation of `a`, `d` is unchanged, `res` is updated to the minimum of its previous value and the evaluated expression result from all permutations of `a` and `z`.
    print(res)
#Overall this is what the function does:The function accepts a sequence of four integers entered via standard input and a sequence of three arithmetic operators ('+' or '*') also entered via standard input. It evaluates all permutations of the integers and all possible parenthesizations of the operations to find the minimum result of the expressions. The final result is printed, but the function does not return any value. Note that the integers are not passed as parameters to the function; instead, they are read from input, which could lead to issues if the input format is not strictly followed.

