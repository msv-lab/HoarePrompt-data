#State of the program right berfore the function call: a and b are positive integers such that 1 ≤ a ≤ b ≤ 10.
def func():
    a, b = map(int, input().split())
    years = 0
    while a <= b:
        a *= 3
        
        b *= 2
        
        years += 1
        
    #State of the program after the loop has been executed: `a` is \(3^y \cdot a_0\), `b` is \(2^y \cdot b_0\), `years` is \(2^y - 1\)
    print(years)
#Overall this is what the function does:The function func does not accept any parameters as per the annotated code. Instead, it takes two integers `a` and `b` as inputs from the user, where `a` and `b` are positive integers such that \(1 \leq a \leq b \leq 10\). The function then enters a loop where `a` is multiplied by 3, `b` is multiplied by 2, and the `years` counter is incremented until `a` becomes greater than `b`. After the loop ends, the function prints the value of `years`.

The functionality of the function is to:
**Take two positive integers `a` and `b` as input, where \(1 \leq a \leq b \leq 10\), and determine the number of years required for `a` to become greater than `b` through repeated multiplication by 3 and 2, respectively.**

