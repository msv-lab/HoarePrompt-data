#State of the program right berfore the function call: a, b, c, d are integers such that 0 ≤ a, b, c, d ≤ 1000, and there are three operations which are either '+' or '*'.
def func():
    res = 100000000000000000000000000
    a = raw_input().split()
    z = raw_input().split()
    for c in itertools.permutations(a):
        res = min(res, eval('((' + c[0] + z[0] + c[1] + ')' + z[1] + c[2] + ')' + z
            [2] + c[3]))
        
        res = min(res, eval('(' + c[0] + z[0] + c[1] + ')' + z[2] + '(' + c[2] + z[
            1] + c[3] + ')'))
        
    #State of the program after the  for loop has been executed: `res` is the minimum value calculated from all permutations of `a` evaluated with the expressions involving `z`, `a` is a list of strings obtained from user input, `c` is the last permutation of `a`, and `z` is a list of strings obtained from user input split by whitespace.
    print(res)
#Overall this is what the function does:The function accepts four integers (a, b, c, d) obtained through user input and evaluates all permutations of these integers with three operations (either '+' or '*') specified by additional user input. It computes the minimum result from these evaluations and prints it. The function does not explicitly handle invalid input or cases where the user does not provide exactly four integers or three operations.

