#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        count = 1
        
        flag = False
        
        j = 0
        
        while j < len(s) - 1:
            if s[j] != s[j + 1]:
                count += 1
                if s[j] == '0' and s[j + 1] == '1':
                    flag = True
                    j += 1
            j += 1
        
        if flag:
            count -= 1
        
        print(count)
        
    #State: Output State: `t` is a positive integer between 1 and 500 inclusive, `i` is 3, `s` is the last input string processed, `count` is the final count calculated from the last string, `flag` is True, and `j` is equal to the length of `s` minus 1. The value of `count` is determined by the length of the string minus one, adjusted based on whether the specific sequence '01' was found and the conditions within the loop were met.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and a binary string \( s \). For each test case, it calculates the number of segments in the binary string \( s \) where consecutive characters differ, adjusting the count if the sequence '01' is found. The function prints the final count for each test case and does not return any value.

