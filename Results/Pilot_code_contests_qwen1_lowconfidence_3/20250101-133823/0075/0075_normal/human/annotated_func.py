#State of the program right berfore the function call: n is an integer such that 0 ≤ n ≤ 2000000000.
def func():
    a = int(input())
    b = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
    res = 0
    if (a == 0) :
        res += b[0]
    #State of the program after the if block has been executed: *`n` is an integer such that 0 ≤ n ≤ 2000000000; `a` is an input integer; `b` is a list containing the values [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]; `res` is 1 if `a` is 0, otherwise `res` remains 0.
    while a > 0:
        res += b[a % 16]
        
        a /= 16
        
    #State of the program after the loop has been executed: `a` is 0, `res` is the sum of the elements in the list `b` indexed by the original values of `a` modulo 16
    print(res)
#Overall this is what the function does:The function takes an integer `a` as input within the range of 0 to 2000000000, and it calculates the sum of specific elements in the list `b` (which contains pre-defined values). It achieves this by repeatedly taking the remainder of `a` when divided by 16 and adding the corresponding value from the list `b` to the result variable `res`. The loop continues until `a` becomes 0. After the loop, the function prints the accumulated result `res`. The function handles the edge case where `a` is 0 by directly adding the first element of `b` to `res`.

