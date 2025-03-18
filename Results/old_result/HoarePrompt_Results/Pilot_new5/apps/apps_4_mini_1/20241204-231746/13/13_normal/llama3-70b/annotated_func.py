#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100000, and the second input is a string of length n consisting only of the characters 'G' and 'S'.
def func():
    n = int(input())
    s = input()
    golden = [i for i, x in enumerate(s) if x == 'G']
    max_beauty = 0
    curr_beauty = 0
    left = 0
    for right in range(n):
        if s[right] == 'G':
            curr_beauty += 1
        else:
            max_beauty = max(max_beauty, curr_beauty)
            curr_beauty = 0
            while left < right and s[left] != 'G':
                left += 1
            if left < right:
                curr_beauty += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 100000, `s` is an input string, `golden` is a list of indices where 'G' appears in `s`, `max_beauty` is the maximum count of consecutive 'G's found in `s`, `curr_beauty` is the count of consecutive 'G's at the end of the loop, `left` is the index of the first 'G' found that is less than the final value of `right`, and `right` is equal to `n`.
    max_beauty = max(max_beauty, curr_beauty)
    max_beauty_one_swap = 0
    for i in range(n - 1):
        if s[i] == 'G' and s[i + 1] == 'S':
            beauty = 1
            for j in range(i - 1, -1, -1):
                if s[j] == 'G':
                    beauty += 1
                else:
                    break
            for j in range(i + 2, n):
                if s[j] == 'G':
                    beauty += 1
                else:
                    break
            max_beauty_one_swap = max(max_beauty_one_swap, beauty)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 100000, `max_beauty_one_swap` is the maximum beauty obtainable by swapping one 'G' with an adjacent 'S', `max_beauty` is the maximum beauty calculated throughout the iterations of the loop, `curr_beauty` is the count of consecutive 'G's encountered during the loop execution, `left` is the index of the first 'G' found that is less than `right`, `right` is equal to `n`, and `golden` remains a list of indices where 'G' appears in `s`. If the loop does not execute, then `max_beauty_one_swap` remains 0 and all other variables retain their original values.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer `n` (where 2 <= n <= 100,000) and a string `s` of length `n` consisting only of the characters 'G' and 'S'. It calculates the maximum number of consecutive 'G's in the string and also determines the maximum possible count of consecutive 'G's that can be obtained by swapping one 'G' with an adjacent 'S'. Finally, it returns the greater of these two values.

