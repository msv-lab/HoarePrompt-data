#State of the program right berfore the function call: a, b, c, d are integers such that 0 <= a, b, c, d <= 1000. The sequence of operations consists of three characters, each being either '+' or '*'.**
def func():
    res = 100000000000000000000000000
    a = raw_input().split()
    z = raw_input().split()
    for c in itertools.permutations(a):
        res = min(res, eval('((' + c[0] + z[0] + c[1] + ')' + z[1] + c[2] + ')' + z
            [2] + c[3]))
        
        res = min(res, eval('(' + c[0] + z[0] + c[1] + ')' + z[2] + '(' + c[2] + z[
            1] + c[3] + ')'))
        
    #State of the program after the  for loop has been executed: `res` is updated to the minimum value calculated by the expression after all iterations of the loop have finished. The values of `c` and `z` may have been updated based on the calculations within the loop.
    print(res)
#Overall this is what the function does:The function does not accept any parameters. It reads input for four integer variables a, b, c, d with values between 0 and 1000. Then, it generates permutations of the values of a and performs calculations based on the sequence of operations specified by the input z. It finds the minimum result obtained from different combinations of operations on a and prints this minimum result.

