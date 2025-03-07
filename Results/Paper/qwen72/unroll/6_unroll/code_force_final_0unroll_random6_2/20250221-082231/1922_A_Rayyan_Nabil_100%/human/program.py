def can_create_template(n, a, b, c):
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return "YES"
    return "NO"
 
def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = input().strip()
        b = input().strip()
        c = input().strip()
        results.append(can_create_template(n, a, b, c))
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()