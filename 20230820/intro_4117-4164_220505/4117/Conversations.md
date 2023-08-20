# Question: 4117
## Generation 1
### Conversations

---

**role**: 
system

---

**content**: 
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#

---

**role**: 
user

---

**content**: 
### QUESTION
We have sticks numbered 1, \cdots, N. The length of Stick i (1 \leq i \leq N) is L_i.
In how many ways can we choose three of the sticks with different lengths that can form a triangle?
That is, find the number of triples of integers (i, j, k) (1 \leq i < j < k \leq N) that satisfy both of the following conditions:
 - L_i, L_j, and L_k are all different.
 - There exists a triangle whose sides have lengths L_i, L_j, and L_k.

-----Constraints-----
 - 1 \leq N \leq 100
 - 1 \leq L_i \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
L_1 L_2 \cdots L_N

-----Output-----
Print the number of ways to choose three of the sticks with different lengths that can form a triangle.

-----Sample Input-----
5
4 4 9 7 5

-----Sample Output-----
5

The following five triples (i, j, k) satisfy the conditions: (1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 4, 5), and (3, 4, 5).
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS

---

**role**: 
assistant

---

**content**: 
#@!CODE START!@#
def count_triangles(N, lengths):
    count = 0
    
    # Iterate over all possible combinations of three sticks
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # Check if the lengths of the sticks are all different and can form a triangle
                if lengths[i] != lengths[j] and lengths[j] != lengths[k] and lengths[k] != lengths[i]:
                    if lengths[i] + lengths[j] > lengths[k] and lengths[j] + lengths[k] > lengths[i] and lengths[k] + lengths[i] > lengths[j]:
                        count += 1
    
    return count

# Read the input
N = int(input())
lengths = list(map(int, input().split()))

# Call the function and print the result
result = count_triangles(N, lengths)
print(result)
#@!CODE END!@#

---

## Generation 2
### Conversations

---

**role**: 
system

---

**content**: 
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#

---

**role**: 
user

---

**content**: 
### QUESTION
We have sticks numbered 1, \cdots, N. The length of Stick i (1 \leq i \leq N) is L_i.
In how many ways can we choose three of the sticks with different lengths that can form a triangle?
That is, find the number of triples of integers (i, j, k) (1 \leq i < j < k \leq N) that satisfy both of the following conditions:
 - L_i, L_j, and L_k are all different.
 - There exists a triangle whose sides have lengths L_i, L_j, and L_k.

-----Constraints-----
 - 1 \leq N \leq 100
 - 1 \leq L_i \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
L_1 L_2 \cdots L_N

-----Output-----
Print the number of ways to choose three of the sticks with different lengths that can form a triangle.

-----Sample Input-----
5
4 4 9 7 5

-----Sample Output-----
5

The following five triples (i, j, k) satisfy the conditions: (1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 4, 5), and (3, 4, 5).
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS

---

**role**: 
assistant

---

**content**: 
#@!CODE START!@#
N = int(input())
sticks = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a, b, c = sticks[i], sticks[j], sticks[k]
            if a != b and b != c and a != c and a+b > c and b+c > a and a+c > b:
                count += 1

print(count)
#@!CODE END!@#

---

