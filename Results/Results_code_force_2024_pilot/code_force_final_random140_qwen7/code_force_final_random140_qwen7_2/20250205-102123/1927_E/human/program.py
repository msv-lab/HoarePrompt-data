# https://codeforces.com/problemset/problem/1927/E
 
def case():
    n,k = map(int,input().split(" "))
 
    permutation = [0] * n
 
    bottom_v = 1
    top_v = n
 
    idx = 0
    while idx < k:
 
        multiples_of_k_plus_idx = idx
        while multiples_of_k_plus_idx < len(permutation):
 
            if idx % 2 == 0:
                permutation[multiples_of_k_plus_idx] = bottom_v
                bottom_v += 1
            else:
                permutation[multiples_of_k_plus_idx] = top_v
                top_v -= 1
 
            multiples_of_k_plus_idx += k
 
        idx += 1
 
    result = " ".join([str(v) for v in permutation])
    print(result)
 
 
def main():
    t = int(input())
    while t > 0:
        case()
        t -= 1
 
if __name__ == "__main__":
    main()