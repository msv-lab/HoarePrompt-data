#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100000, and a string of length n consisting of characters 'G' (for golden trophies) and 'S' (for silver trophies).
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 2 <= `n` <= 100000; `max_beauty` is the maximum number of consecutive 'G's in string `s`; `curr_beauty` is 0 (as it is reset at the end of the loop execution); `left` is the index of the first 'G' found before reaching the end of the string (or `n` if none found). If there are no 'G's in `s`, then `max_beauty` is 0.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 100000; `max_beauty_one_swap` is the maximum beauty value calculated from the string for all eligible 'G' and 'S' pairs encountered; `curr_beauty` remains 0 as it is not updated in the loop; `left` is unchanged from its initial value and reflects the first 'G' found or `n` if none found; `beauty` is the count of 'G's that can be formed by making at most one swap with an 'S' adjacent to any 'G' found during the iterations.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:The function accepts an integer `n` (where 2 <= n <= 100000) and a string `s` consisting of characters 'G' (for golden trophies) and 'S' (for silver trophies). It calculates the maximum number of consecutive 'G's that can be achieved in the string, either as-is or by swapping a single 'S' adjacent to a 'G' with another 'G'. The function returns the highest value of these consecutive 'G's. If there are no 'G's present, it returns 0.

