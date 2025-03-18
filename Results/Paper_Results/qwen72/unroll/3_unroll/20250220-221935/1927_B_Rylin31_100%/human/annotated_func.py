#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5. For the given trace, there exists a suitable string s.
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
        
    #State: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5. For the given trace, there exists a suitable string s. The loop has executed all iterations, and the variable `ans` has been printed for each iteration, containing a string formed by mapping each integer in the input array to a character in the alphabet, starting from 'a'. The list `s` has been updated to reflect the number of times each index in the array has been encountered.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `l` representing the length of the list, and then reads a list of integers `array`. It generates a string `ans` by mapping each integer in `array` to a character in the alphabet, starting from 'a', and prints this string. The list `s` is used to track the number of times each index in `array` has been encountered, and it is updated accordingly. After processing all test cases, the function completes without returning any value.

