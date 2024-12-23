#State of the program right berfore the function call: n is an even number, and there is a list of n integers (each between 1 and 100) representing the numbers written on the cards.
def func():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a list of `n` input integers, the original list of `n` integers remains unchanged, `i` is `n-1` if `n` is greater than 0, `i` is undefined if `n` is 0.
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a list of `n` input integers, `d` is a dictionary where each key is a unique integer from `a` and its corresponding value is the count of that integer in `a`.
    c = 0
    a1, a2 = -1, -1
    for i in d:
        if d[i] == n // 2:
            if c == 0:
                a1 = i
                c += 1
            else:
                a2 = i
                break
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a list of `n` input integers, `d` is a dictionary where each key is a unique integer from `a` and its corresponding value is the count of that integer in `a`, `c` is either 0 or 1, `a1` is either -1 or the first integer with a count of `n // 2`, `a2` is either -1 or the second integer with a count of `n // 2`.
    if (a1 != -1 and a2 != -1) :
        print('YES')
        print(a1, a2)
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `a` is a list of `n` input integers, `d` is a dictionary where each key is a unique integer from `a` and its corresponding value is the count of that integer in `a`, `c` is either 0 or 1, `a1` is either -1 or the first integer with a count of `n // 2`, `a2` is either -1 or the second integer with a count of `n // 2`. If both `a1` and `a2` are not -1, 'YES' has been printed to the console along with the values of `a1` and `a2`. Otherwise, 'NO' has been printed to the console.
#Overall this is what the function does:The function accepts an even number `n` as input and then `n` integers between 1 and 100. It counts the occurrences of each integer in the list and checks if there are exactly two integers that each appear `n/2` times. If such integers are found, it prints 'YES' followed by the two integers; otherwise, it prints 'NO'. The function does not return any value but provides output to the console indicating whether the list contains a pair of integers that each account for half of the total list length, considering the input specifications.

