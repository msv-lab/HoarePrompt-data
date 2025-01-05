import sys

lines = []
for i in range(3):
    lines.append(sys.stdin.readline())
    
if(lines[0][0] == "X" and lines[2][2] != "X") or (lines[0][1] == "X" and lines[2][1] != "X") or(lines[0][2] == "X" and lines[2][0] != "X") or (lines[1][0] == "X" and lines[1][2] != "X") or (lines[1][2] == "X" and lines[1][0] != "X"):
    print("NO")
else:
    print("YES")