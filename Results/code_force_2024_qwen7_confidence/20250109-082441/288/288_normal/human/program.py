def generate_words(n):
    words = []
    for i in range(n):
        binary = bin(i)[2:]  # Get binary representation without '0b'
        word = ''.join('O' if b == '1' else 'X' for b in binary)
        words.append(word)
    return words

def count_unique_substrings(s):
    substrings = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.add(s[i:j])
    return len(substrings)

def precompute_powers(words):
    n = len(words)
    power_dict = {}
    for i in range(n):
        for j in range(n):
            combined_spell = words[i] + words[j]
            power = count_unique_substrings(combined_spell)
            power_dict[power] = (i + 1, j + 1)  # Store 1-based indices
    return power_dict

def solve_arithmancy(n, queries):
    words = generate_words(n)
    power_dict = precompute_powers(words)
    results = []
    for power in queries:
        if power in power_dict:
            results.append(power_dict[power])
        else:
            results.append("NO")
    return results

# Example usage
n = 10  # Number of words to generate
queries = [7, 15, 11]  # Example powers to query
results = solve_arithmancy(n, queries)
for result in results:
    print(result)