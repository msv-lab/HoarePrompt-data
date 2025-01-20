#State of the program right berfore the function call: The function takes no input parameters. The input consists of two lines: the first line contains an integer n representing the length of the genome (4 ≤ n ≤ 255), and the second line contains a string s of length n representing the coded genome, which consists of characters 'A', 'C', 'G', 'T' and '?'.
def func_1():
    input = sys.stdin.read

data = input().split()

n = int(data[0])

s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #None
    #State of the program after the if block has been executed: n is an integer, s is a string consisting of characters 'A', 'C', 'G', 'T', and '?', and n is divisible by 4
    target_count = n // 4

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: n is still an integer divisible by 4, s remains the same string, target_count is still n // 4, and counts is a dictionary where each key 'A', 'C', 'G', 'T' has a value equal to the number of occurrences of that character in s.
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: Output State: `n` is an integer divisible by 4, `s` is a non-empty string containing at least one of 'A', 'C', 'G', 'T', `target_count` is `n // 4`, and `counts` is a dictionary with keys 'A', 'C', 'G', 'T'. The function returns `None` if none of the values in `counts` exceed `target_count`. If any value in `counts` exceeds `target_count`, the function returns `None` immediately upon encountering such a value.
    #
    #Explanation:
    #1. **Analyze the Code and Initial State**: The loop iterates over each character key ('A', 'C', 'G', 'T') in the `counts` dictionary. For each key, it checks if the count of that character exceeds `target_count`.
    #2. **Track Variable Changes**: 
    #   - `n` remains constant as it is only used to define `target_count` and is not modified within the loop.
    #   - `s` remains constant as it is not modified within the loop.
    #   - `target_count` remains constant as it is only defined once and is not modified within the loop.
    #   - `counts` may change its internal values during the iteration, but the keys remain the same.
    #3. **Summarize the Loop Behavior**: The loop will execute exactly once for each key in the `counts` dictionary. It prints '===' and returns `None` as soon as it finds a character count that exceeds `target_count`. If no character count exceeds `target_count`, the loop completes without returning anything, and the function implicitly returns `None`.
    #4. **Verify Relationships**: The conditions for the loop to execute are consistent with the described iterations and final output state. If any count exceeds `target_count`, the function returns `None` immediately, and if no count exceeds `target_count`, the function returns `None` after the loop completes.
    #
    #Therefore, the final output state after the loop has executed all its iterations is as described above.
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is an integer divisible by 4, `result` is a list of length `n` where each element is one of the characters 'A', 'C', 'G', 'T' and appears exactly `target_count` times, `counts` is a dictionary where the keys are 'A', 'C', 'G', 'T' and each key has a count of `target_count`, and `target_count` is `n // 4`.
    print(''.join(result))
#Overall this is what the function does:The function processes a genome represented by an integer \( n \) and a string \( s \) of length \( n \). The function checks if \( n \) is divisible by 4. If not, it prints '===' and returns. Otherwise, it counts the occurrences of 'A', 'C', 'G', and 'T' in \( s \). If any of these counts exceed \( n/4 \), it prints '===' and returns. If all counts are valid, it replaces the '?' characters in \( s \) with the most underrepresented nucleotide ('A', 'C', 'G', or 'T') until each nucleotide appears exactly \( n/4 \) times. Finally, it prints the modified string. If the function completes without printing '===', it implicitly returns `None`.

