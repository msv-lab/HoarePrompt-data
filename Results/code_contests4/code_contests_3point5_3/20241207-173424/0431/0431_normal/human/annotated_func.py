#State of the program right berfore the function call: **
def func_1(a, k):
    bags, carry = 0, 0
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        
        bags += i // k
        
        carry = i % k
        
    #State of the program after the  for loop has been executed: `bags` is updated based on the floor division of the sum of all elements in `a` by `k`, `carry` is the remainder of the sum of all elements in `a` divided by `k`
    if (carry != 0) :
        bags += 1
    #State of the program after the if block has been executed: *`bags` is updated based on the floor division of the sum of all elements in `a` by `k`, `carry` is the remainder of the sum of all elements in `a` divided by `k`. If `carry` is not equal to 0, `bags` is incremented by 1.
    return bags
    #The program returns the updated value of 'bags' after performing the floor division of the sum of all elements in 'a' by 'k' and incrementing by 1 if the remainder 'carry' is not equal to 0
#Overall this is what the function does:The function `func_1` accepts two parameters, a list of integers `a` and an integer `k`. It calculates the number of bags needed to carry all the elements in `a` based on the floor division of the sum of all elements in `a` by `k`. If there is a non-zero remainder `carry`, an additional bag is required. The function then returns the total number of bags needed.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9. a_i are integers such that 0 ≤ a_i ≤ 10^9 for each i.**
def func_2():
    _, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
#Overall this is what the function does:The function `func_2` reads two inputs, `n` and `k`, and a list of integers `a`. It then calls `func_1` twice with different inputs and prints the minimum result of these function calls. The function `func_2` does not accept any parameters explicitly.

