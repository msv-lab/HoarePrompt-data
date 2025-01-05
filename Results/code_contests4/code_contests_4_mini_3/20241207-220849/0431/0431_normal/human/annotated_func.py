#State of the program right berfore the function call: a is a list of non-negative integers representing the units of garbage produced for each of the n days, and k is a positive integer representing the capacity of each bag. The length of list a is equal to n, where 1 <= n <= 200000 and 1 <= k <= 10^9.
def func_1(a, k):
    bags, carry = 0, 0
    for i in a:
        if carry != 0:
            bags += 1
            i = max(0, i - carry)
        
        bags += i // k
        
        carry = i % k
        
    #State of the program after the  for loop has been executed: `bags` is the total number of bags formed from all elements of `a`, `carry` is the remainder of the last processed element of `a` when divided by `k`, `a` is a non-empty iterable.
    if (carry != 0) :
        bags += 1
    #State of the program after the if block has been executed: *`bags` is the total number of bags formed from all elements of `a`, `carry` is the remainder of the last processed element of `a` when divided by `k`, and since `carry` is not equal to 0, `bags` is increased by 1.
    return bags
    #The program returns the total number of bags formed from all elements of 'a', increased by 1 due to 'carry' not being equal to 0
#Overall this is what the function does:The function accepts a list `a` of non-negative integers representing the units of garbage produced over several days and a positive integer `k` representing the capacity of each bag. It calculates the total number of bags required to handle the garbage, taking into account any leftover garbage that doesn't fill an entire bag, and adds an extra bag if there is any leftover after processing all days. The function will return the total number of bags needed, which includes an additional bag if there is any leftover garbage remaining after the last day.

#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000) representing the number of days, k is a positive integer (1 ≤ k ≤ 1,000,000,000) representing the capacity of each bag, and a_i is a list of n non-negative integers (0 ≤ a_i ≤ 1,000,000,000) representing the number of units of garbage produced on each day.
def func_2():
    _, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    print(min(func_1(a, k), func_1(a[::-1], k)))
#Overall this is what the function does:The function accepts two parameters: a list of non-negative integers representing the units of garbage produced over `n` days and a positive integer `k` representing the capacity of each bag. It calculates the total number of bags required to accommodate the garbage over the days, considering both the original order of days and the reverse order, and returns the minimum number of bags needed. Note that the function assumes that the helper function `func_1` is correctly implemented to calculate the number of bags for the given list of garbage and bag capacity.

