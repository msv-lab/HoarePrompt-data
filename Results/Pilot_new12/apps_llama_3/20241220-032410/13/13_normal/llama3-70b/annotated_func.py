#State of the program right berfore the function call: The input consists of an integer n (2 <= n <= 10^5) and a string of length n consisting of characters 'G' and 'S', where 'G' represents a golden trophy and 'S' represents a silver trophy.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 2 and 10^5 (inclusive), `s` is a string of length `n` consisting of characters 'G' and 'S', `golden` is a list of indices of 'G' characters in `s`, `right` equals `n`, `max_beauty` is the maximum number of consecutive 'G' characters without interruption by an 'S' that doesn't follow a 'G', `curr_beauty` reflects the state of the last character and sequence, and `left` points to the last 'G' character or is at the end of the string.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 2 and 10^5 (inclusive), `s` is a string of length `n` consisting of characters 'G' and 'S', `golden` is a list of indices of 'G' characters in `s`, `right` equals `n`, `max_beauty` and `curr_beauty` reflect values determined outside this loop or before it started, `left` points to the last considered 'G' character or the end of the string based on its initial state or updates outside this loop, `max_beauty_one_swap` is the maximum beauty score found for all 'G' 'S' pairs in `s`, `i` has iterated over all indices from 0 to `n-2`, and `j` and `beauty` are temporary variables whose final states are not significant after the loop completes.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer `n` and a string `s` of length `n` consisting of 'G' and 'S' characters as input, and returns the maximum beauty score, which is the maximum number of consecutive 'G' characters that can be achieved either with no swaps or with one swap of a 'G' and an 'S' that immediately follows it, ignoring any 'S' characters that do not follow a 'G' character. The function handles edge cases such as an empty string, a string with no 'G' characters, a string with no 'S' characters, and a string where 'G' and 'S' characters are alternating. The final state of the program after it concludes is that it has printed the maximum beauty score based on the input parameters.

