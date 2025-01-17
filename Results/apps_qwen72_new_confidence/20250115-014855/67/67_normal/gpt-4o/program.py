from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

def count_ties(t, w, b):
    if w > b:
        w, b = b, w
    
    lcm_wb = lcm(w, b)
    full_cycles = t // lcm_wb
    
    common_lengths = min(w, b) - 1
    tie_count = full_cycles * common_lengths
    
    remainder = t % lcm_wb
    
    tie_count += min(common_lengths, remainder)
    
    return tie_count

def irreducible_fraction(p, q):
    g = gcd(p, q)
    return f"{p // g}/{q // g}"

def main():
    import sys
    input = sys.stdin.read
    t, w, b = map(int, input().split())
    
    if w == b:
        print("1/1")
        return
    
    num_ties = count_ties(t, w, b)
    
    print(irreducible_fraction(num_ties, t))

if __name__ == "__main__":
    main()
