#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 5000) representing the length of the string s. The next line contains a string s of length n consisting of characters '+' and '-'. There are no constraints on the sum of n over all test cases.
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
        
        print(P - M)
        
    #State: The final output state is the result of the last test case processed, which is the difference between the number of '+' characters and the number of '-' characters in the string of the last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a string of '+' and '-' characters. For each test case, it calculates the difference between the number of '+' characters and the number of '-' characters and prints this difference.

