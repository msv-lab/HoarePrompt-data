#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and s is a string of length n containing only "U" and "D".
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: Output State: `results` is a list of 'yes' and 'no' strings, where each string corresponds to whether the count of 'U' in the input string is odd ('yes') or even ('no'). The length of the list is equal to the value of `t`.
    for i in results:
        print(i)
        
    #State: The loop will print each string in the list `results` on a new line.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (the number of cases), a positive integer \( n \) (the length of the string), and a string \( s \) consisting of 'U' and 'D'. For each test case, it checks if the count of 'U' in the string \( s \) is odd or even and appends 'yes' or 'no' to the results list accordingly. Finally, it prints each element in the results list, one per line.

