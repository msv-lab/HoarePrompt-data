#State of the program right berfore the function call: **
def func_1(a, k):
    bags, carry = 0, 0
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        
        bags += i // k
        
        carry = i % k
        
    #State of the program after the  for loop has been executed: `bags` is the total number of bags calculated according to the loop, `carry` is the remainder of the last `i` divided by `k`, `a` still has at least one element left to iterate over
    if (carry != 0) :
        bags += 1
    #State of the program after the if block has been executed: *`bags` is the total number of bags calculated according to the loop, `carry` is the remainder of the last `i` divided by `k`, `a` still has at least one element left to iterate over. If `carry` is not equal to 0, `bags` is incremented by 1 and `carry` is updated to the remainder of the last `i` divided by `k`. Additionally, `a` still has at least one element left to iterate over.
    return bags
    #The program returns the total number of bags calculated after the loop
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `k`. It iterates over the elements of `a`, calculating the total number of bags based on the division of each element by `k` and any remaining amount carried over to the next iteration. The function returns the total number of bags calculated after the loop. If there is a remaining `carry` after the loop, an additional bag is added.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= n <= 2*10^5 and 1 <= k <= 10^9. The list a_i contains non-negative integers.**
def func_2():
    _, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
#Overall this is what the function does:The function `func_2` reads input values for `n` and `k`, as well as a list of integers `a`. It then calls `func_1` twice with different arguments derived from `a` and `k`, and prints the minimum result obtained from these calls. The actual calculations and return values of `func_1` are not specified in the given information.

