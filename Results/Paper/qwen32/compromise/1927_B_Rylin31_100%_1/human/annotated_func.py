#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for each test case, a valid string s exists.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: t is the number of test cases, l is the length of the list s for the last test case, s is the final list of counts for the last test case, array is the list of integers for the last test case, ans is the final string constructed for the last test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it constructs and prints a string based on a list of integers. Each integer in the list specifies the position in the alphabet for the next character in the string, with the position being incremented each time it is used.

