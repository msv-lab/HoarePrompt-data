#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
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
        
    #State: The output state consists of the printed values of `ans` for each test case, where `ans` is the count of non-overlapping occurrences of "map" and "pie" in the string `s` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string `s`. For each test case, it counts the number of non-overlapping occurrences of the substrings "map" and "pie" in `s`, and prints this count.

