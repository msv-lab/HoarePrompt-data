#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3*10^5, and a is a string of length n consisting only of '0' and '1'.
def func_1():
    n = int(input())
    a = input()
    S = [[0, 0]]
    for s in a:
        x, y = S[-1]
        
        if s == '0':
            x += 1
        else:
            y += 1
        
        S.append([x, y])
        
    #State: Output State: `a` is an input string consisting only of '0' and '1', and `n` is the length of the input string `a`; `S` is a list containing sublists where each sublist contains two integers, with the first integer representing the count of '0's encountered in `a` up to the current character, and the second integer representing the count of '1's encountered up to the current character.
    ans = -1
    for i in range(n + 1):
        left = S[i][0]
        
        lsum = i
        
        right = S[-1][1] - S[i][1]
        
        rsum = n - i
        
        if left * 2 < lsum or right * 2 < rsum:
            continue
        elif abs(n / 2 - i) < abs(n / 2 - ans):
            ans = i
        
    #State: Output State: `a` is an input string consisting only of '0' and '1', and `n` is the length of the input string `a`; `S` is a list containing sublists where each sublist contains two integers, with the first integer representing the count of '0's encountered in `a` up to the current character, and the second integer representing the count of '1's encountered up to the current character; `ans` is the index `i` that minimizes the absolute difference between `i` and `n/2`, subject to the condition that the number of '0's seen so far is at least half the number of characters seen so far, and the number of '1's remaining is at least half the number of characters remaining.
    print(ans)
    #This is printed: ans (where ans is the index that minimizes the absolute difference between i and n/2, subject to the conditions that the number of '0's seen so far is at least half the number of characters seen so far, and the number of '1's remaining is at least half the number of characters remaining)
#Overall this is what the function does:The function processes an input string `a` consisting only of '0' and '1', calculates the count of '0's and '1's up to each character, and finds the index `i` that minimizes the absolute difference between `i` and `n/2`. This index `i` satisfies the condition that the number of '0's seen so far is at least half the number of characters seen so far, and the number of '1's remaining is at least half the number of characters remaining. The function prints this index `i`.

#State of the program right berfore the function call: n is an integer such that 3 <= n <= 3 * 10^5, and a is a string of length n consisting only of '0' and '1'.
def func_2():
    for _ in range(int(input())):
        func_1()
        
    #State: Output State: a is a string of length n consisting only of '0' and '1'. The value of n remains unchanged and is within the range 3 <= n <= 3 * 10^5. The variable `func_1` is called multiple times (equal to the number of iterations specified by `input()`), but its exact behavior is not defined, so the content of `a` may or may not change; however, no information about `a` changing is provided, so we assume `a` remains unchanged.
#Overall this is what the function does:The function does not accept any parameters and returns nothing. It reads an integer from user input, which specifies the number of times to call the `func_1` function. After calling `func_1` the specified number of times, the function ensures that the string `a` remains unchanged and consists of '0' and '1' characters, with a length between 3 and 300,000 inclusive.

