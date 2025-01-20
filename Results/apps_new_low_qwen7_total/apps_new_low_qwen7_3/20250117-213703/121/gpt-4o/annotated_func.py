#State of the program right berfore the function call: The function takes no input parameters. However, the input is provided through standard input, where the first line contains an integer n (4 ≤ n ≤ 255) representing the length of the genome, and the second line contains a string s of length n consisting of characters 'A', 'C', 'G', 'T', and '?' representing the coded genome.
def func_1():
    input = sys.stdin.read

data = input().split()

n = int(data[0])

s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program does not return any value
    #State of the program after the if block has been executed: `n` is an integer between 4 and 255, `s` is a string of length `n` consisting of characters 'A', 'C', 'G', 'T', and '?', and `n % 4 == 0`
    target_count = n // 4

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255, `s` is a string of length `n` that contains only the characters 'A', 'C', 'G', 'T', and possibly '?', `counts` is a dictionary with keys `'A'`, `'C'`, `'G'`, and `'T'` where the count of each character (either 'A', 'C', 'G', or 'T') in `s` is incremented by 1, and `target_count` is `n // 4`.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255, `s` is a string of length `n` containing only the characters 'A', 'C', 'G', 'T', and possibly '?', `counts` is a dictionary with keys `'A'`, `'C'`, `'G'`, and `'T'`, and `target_count` is `n // 4`. The loop continues iterating through the keys in the `counts` dictionary in lexicographical order until it finds a key `char` such that `counts[char] > target_count`. If no such key is found, the function does not return and `counts` remains unchanged. If such a key is found, the function prints '===' and returns None.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `n` is an integer between 4 and 255, `s` is a string of length `n` containing only the characters 'A', 'C', 'G', 'T', and possibly '?', `counts` is a dictionary with keys `'A'`, `'C'`, `'G'`, and `'T'`, and each key has a count of exactly `n // 4` or `n // 4 + 1`. The `result` array is a list of length `n` where each index contains one of 'A', 'C', 'G', or 'T', and every nucleotide type ('A', 'C', 'G', and 'T') appears exactly `n // 4` or `n // 4 + 1` times in `result`. If `result[i]` is not '?', the postcondition remains unchanged, and `i` is incremented by 1. The loop terminates when the count of all nucleotides in `counts` reaches their target count (`n // 4 + 1`), ensuring that each nucleotide type appears the required number of times in `result`.
    print(''.join(result))
#Overall this is what the function does:The function reads an integer \( n \) and a string \( s \) from standard input, where \( n \) represents the length of the genome and \( s \) consists of characters 'A', 'C', 'G', 'T', and '?'. The function checks if \( n \) is divisible by 4, and if not, it prints '===' and exits. If \( n \) is divisible by 4, it calculates the target count of each nucleotide as \( n // 4 \). It then counts the occurrences of each nucleotide in \( s \). If any nucleotide's count exceeds the target count, it prints '===' and exits. If not, it replaces all '?' characters in \( s \) with the nucleotides in lexicographical order ('A', 'C', 'G', 'T') such that each nucleotide appears exactly the target count or \( n // 4 + 1 \) times. Finally, it prints the modified string. The function does not return any value.

