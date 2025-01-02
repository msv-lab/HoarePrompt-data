#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 100. a_i and b_i are strings representing valid T-shirt sizes for the previous year and the current year, respectively, for i ranging from 1 to n.
def func():
    if (__name__ == '__main__') :
        n = int(raw_input())
        dic = {}
        for i in xrange(n):
            s = raw_input()
            
            if not dic.has_key(s):
                dic[s] = 1
            else:
                dic[s] += 1
            
        #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ n ≤ 100, `i` is n-1, `a_i` and `b_i` are strings representing valid T-shirt sizes for the previous year and the current year, respectively, for i ranging from 1 to n, `dic` is a dictionary where each key is a unique T-shirt size input during the loop, and the value associated with each key is the count of how many times that T-shirt size was input. If the loop does not execute (i.e., `n` is 0), `dic` remains an empty dictionary.
        ans = 0
        for i in xrange(n):
            s = raw_input()
            
            if dic.has_key(s) and dic[s] > 0:
                dic[s] -= 1
            else:
                ans += 1
            
        #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ n ≤ 100, `i` is n-1, `dic` is a dictionary where each key is a unique T-shirt size input during the loop, and the value associated with each key is the count of how many times that T-shirt size was input minus the number of times it was matched and decremented. `ans` is the number of unique T-shirt sizes that were not found in `dic` or whose count in `dic` was 0 when they were encountered. If the loop does not execute (i.e., `n` is 0), `dic` remains an empty dictionary, and `ans` is 0.
        print(ans)
    #State of the program after the if block has been executed: *`n` is an integer where 1 ≤ n ≤ 100. If the script is the main entry point, `i` is set to `n - 1`, `dic` is a dictionary where each key is a unique T-shirt size input during the loop, and the value associated with each key is the count of how many times that T-shirt size was input minus the number of times it was matched and decremented. `ans` is the number of unique T-shirt sizes that were not found in `dic` or whose count in `dic` was 0 when they were encountered. If the script is not the main entry point, the state remains unchanged.
#Overall this is what the function does:The function processes a series of T-shirt size inputs for two consecutive years. It reads `n` T-shirt sizes for the previous year and stores their counts in a dictionary. Then, it reads `n` T-shirt sizes for the current year and decrements the counts in the dictionary if a matching size is found. Finally, it prints the number of T-shirt sizes from the current year that do not have a match in the previous year's sizes. The function only executes if it is the main entry point of the script. If the script is not the main entry point, no action is taken. Edge cases include scenarios where `n` is 0, resulting in an empty dictionary and `ans` being 0. Missing functionality includes handling invalid input formats, such as non-integer values for `n` or non-string values for T-shirt sizes.

