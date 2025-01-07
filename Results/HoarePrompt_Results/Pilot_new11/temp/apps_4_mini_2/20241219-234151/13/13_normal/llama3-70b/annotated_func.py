#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100000, and the second input is a string of length n consisting of characters 'G' and 'S'.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 100000, `s` is a string of length `n` consisting of 'G' and 'S'; `golden` contains the indices of all 'G's in `s`; `curr_beauty` is the count of consecutive 'G's encountered at the end of the loop iteration; `max_beauty` is the maximum count of consecutive 'G's found in `s`; `left` is the index of the first 'G' encountered in `s` or `n` if there are no 'G's; `right` is equal to `n`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that `2 <= n <= 100000`, `max_beauty_one_swap` is the maximum beauty obtainable with one swap of a 'G' and adjacent 'S', with `s` being the original string. If there are no occurrences of 'G' followed by 'S', then `max_beauty_one_swap` remains 0.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function reads an integer `n` and a string `s` consisting of characters 'G' and 'S'. It calculates the longest sequence of consecutive 'G's in the string, referred to as `max_beauty`. It also computes the maximum potential sequence of consecutive 'G's obtainable by swapping one 'G' with an adjacent 'S', termed `max_beauty_one_swap`. Finally, it prints the maximum of `max_beauty` and `max_beauty_one_swap`. 
The function handles edge cases by ensuring that if there are no 'G's in the string, `max_beauty` will remain 0 (as initialized), and `max_beauty_one_swap` will also remain 0 if there are no valid 'G' followed by 'S' pairs. It effectively considers all possible ways to enhance the beauty score based on given conditions.

