#State of the program right berfore the function call: a, b, c, d are integers such that 0 <= a, b, c, d <= 1000. The sequence of operations consists of three characters either '+' or '*'.**
def func():
    res = 100000000000000000000000000
    a = raw_input().split()
    z = raw_input().split()
    for c in itertools.permutations(a):
        res = min(res, eval('((' + c[0] + z[0] + c[1] + ')' + z[1] + c[2] + ')' + z
            [2] + c[3]))
        
        res = min(res, eval('(' + c[0] + z[0] + c[1] + ')' + z[2] + '(' + c[2] + z[
            1] + c[3] + ')'))
        
    #State of the program after the  for loop has been executed: `res` will contain the minimum value obtained from evaluating the expressions with permutations of `a`, `a` will remain a list of strings, `z` will remain a list of strings
    print(res)
#Overall this is what the function does:The function `func` does not accept any parameters. It takes two inputs of strings representing integers `a` and `z`, and performs all permutations of `a` to calculate the minimum result from evaluating different expressions. The expressions consist of a sequence of operations (+ or *) between the integers in `a` and `z`. The function then prints the minimum result obtained from these expressions.

