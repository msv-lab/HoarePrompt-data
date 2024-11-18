def find_smallest_possible_n(s, sub):
    n_len = len(s) - len(sub)

    def is_valid_number(num_str, sub):
        return sub in num_str and len(num_str) == n_len

    def generate_possible_numbers(chars, sub):
        from itertools import permutations
        for perm in permutations(chars):
            candidate = ''.join(perm)
            if is_valid_number(candidate, sub):
                yield candidate

    from collections import Counter
    s_counter = Counter(s)
    sub_counter = Counter(sub)

    for char in sub_counter:
        s_counter[char] -= sub_counter[char]

    remaining_chars = ''.join([char * s_counter[char] for char in s_counter])

    possible_numbers = generate_possible_numbers(remaining_chars, sub)
    smallest_number = min(possible_numbers, key=int)

    return smallest_number

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    s = data[0]
    sub = data[1]
    
    result = find_smallest_possible_n(s, sub)
    print(result)
