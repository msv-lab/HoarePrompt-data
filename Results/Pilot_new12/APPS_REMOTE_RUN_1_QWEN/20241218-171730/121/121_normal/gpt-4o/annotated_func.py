#State of the program right berfore the function call: The input consists of two lines. The first line contains an integer n where 4 ≤ n ≤ 255, representing the length of the genome string. The second line contains a string s of length n, consisting of characters 'A', 'C', 'G', 'T', and '?', representing the coded genome.
def func_1():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #None
    #State of the program after the if block has been executed: `data` is a list containing [integer value of `data[0]`, string `s`], `s` is the string from `data[1]`, and `n % 4 == 0`
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `data` is a list containing [integer value of `data[0]`, an empty string], `n % 4 == 0`, `target_count` is `n // 4`, and `counts` is a dictionary with values where the count of each character ('A', 'C', 'G', 'T') is the number of times that character appears in the string `s`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `counts` is a dictionary where the count of each key (character) is less than or equal to `target_count`, `data` remains as `[integer value of `data[0]`, an empty string]`, `n` % 4 == 0, and `target_count` remains as `n // 4`. If the loop does not execute, the function does not return anything (i.e., it returns None implicitly). If the loop executes at least once, the function returns None.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `i` is `n`, `result` is a list where every occurrence of `'?'` is replaced by a character from `counts` such that the count of that character in `counts` is less than `target_count`, `counts` is a dictionary where the count of each character that replaced `'?'` is incremented by 1, `data` remains as `[integer value of `data[0]`, an empty string]`, `n` % 4 == 0, and `target_count` remains as `n // 4`.
    print(''.join(result))
#Overall this is what the function does:The function processes a genome string \(s\) and determines if replacing '?' characters with 'A', 'C', 'G', or 'T' results in each character having a count less than or equal to \(n/4\), where \(n\) is the length of the genome string. If any character count exceeds \(n/4\), the function prints '===' and returns. Otherwise, it replaces each '?' in the string with the character that has the smallest count and increments its count until all '?' are replaced. Finally, it prints the modified genome string.

