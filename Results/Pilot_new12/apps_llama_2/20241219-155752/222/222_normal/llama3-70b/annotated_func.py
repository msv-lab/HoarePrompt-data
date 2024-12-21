#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer.
def func():
    n, k = map(int, input().split())
    l = (n + k - 1) // (k * 2 + 1)
    res = []
    for i in range(l):
        res.append(i * (k * 2 + 1) + 1)
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `k` is the original input integer, `l` is `(n + k - 1) // (k * 2 + 1)`, `res` is a list containing `l` elements of the form `i * (k * 2 + 1) + 1` for `i` ranging from 0 to `l-1`, or an empty list if `l` is 0
    print(l)
    print(' '.join(map(str, res)))
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is a positive integer and `k` is a non-negative integer. It calculates the value of `l` as `(n + k - 1) // (k * 2 + 1)` and generates a list `res` containing `l` elements of the form `i * (k * 2 + 1) + 1` for `i` ranging from 0 to `l-1`. If `l` is 0, an empty list is generated. The function then prints the value of `l` and the elements of the list `res`. The function does not return any values, instead, it prints the results directly to the console. The final state of the program includes the printed values of `l` and `res`, while the original input values `n` and `k` remain unchanged. The function handles potential edge cases where `k` is 0 or `n` and `k` result in a value of `l` equal to 0, in which case an empty list is printed.

