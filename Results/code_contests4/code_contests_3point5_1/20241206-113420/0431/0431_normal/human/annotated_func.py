#State of the program right berfore the function call: **
def func_1(a, k):
    bags, carry = 0, 0
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        
        bags += i // k
        
        carry = i % k
        
    #State of the program after the  for loop has been executed: `bags` will be increased by the integer division of the sum of all elements in list `a` by `k`, `carry` will be the remainder of the sum of all elements in list `a` divided by `k`, `a` will be an empty list, and `i` will be 0
    if (carry != 0) :
        bags += 1
    #State of the program after the if block has been executed: *`bags` will be increased by the integer division of the sum of all elements in list `a` by `k` and `carry` will be the remainder of the sum of all elements in list `a` divided by `k`. The list `a` will remain empty, `i` will be 0, and if `carry` is not equal to 0, `bags` will be increased by 1.
    return bags
    #The program returns the number of bags after the integer division of the sum of all elements in list `a` by `k`, considering any remainder as an additional bag
#Overall this is what the function does:The function func_1 accepts a list of integers `a` and an integer `k`. It iterates through the elements of `a`, calculating the sum and dividing it by `k` to determine the number of bags. If there is a remainder after division, an additional bag is added. The function returns the total number of bags required.

#State of the program right berfore the function call: **
def func_2():
    _, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
#Overall this is what the function does:The function `func_2` reads input values from the user, calculates two minimum values by calling `func_1` with different arguments, and prints the smaller of the two results. It does not accept any parameters and does not have a return value.

