#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an integer within the range [0, 359]. If `x` is 0, then 0 is printed. If `x` is not 0, the printed value is either 0, 1, 2, or 3 depending on the range of `x`.
#Overall this is what the function does:The function reads an integer `x` from the user, ensuring it is within the range \([-10^{18}, 10^{18}]\). It then computes the remainder of `x` when divided by 360, placing it in the range \([0, 359]\). Depending on the value of `x`, it prints one of four possible values: 0, 1, 2, or 3. Specifically, if `x` is 0, it prints 0; otherwise, it prints the result of \(((x + 90 - 1) // 90) \% 4\). The function does not return a value but modifies the output stream. Potential edge cases include the maximum and minimum values of \(x\) due to the range constraint. The function correctly handles all inputs within the specified range and prints the appropriate output based on the computed value of `x`.

