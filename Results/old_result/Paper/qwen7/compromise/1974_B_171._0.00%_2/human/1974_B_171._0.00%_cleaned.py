input = sys.stdin.readline

def func_1(encoded: str) -> str:
    mapping = {}
    decoded = []
    for char in encoded:
        if char in mapping:
            decoded.append(mapping[char])
        else:
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) not in mapping.values():
                    mapping[chr(c)] = char
                    break
            decoded.append(chr(c))
    return ''.join(decoded)
if __name__ == '__main__':
    num_cases = int(input().strip())
    for _ in range(num_cases):
        n = int(input().strip())
        encoded = input().strip()
        decoded = func_1(encoded)
        print(decoded)