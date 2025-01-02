#State of the program right berfore the function call: a, b, c, and d are integers such that 1 ≤ a, b, c, d ≤ 100.
def func():
    a, b = map(int, raw_input().split())
    c, d = map(int, raw_input().split())
    if (b == d) :
        print(b)
        sys.exit()
    #State of the program after the if block has been executed: *`a` and `b` are updated from user input, `c` and `d` are the integers provided by the user's input. If `b` is equal to `d`, the program has terminated.
    t = d - b
    for x in range((a * c + d + b) / a + 11):
        if (a * x - t) % c == 0:
            print(b + a * x)
            sys.exit()
        
    #State of the program after the  for loop has been executed: `a` is a non-zero integer, `b` and `d` are such that `d + b` is non-negative, `c` is a non-negative integer, and `t` is `d - b`. If the loop finds an `x` such that `(a * x - t) % c == 0`, the program prints `b + a * x` and exits. If no such `x` is found, the loop completes without printing, and the values of `a`, `b`, `c`, and `d` remain unchanged.
    print(-1)
#Overall this is what the function does:The function reads two pairs of integers from the user, `(a, b)` and `(c, d)`, where each integer is within the range of 1 to 100. The function then checks if `b` is equal to `d`. If they are equal, the function prints `b` and terminates. If `b` is not equal to `d`, the function calculates a value `t` as `d - b` and iterates over a range of values determined by the expression `(a * c + d + b) / a + 11`. For each value `x` in this range, the function checks if `(a * x - t) % c == 0`. If such an `x` is found, the function prints `b + a * x` and terminates. If no such `x` is found, the function prints `-1` and terminates. The function does not return any value; it only prints to the console and exits.

