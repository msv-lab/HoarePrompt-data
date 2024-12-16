#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and the second line of input is a string consisting of n characters, each being either 'G' or 'S', where 'G' represents a golden trophy and 'S' represents a silver trophy.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer input by the user within the range \(2 \leq n \leq 10^5\), `s` is a string consisting of `n` characters, each being either 'G' or 'S', `golden` is a list of indices of 'G' in `s`, `max_beauty` is the maximum beauty found during the traversal of `s`, `curr_beauty` is the beauty at the last position `right` where `s[right]` is 'G' or 0, `left` is the index of the last 'G' character in `s` or `n` if no 'G' characters are present.
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
        
    #State of the program after the  for loop has been executed: `i` is `n - 1`, `n` is the length of the string `s`, `j` is the largest index such that `s[j] == 'G'` and `j >= i + 2`, or `n` if no such index exists, `beauty` is the maximum value of `beauty` calculated for all valid pairs, `max_beauty_one_swap` is the maximum value of `beauty` across all iterations.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer `n` such that \(2 \leq n \leq 10^5\) and a string `s` consisting of `n` characters, each being either 'G' or 'S', representing golden and silver trophies respectively. It calculates the maximum beauty of the trophies by either keeping them as they are or by swapping one silver trophy for a golden one. The maximum beauty is defined as the maximum number of consecutive golden trophies. The function returns the higher of the original maximum beauty and the maximum beauty after one possible swap.

