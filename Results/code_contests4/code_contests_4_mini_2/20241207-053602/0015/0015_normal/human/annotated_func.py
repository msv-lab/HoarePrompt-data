#State of the program right berfore the function call: n, x, and y are integers such that 1 ≤ n, x, y ≤ 10^4 and x ≤ n.
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^4; `x` is an integer such that 1 ≤ `x` ≤ `n`; `y` is an integer such that 1 ≤ `y` ≤ 10^4; `p` is a list of substrings; `num` is a list of integers which contains the integer conversion of each element in `p`.
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 10^4; `x` is an integer such that 1 ≤ `x` ≤ `n`; `y` is calculated as (num[0] * num[2]) / 100 - num[1]; `p` is a list of substrings; `num` is a list of integers which contains the integer conversion of each element in `p`. If `y` is an integer (i.e., `y` is divisible by 1), the value of `y` is printed as an integer. Otherwise, `int(y) + 1` is printed as the output.
#Overall this is what the function does:The function accepts input from the user, splits the input string into substrings, converts them to integers, and calculates a value `y` using the formula `(num[0] * num[2]) / 100 - num[1]`. It then prints the ceiling of `y` if `y` is not an integer, otherwise, it prints `y` as an integer. The function does not accept parameters directly nor does it return a value; it only outputs the result to the console. Additionally, there is a lack of input validation which may lead to errors if the input does not meet expectations.

