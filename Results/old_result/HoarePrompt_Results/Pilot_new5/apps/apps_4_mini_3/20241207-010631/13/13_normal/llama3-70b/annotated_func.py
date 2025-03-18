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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 100000, `s` is a string of length `n` consisting only of 'G' and 'S', `golden` contains the indices of 'G' in `s`, `max_beauty` is the maximum continuous count of 'G's found in `s`, `curr_beauty` is the count of the last segment of consecutive 'G's, `left` is the index of the first 'G' in `s` or equal to `n` if there are no 'G's in `s`, and `right` is equal to `n - 1`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 100000; `max_beauty_one_swap` is the maximum beauty obtainable by swapping one 'G' with one adjacent 'S' in `s`; `i` is equal to `n - 1` after all iterations, which indicates that the loop has checked all pairs of 'G' and 'S'. If there are no such pairs where `s[i]` is 'G' and `s[i + 1]` is 'S', then `max_beauty_one_swap` remains 0.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer `n` (where 2 <= n <= 100000) and a string `s` of length `n` consisting of characters 'G' and 'S'. It calculates the maximum number of consecutive 'G's found in the string and the maximum beauty obtainable by swapping one 'G' with one adjacent 'S'. The function then prints the greater of these two values. If there are no 'G's in the string, the maximum beauty will be calculated based on the available 'G's surrounding an 'S' for potential swapping.

