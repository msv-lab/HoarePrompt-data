def query(a, b, c, d):
    print(f"? {a} {b} {c} {d}")
    sys.stdout.flush()
    return input().strip()

def answer(i, j):
    print(f"! {i} {j}")
    sys.stdout.flush()

import sys

def solve():
    import random
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        
        # We will use a heuristic approach to maximize the XOR
        # We will randomly select pairs and compare their OR results to get hints about their bits
        
        # We will use a dictionary to store the best candidate for each bit position
        best_by_bit = {}
        
        # We will perform a number of random queries to gather information
        num_queries = min(3 * n, 1000)  # Limit queries to 3n or 1000, whichever is smaller
        
        for _ in range(num_queries):
            indices = random.sample(range(n), 4)
            a, b, c, d = indices
            result = query(a, b, c, d)
            
            # We interpret the result to decide which pair might have higher bits set
            if result == '>':
                # (p_a | p_b) > (p_c | p_d)
                # This suggests p_a or p_b might have higher bits set
                for idx in (a, b):
                    for bit in range(20):  # Assuming n <= 10^6, we consider up to 20 bits
                        if (1 << bit) & idx:
                            if bit not in best_by_bit or random.random() < 0.5:
                                best_by_bit[bit] = idx
            elif result == '<':
                # (p_a | p_b) < (p_c | p_d)
                # This suggests p_c or p_d might have higher bits set
                for idx in (c, d):
                    for bit in range(20):
                        if (1 << bit) & idx:
                            if bit not in best_by_bit or random.random() < 0.5:
                                best_by_bit[bit] = idx
        
        # After collecting some data, we try to find the best pair
        # We will use the indices with the highest bit set as candidates
        if best_by_bit:
            sorted_bits = sorted(best_by_bit.keys(), reverse=True)
            best_indices = [best_by_bit[bit] for bit in sorted_bits[:2]]
            if len(best_indices) < 2:
                best_indices.append(random.choice(list(set(range(n)) - set(best_indices))))
            answer(best_indices[0], best_indices[1])
        else:
            # If no information was useful, fallback to a random guess
            i, j = random.sample(range(n), 2)
            answer(i, j)