#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with length n. The sum of all n across all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = input()
        
        ans = 0
        
        i = 0
        
        while i < len(a) - 2:
            s = a[i:i + 3]
            if s == 'map' or s == 'pie':
                i += 3
                ans += 1
            else:
                i += 1
        
        print(ans)
        
    #State: a is the final input string, n is the original input integer, ans is the total count of occurrences where the substring s (of length 3) starting from index i is either 'map' or 'pie', i is len(a), and s is the last substring of a considered during the loop, which starts from index len(a)-2 and has a length of 3.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `n` and a string `s` of length `n`. For each test case, it counts and prints the number of occurrences of the substrings 'map' and 'pie' within `s`. The function does not return any value but prints the count for each test case.

