#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^5, and the second input is a string of length n consisting only of characters 'G' and 'S'.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^5\); `s` is a string of length `n` consisting only of characters 'G' and 'S'; `golden` contains the indices of 'G' in `s`; `max_beauty` is the maximum length of consecutive 'G' characters found in `s`; `curr_beauty` represents the beauty score of the last sequence of 'G's ending at the final character of `s`; `left` indicates the index of the last 'G' encountered before the end of the string, and `right` is equal to `n - 1`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(2 \leq n \leq 10^5\); `max_beauty_one_swap` is the maximum beauty score achievable by swapping one 'G' adjacent to an 'S', where `beauty` represents the count of consecutive 'G's connected to an 'S'; if the loop does not execute, `max_beauty_one_swap` remains 0.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function reads an integer `n` and a string `s` of length `n`, consisting of the characters 'G' (golden) and 'S' (silver). It calculates the maximum sequence of consecutive 'G' characters found in `s`, denoted as `max_beauty`, and then considers the possibility of swapping a 'G' adjacent to an 'S' to maximize the beauty score further. It computes another score, `max_beauty_one_swap`, representing the maximum beauty achievable through such a swap. Finally, the function outputs the greater of `max_beauty` and `max_beauty_one_swap`. 

The function does not return any value; instead, it prints the result. Notably, if the string contains only 'S' characters, both `max_beauty` and `max_beauty_one_swap` would remain 0, and the output will be 0. This highlights that the edge cases of not having any 'G' characters are handled. Furthermore, the processing assumes that valid input is provided, as indicated in the preconditions. However, there is an implicit assumption in the code that it never encounters the case of `n` being less than 2 or more than 100,000, as enforced by the constraints given before the function call.

