#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of characters '+' and '-', with no other characters.
def func():
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(abs(P - M))
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to the length of the string `e`, `s` will remain the same input integer, `e` will be an empty string, `P` will be the total number of '+' characters in the original string `e`, and `M` will be the total number of '-' (or any other character that is not '+') characters in the original string `e`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `s` and a string `e` containing characters '+' and '-'. For each test case, it counts the number of '+' characters and the number of '-' characters in the string `e`. After processing all test cases, it prints the absolute difference between the counts of '+' and '-' characters for each string `e`. The function does not return any value but outputs the results for each test case.

