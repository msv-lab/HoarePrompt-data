def min_segment_length(n, s):
    first_black = -1
    last_black = -1
    for i in range(n):
        if s[i] == 'B':
            if first_black == -1:
                first_black = i
            last_black = i
    return last_black - first_black + 1
 
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input().strip()
        results.append(min_segment_length(n, s))
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()
