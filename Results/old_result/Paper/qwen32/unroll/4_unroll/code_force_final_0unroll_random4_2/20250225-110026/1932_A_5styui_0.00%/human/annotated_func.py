#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 50, and the path is a string of n characters where each character is either '.', '@', or '*', with the first character guaranteed to be '.'.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: t is an integer such that 1 <= t <= 1000; n is an integer such that 1 <= n <= 50; path is a string of n characters where each character is either '.', '@', or '*', with the first character guaranteed to be '.'; a is an input integer; s is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a path string. For each path, it counts the number of '@' characters and prints this count. The function does not modify the input path or the number of test cases; it only outputs the count of '@' characters for each path.

