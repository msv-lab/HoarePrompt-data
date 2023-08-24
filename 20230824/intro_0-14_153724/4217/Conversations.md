# Question: 4217
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
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
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
Katsusando loves omelette rice.
Besides, he loves crème brûlée, tenderloin steak and so on, and believes that these foods are all loved by everyone.
To prove that hypothesis, he conducted a survey on M kinds of foods and asked N people whether they like these foods or not.
The i-th person answered that he/she only likes the A_{i1}-th, A_{i2}-th, ..., A_{iK_i}-th food.
Find the number of the foods liked by all the N people.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N, M \leq 30
 - 1 \leq K_i \leq M
 - 1 \leq A_{ij} \leq M
 - For each i (1 \leq i \leq N), A_{i1}, A_{i2}, ..., A_{iK_i} are distinct.

-----Constraints-----
Input is given from Standard Input in the following format:
N M
K_1 A_{11} A_{12} ... A_{1K_1}
K_2 A_{21} A_{22} ... A_{2K_2}
:
K_N A_{N1} A_{N2} ... A_{NK_N}

-----Output-----
Print the number of the foods liked by all the N people.

-----Sample Input-----
3 4
2 1 3
3 1 2 3
2 3 2

-----Sample Output-----
1

As only the third food is liked by all the three people, 1 should be printed.
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#

# Read N and M from input
N, M = map(int, input().split())

# Create a list to store the count of each food
food_count = [0] * M

# Iterate through each person
for _ in range(N):
    # Read the list of foods liked by the person
    person = list(map(int, input().split()))[1:]

    # Increment the count for each food liked by the person
    for food in person:
        food_count[food - 1] += 1

# Count the number of foods liked by all the N people
liked_by_all = sum(1 for count in food_count if count == N)

# Print the result
print(liked_by_all)

#@!CODE END!@#
````

---

