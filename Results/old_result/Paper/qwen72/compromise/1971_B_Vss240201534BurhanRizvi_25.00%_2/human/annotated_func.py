#State of the program right berfore the function call: The function `func` is expected to take no input parameters, but based on the problem description, it should be modified to take a string `s` as an input parameter, where `s` is a string of length at most 10 consisting of lowercase English letters.
def func():
    for _ in range(int(input())):
        s = input()
        
        s2 = ''.join(random.sample(s, len(s)))
        
        if s != s2:
            print('Yes')
            print(s2)
        else:
            print('No')
        
    #State: The loop will execute a number of times equal to the integer provided by the user. For each iteration, it will read a string `s` from the user, create a shuffled version `s2` of that string, and print 'Yes' followed by `s2` if `s2` is different from `s`. If `s2` is the same as `s`, it will print 'No'. The state of the variables `s` and `s2` will be updated for each iteration, but the final state of these variables after the loop finishes will be the values from the last iteration.
#Overall this is what the function does:The function `func` reads an integer from the user, which determines the number of iterations. For each iteration, it reads a string `s` from the user, shuffles the characters of `s` to create a new string `s2`, and prints 'Yes' followed by `s2` if `s2` is different from `s`. If `s2` is the same as `s`, it prints 'No'. After the loop completes, the final state of the program includes the values of `s` and `s2` from the last iteration, but these are not returned or used outside the function. The function does not return any value.

