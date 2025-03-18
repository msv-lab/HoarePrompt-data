import sys
from typing import List
 
input = sys.stdin.readline
 
def decode(encoded: str) -> str:
    mapping = {}
    decoded = []
 
    for char in encoded:
        if char in mapping:
            decoded.append(mapping[char])
        else:
            # Find the next unused letter from 'a' to 'z'
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) not in mapping.values():
                    mapping[chr(c)] = char
                    break
            decoded.append(chr(c))
 
    return "".join(decoded)
 
if __name__ == "__main__":
    num_cases = int(input().strip())
 
    for _ in range(num_cases):
        n = int(input().strip())
        encoded = input().strip()
        decoded = decode(encoded)
        print(decoded)