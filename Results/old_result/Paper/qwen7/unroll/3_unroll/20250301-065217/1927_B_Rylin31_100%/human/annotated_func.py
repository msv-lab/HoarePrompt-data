#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, l is a positive integer such that 1 ≤ l ≤ 2⋅10^5; s is a list of l integers initialized to 0; array is a list of l integers read from input; ans is a string; after executing the loop, ans is constructed by iterating over array, appending the character corresponding to the value of s[j] + 97, and then incrementing s[j] by 1 for each j in array.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `l`, initializes a list `s` of length `l` with zeros, reads a list of integers `array` of length `l`, and constructs a string `ans` by converting each integer in `array` to a corresponding character based on the value of `s[j] + 97`. After processing each integer in `array`, it increments the corresponding value in `s`. Finally, it prints the constructed string `ans` for each test case.

