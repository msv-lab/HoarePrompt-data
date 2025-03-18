#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent the inclusive range of folder names to process.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' printed for each iteration of the loop based on the conditions specified within the loop body. For each iteration, the value of `n` (read from input) and string `s` (read from input) will determine whether 'YES' or 'NO' is printed. The initial values of `start`, `end`, and `t` will remain unchanged, and the output will reflect the results of the loop's conditions applied to the inputs provided during each iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a binary string `s`. For each test case, it checks specific conditions related to the string `s` and prints either 'YES' or 'NO' based on those conditions. The function does not modify any external variables and its return value is determined by the conditions evaluated during the processing of each test case.

