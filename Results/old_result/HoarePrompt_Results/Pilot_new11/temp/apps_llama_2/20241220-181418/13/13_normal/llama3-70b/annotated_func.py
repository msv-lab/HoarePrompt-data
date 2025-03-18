#State of the program right berfore the function call: the function takes no arguments, but the program's input variables are an integer n (2 <= n <= 10^5) and a string of length n consisting of characters 'G' and 'S', where 'G' represents a golden trophy and 'S' represents a silver trophy.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 2 and 10^5 (inclusive), `s` is a string of length `n` consisting of characters 'G' and 'S', `golden` is a list of indices of 'G' characters in `s`, `max_beauty` is the maximum length of consecutive 'G' characters in `s`.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 10^5 (inclusive), `s` is a string of length `n` consisting of characters 'G' and 'S', `golden` is a list of indices of 'G' characters in `s`, `i` is `n-2`, `max_beauty_one_swap` is the maximum achievable beauty by swapping any 'G' followed by an 'S' in `s`.
    print(max(max_beauty, max_beauty_one_swap))
#Overall this is what the function does:This function calculates and prints the maximum achievable beauty of a sequence of golden ('G') and silver ('S') trophies, considering two scenarios: (1) the maximum consecutive length of 'G' trophies in the given sequence, and (2) the maximum length of consecutive 'G' trophies achievable by swapping a single 'G' trophy followed by an 'S' trophy with the adjacent 'S' trophy. The function takes no arguments but reads an integer `n` (2 <= n <= 10^5) and a string `s` of length `n` consisting of 'G' and 'S' characters from the input. The function does not modify the input variables but consumes them to calculate the maximum beauty. After execution, the function prints the maximum beauty between the two scenarios. The function handles edge cases where the input sequence is entirely composed of 'G' or 'S' trophies, as well as cases where the maximum beauty is achieved by swapping a 'G' trophy followed by an 'S' trophy.

