#State of the program right berfore the function call: The function takes no input parameters. The input consists of two lines: the first line contains an integer n representing the length of the genome, and the second line contains a string s of length n representing the coded genome, which consists of characters 'A', 'C', 'G', 'T' and '?'.
def func_1():
    input = sys.stdin.read

data = input().split()

n = int(data[0])

s = data[1]
    if (n % 4 != 0) :
        print('===')
        return
        #The program returns None
    #State of the program after the if block has been executed: n is 6, s is ACGT??? and (n % 4 == 0)
    target_count = n // 4

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
        
    #State of the program after the  for loop has been executed: n = 6, s = "ACGT???", counts = {'A': 1, 'C': 1, 'G': 1, 'T': 0}
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
        
    #State of the program after the  for loop has been executed: n = 6, s = "ACGT???", counts = {'A': 1, 'C': 1, 'G': 1, 'T': 0}
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
        
    #State of the program after the  for loop has been executed: `i` is 6, `n` is 6, `result` is ['A', 'C', 'G', 'T', 'A', 'C'], and `counts` is {'A': 2, 'C': 2, 'G': 1, 'T': 0}.
    print(''.join(result))
#Overall this is what the function does:The function `func_1` processes an input consisting of an integer `n` and a string `s` of length `n`, where `s` consists of characters 'A', 'C', 'G', 'T', and '?'. The function checks if `n` is divisible by 4 and if the count of 'A', 'C', 'G', and 'T' in `s` does not exceed `n/4`. If these conditions are met, it replaces the '?' characters in `s` with 'A', 'C', 'G', or 'T' such that each character appears exactly `n/4` times in the resulting string. If any of these conditions fail, the function prints '===' and returns. The function does not return any value.

