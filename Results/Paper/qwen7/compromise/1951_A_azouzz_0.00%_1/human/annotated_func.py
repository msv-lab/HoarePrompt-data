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
        
    #State: The output state will consist of 'YES' or 'NO' printed for each iteration of the loop based on the conditions specified in the loop body. The specific sequence of 'YES' and 'NO' will depend on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple inputs, each consisting of an integer `n` followed by a string `s`. It checks if the string `s` meets certain conditions and prints either 'YES' or 'NO' for each input. Specifically, it prints 'YES' if the count of '1's in `s` is 2 or less, or if '11' does not appear in `s`. Otherwise, it prints 'NO'. The function does not accept any parameters and does not return any value.

