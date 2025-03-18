#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D".
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if n % 2 == 0:
            results.append('no')
        elif arr.count('U') > arr.count('D'):
            results.append('yes')
        else:
            results.append('no')
        
    #State: results is a list of 'no' and 'yes' based on the conditions given in the loop. For each iteration, if `n` is even, 'no' is appended; otherwise, if the count of 'U' in the input string `arr` is greater than the count of 'D', 'yes' is appended; otherwise, 'no' is appended.
    for i in results:
        print(i)
        
    #State: Output State: The output state depends on the initial list `results` and the conditions specified in the loop. Since no specific `results` list or `arr` string is provided, we cannot determine the exact output. However, the loop will print each element of the `results` list as it is, without modifying it.
    #
    #If we assume an example where `results = ['no', 'yes', 'no']` and `arr` is a string like "UUDD", then the loop would print:
    #
    #```
    #no
    #yes
    #no
    #```
    #
    #Output State: ['no', 'yes', 'no'].
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) (number of test cases), a positive integer \( n \) (length of a string), and a string \( s \) of length \( n \) containing only "U" and "D". For each test case, it checks if \( n \) is even or if the number of "U"s in \( s \) is greater than the number of "D"s. If \( n \) is even, it appends "no" to the results list; otherwise, it appends "yes" or "no" based on the comparison of "U"s and "D"s. Finally, it prints each element of the results list.

