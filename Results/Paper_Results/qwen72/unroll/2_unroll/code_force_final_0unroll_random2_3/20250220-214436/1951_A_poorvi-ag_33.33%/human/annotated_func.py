#State of the program right berfore the function call: start and end are integers such that start <= end, and the current directory contains subfolders with numeric names.
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('1') == 2 and '11' in arr:
            results.append('no')
        
        if arr.count('1') % 2 == 0:
            if arr.count('1') == 2 and '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('no')
        
    #State: `start` and `end` remain unchanged, `t` is an input integer, `results` is a list containing 'yes' or 'no' based on the conditions evaluated for each input `arr` during the loop iterations.
    for r in results:
        print(r)
        
    #State: `start` and `end` remain unchanged, `t` is an input integer, `results` is a list containing 'yes' or 'no' based on the conditions evaluated for each input `arr` during the loop iterations. The loop has printed each element in the `results` list.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads an integer `n` and a string `arr` from the user. It then evaluates the string `arr` to determine if it meets specific conditions: if the string contains exactly two '1's and these '1's are adjacent, or if the number of '1's in the string is odd, it appends 'no' to a list `results`. Otherwise, it appends 'yes'. After processing all test cases, it prints each element in the `results` list. The function does not modify the `start` and `end` variables, and it does not return any value.

