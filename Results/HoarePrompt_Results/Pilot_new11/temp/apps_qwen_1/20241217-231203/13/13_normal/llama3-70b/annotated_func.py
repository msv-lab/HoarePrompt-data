#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^5, and the second line contains a string of length n consisting only of the characters 'G' and 'S', where 'G' represents a golden trophy and 'S' represents a silver trophy.
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
        
    #State of the program after the  for loop has been executed: `left` is the index of the last 'G' in `s` or the length of `s` if no 'G' is found, `right` is the length of `s`, `s` is a string of length `n` consisting only of the characters 'G' and 'S', `golden` is a list of indices where `s` has the character 'G', `max_beauty` is the maximum number of consecutive 'G's encountered during the loop, `curr_beauty` is 0.
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
        
    #State of the program after the  for loop has been executed: `max_beauty_one_swap` is the maximum number of consecutive 'G's in `s` after swapping at most one 'S' with 'G', `max_beauty` is the maximum number of consecutive 'G's in `s` without any swaps, `golden` contains all indices of 'G' in `s`, `left` is the index of the last 'G' in `s` or the length of `s` if no 'G' is found, `right` is the length of `s`, `s` is a string of length `n` consisting only of 'G' and 'S', `n` is the length of `s`, `i` is `n - 1`, `j` is the index of the last 'G' in `s` that is at least 2 positions after `i`.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer \( n \) (where \( 2 \leq n \leq 10^5 \)) and a string \( s \) of length \( n \) consisting only of the characters 'G' and 'S', representing golden and silver trophies respectively. It calculates and prints the maximum number of consecutive golden trophies ('G') either without any swaps or with at most one swap of a silver trophy ('S') to a golden trophy ('G'). The function handles all potential edge cases, such as strings containing no golden trophies or no suitable positions for swapping.

