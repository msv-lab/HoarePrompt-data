def can_reach_all_junctions(n, m, horizontal, vertical):
    if (horizontal[0] == '>' and horizontal[-1] == '>' and vertical[0] == 'v' and vertical[-1] == 'v') or \
       (horizontal[0] == '<' and horizontal[-1] == '<' and vertical[0] == '^' and vertical[-1] == '^'):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    horizontal = data[2]
    vertical = data[3]
    
    print(can_reach_all_junctions(n, m, horizontal, vertical))
