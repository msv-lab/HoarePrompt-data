from itertools import permutations

def find_max_permutation(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Generate all permutations of the digits of a
    perm = permutations(a_str)
    
    max_num = -1
    for p in perm:
        num_str = ''.join(p)
        if num_str[0] != '0':  # Ensure no leading zero
            num = int(num_str)
            if num <= b:
                max_num = max(max_num, num)
    
    return max_num

a = int(input())
b = int(input())

print(find_max_permutation(a, b))
