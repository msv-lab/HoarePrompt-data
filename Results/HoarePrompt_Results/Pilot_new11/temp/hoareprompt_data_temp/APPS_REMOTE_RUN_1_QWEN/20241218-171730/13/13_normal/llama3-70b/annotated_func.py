#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and the second line of input is a string consisting of n characters, each of which is either 'G' or 'S', representing golden and silver trophies respectively.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^5\), `s` is a string of length `n` consisting of characters 'G' or 'S', `golden` is a list of integers containing the indices of all characters in `s` that are equal to 'G', `max_beauty` is the length of the longest consecutive sequence of 'G's in `s`, `curr_beauty` is 0, `left` is the index of the last 'G' in the string `s`, or `n` if there are no 'G's, and `right` is `n`.
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
        
    #State of the program after the  for loop has been executed: `i` is a non-negative integer less than `n-1`, `j` is either `i + 2` or the position just after the last consecutive 'G' in the string starting from index `i + 1` (if the condition `s[i] == 'G' and s[i + 1] == 'S'` is true), `beauty` is the count of consecutive 'G's from `i - 1` to the first non-'G' character in the range from `i + 1` to `j`, `left` is the index of the last 'G' in the string `s`, or `n` if there are no 'G's, `right` is `n`, `max_beauty` is the maximum of its current value and `curr_beauty`, `curr_beauty` is 0, `max_beauty_one_swap` is the maximum value among all `beauty` calculated during the loop iterations when `beauty` > 0, and `golden` is a list of indices of all characters in `s` that are equal to 'G'.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function processes a string `s` of length `n` consisting of characters 'G' (golden) and 'S' (silver). It calculates two values: `max_beauty`, which is the length of the longest consecutive sequence of 'G's in the string, and `max_beauty_one_swap`, which is the maximum beauty (length of consecutive 'G's) achievable by swapping exactly one 'S' to 'G'. The function then prints the maximum of these two values. The function handles edge cases where there are no 'G's in the string.

