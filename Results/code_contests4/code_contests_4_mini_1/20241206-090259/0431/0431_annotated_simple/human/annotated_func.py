#State of the program right berfore the function call: a is a list of non-negative integers representing the number of garbage units produced each day, and k is a positive integer representing the maximum capacity of a bag. The length of a is n, where 1 ≤ n ≤ 200,000.
def func_1(a, k):
    bags, carry = 0, 0
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        
        bags += i // k
        
        carry = i % k
        
    #State of the program after the  for loop has been executed: `bags` is the total number of bags formed from all elements in `a`, `carry` is the leftover items after processing all elements in `a`, `a` is a list of elements used for calculation, and `k` is a positive integer that represents the capacity of each bag.
    if (carry != 0) :
        bags += 1
    #State of the program after the if block has been executed: *`bags` is the total number of bags formed from all elements in `a`, `carry` is the leftover items after processing all elements in `a`, `a` is a list of elements used for calculation, and `k` is a positive integer that represents the capacity of each bag. If `carry` is not equal to 0, `bags` is increased by 1 to account for the leftover items.
    return bags
    #The program returns the total number of bags formed from all elements in `a`, accounting for any leftover items if `carry` is not equal to 0.
#Overall this is what the function does:The function accepts a list of non-negative integers `a`, representing the number of garbage units produced each day, and a positive integer `k`, representing the maximum capacity of a bag. It calculates and returns the total number of bags needed to accommodate the garbage units, taking into account any leftover items from the last day's garbage after filling the bags. If there are any remaining garbage units that do not fit into a full bag, it adds one more bag to account for those leftovers.

#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200000, k is a positive integer such that 1 ≤ k ≤ 10^9, and a_i are non-negative integers such that 0 ≤ a_i ≤ 10^9 for each day i from 1 to n.
def func_2():
    _, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
#Overall this is what the function does:The function accepts two integers `k` and `n`, and a list of non-negative integers `a` representing daily values. It computes the minimum result of the function `func_1` applied to the list `a` and the reversed list `a[::-1]` with `k` as a parameter. The function does not return any value explicitly; it only prints the minimum result of the two function calls.

