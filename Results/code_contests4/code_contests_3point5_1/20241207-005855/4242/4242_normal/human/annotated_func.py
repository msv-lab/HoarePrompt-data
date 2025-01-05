#State of the program right berfore the function call: ** The input consists of four integers a, b, c, d where 0 ≤ a, b, c, d ≤ 1000. The sequence of operations consists of three signs either '+' or '*' in the order of performing.
def func():
    res = 100000000000000000000000000
    a = raw_input().split()
    z = raw_input().split()
    for c in itertools.permutations(a):
        res = min(res, eval('((' + c[0] + z[0] + c[1] + ')' + z[1] + c[2] + ')' + z
            [2] + c[3]))
        
        res = min(res, eval('(' + c[0] + z[0] + c[1] + ')' + z[2] + '(' + c[2] + z[
            1] + c[3] + ')'))
        
    #State of the program after the  for loop has been executed: `res` will contain the minimum value obtained from all the evaluations in the loop, `a` will remain unchanged, `z` will remain unchanged
    print(res)
#Overall this is what the function does:The function does not accept any parameters. It reads input consisting of four integers a, b, c, d where 0 ≤ a, b, c, d ≤ 1000 and a sequence of three signs either '+' or '*'. It then evaluates different expressions formed by performing the sequence of operations on the input integers a, b, c, and d. The function calculates the minimum value obtained from these evaluations and prints it as the final result.

