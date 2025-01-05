#State of the program right berfore the function call: n, x, and y are integers such that 1 ≤ n, x, y ≤ 10,000, and x ≤ n.
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10,000; `x` is an integer such that 1 ≤ `x` ≤ `n`; `y` is an integer such that 1 ≤ `y` ≤ 10,000; `p` is a list of substrings; `num` contains the integer values of all substrings in `p`.
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 10,000; `x` is an integer such that 1 ≤ `x` ≤ `n`; `y` is updated based on the calculation involving `num[0]`, `num[1]`, and `num[2]`; `p` is a list of substrings; `num` contains the integer values of all substrings in `p`. If `y` is an integer, it is printed as is. Otherwise, the output will be `int(y) + 1`, which indicates that the integer value of `y` will be incremented by 1 before printing.
#Overall this is what the function does:The function accepts input from the user, which is expected to consist of three space-separated integers. It calculates a value `y` based on the formula `(num[0] * num[2]) / 100 - num[1]`. The function prints `y` as an integer if it is a whole number; otherwise, it prints the integer value of `y` incremented by 1. The function does not return any value, and the potential edge cases include handling of input that does not conform to the expected format or values outside the specified range.

