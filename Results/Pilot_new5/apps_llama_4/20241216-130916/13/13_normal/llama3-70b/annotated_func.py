#State of the program right berfore the function call: The input is a string of length n, where n is an integer between 2 and 10^5 (inclusive), and a list of n characters where each character is either 'G' (representing a golden trophy) or 'S' (representing a silver trophy).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 10^5 (inclusive), `s` is a string of length `n` consisting of 'G' and 'S' characters, `golden` is a list of indices of 'G' characters in `s`, `max_beauty` is the maximum number of consecutive 'G' characters before an 'S', `curr_beauty` is either 0 or the count of 'G' characters at the end of `s`, `left` is at or past the last 'G' or 'S' character, and `right` equals `n`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 10^5 (inclusive), `s` is a string of length `n` consisting of 'G' and 'S' characters, `golden` is a list of indices of 'G' characters in `s`, `max_beauty_one_swap` is the maximum beauty score of 'G' characters that can be achieved by swapping one 'G' with an 'S' in `s`, or 0 if no 'G' is followed by 'S', and other variables (`max_beauty`, `curr_beauty`, `left`, `right`) retain their values as per their last updates before or within the loop, with `i` being `n-1` after the loop completes.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer n and a string s of length n, calculates the maximum consecutive 'G' characters before an 'S' and the maximum beauty score achievable by swapping one 'G' with an 'S' if a 'G' is followed by an 'S', then prints the maximum of these two scores, assuming the input string only contains 'G' and 'S' characters.

