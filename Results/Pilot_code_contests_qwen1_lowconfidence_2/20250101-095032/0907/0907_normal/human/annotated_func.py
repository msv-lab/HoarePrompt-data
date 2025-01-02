#State of the program right berfore the function call: The input is a list of integers representing the parameter t for each customer, where the length of the list is at least 1 and at most 100,000, and each element in the list is an integer between -10 and 10, inclusive.
def func():
    a = dict()
    for i in range(-10, 11):
        a[i] = 0
        
    #State of the program after the  for loop has been executed: `a` is a dictionary where the keys are integers ranging from -10 to 10, and the value for each key is 0, `t` is a list of integers, and `i` is 10.
    n = input()
    t = map(int, raw_input().split())
    for i in range(n):
        a[t[i]] += 1
        
    #State of the program after the  for loop has been executed: `a` is a dictionary where the keys are integers ranging from -10 to 10, and the value for each key is the count of how many times that key appears in the first `n` elements of the list `t`, `t` is a list of integers from user input, `i` is `n`, `n` is a non-negative integer.
    ans = 0
    for i in range(-10, 0):
        ans += a[i] * a[-i]
        
    #State of the program after the  for loop has been executed: `a` is a dictionary where the keys are integers ranging from -10 to 10, and the value for each key is the count of how many times that key appears in the first `n` elements of the list `t`, `t` is a list of integers from user input, `i` is `n`, `n` is a non-negative integer, `ans` is 0.
    ans += a[0] * (a[0] - 1) / 2
    print(ans)
#Overall this is what the function does:The function accepts a list of integers `t` and counts the number of pairs of positive and negative integers that have equal absolute values. If no such pairs exist, it counts the number of occurrences of zero. The function returns this count as an integer. The function also handles the case where the list is empty by returning 0.

