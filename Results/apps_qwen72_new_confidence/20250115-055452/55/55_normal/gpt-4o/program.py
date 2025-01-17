def can_balance(w, m):
    while m != 0:
        if m % w <= 1:
            m //= w
        elif m % w == w - 1:
            m = (m // w) + 1
        else:
            return "NO"
    return "YES"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    w = int(data[0])
    m = int(data[1])
    print(can_balance(w, m))
