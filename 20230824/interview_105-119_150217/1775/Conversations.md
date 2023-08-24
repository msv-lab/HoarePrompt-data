# Question: 1775
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
An army of n droids is lined up in one row. Each droid is described by m integers a_1, a_2, ..., a_{m}, where a_{i} is the number of details of the i-th type in this droid's mechanism. R2-D2 wants to destroy the sequence of consecutive droids of maximum length. He has m weapons, the i-th weapon can affect all the droids in the army by destroying one detail of the i-th type (if the droid doesn't have details of this type, nothing happens to it). 

A droid is considered to be destroyed when all of its details are destroyed. R2-D2 can make at most k shots. How many shots from the weapon of what type should R2-D2 make to destroy the sequence of consecutive droids of maximum length?


-----Input-----

The first line contains three integers n, m, k (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 5, 0 ≤ k ≤ 10^9) — the number of droids, the number of detail types and the number of available shots, respectively.

Next n lines follow describing the droids. Each line contains m integers a_1, a_2, ..., a_{m} (0 ≤ a_{i} ≤ 10^8), where a_{i} is the number of details of the i-th type for the respective robot.


-----Output-----

Print m space-separated integers, where the i-th number is the number of shots from the weapon of the i-th type that the robot should make to destroy the subsequence of consecutive droids of the maximum length.

If there are multiple optimal solutions, print any of them. 

It is not necessary to make exactly k shots, the number of shots can be less.


-----Examples-----
Input
5 2 4
4 0
1 2
2 1
0 2
1 3

Output
2 2

Input
3 2 4
1 2
1 3
2 2

Output
1 3



-----Note-----

In the first test the second, third and fourth droids will be destroyed. 

In the second test the first and second droids will be destroyed.
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
n, m, k = map(int, input().split())

# Initialize a list to store the total number of each detail type in the army
total_details = [0] * m

# Initialize a list to store the number of shots for each detail type
shots = [0] * m

# Read the input droids and update the total_details list
for _ in range(n):
    droid_details = list(map(int, input().split()))
    for i in range(m):
        total_details[i] += droid_details[i]

# Find the maximum number of consecutive droids that can be destroyed
max_destroyed = min(k, n)

# Distribute the shots among the detail types as evenly as possible
for i in range(m):
    if max_destroyed == 0:
        break
    shots[i] = min(max_destroyed, total_details[i])
    max_destroyed -= shots[i]

# Print the number of shots for each detail type
print(*shots)
#@!CODE END!@#
````

---

## Feedback 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Code Reviewer who will give feedback on a buggy program. Imagine that you've been given a piece of code that is causing unexpected results. Your task is to scrutinize the code, identify the bugs, and provide constructive feedback. Discuss your findings in detail: what are the bugs? Where in the code do they occur? What impact do they have on the program's functionality?

### Requirement
You will NOT SUGGEST SOLUTION, because the user wants to fix the bugs themselves.
You will NOT SUGGEST SOLUTION, because the user wants to fix the bugs themselves.
You will NOT SUGGEST SOLUTION, because the user wants to fix the bugs themselves.
You will NOT generate FINAL CODE, because the user wants to fix the bugs themselves.
You will NOT generate FINAL CODE, because the user wants to fix the bugs themselves.
You will NOT generate FINAL CODE, because the user wants to fix the bugs themselves.
You will NOT FIX the CODE, because the user wants to fix the bugs themselves.
You will NOT FIX the CODE, because the user wants to fix the bugs themselves.
You will NOT FIX the CODE, because the user wants to fix the bugs themselves.
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
An army of n droids is lined up in one row. Each droid is described by m integers a_1, a_2, ..., a_{m}, where a_{i} is the number of details of the i-th type in this droid's mechanism. R2-D2 wants to destroy the sequence of consecutive droids of maximum length. He has m weapons, the i-th weapon can affect all the droids in the army by destroying one detail of the i-th type (if the droid doesn't have details of this type, nothing happens to it). 

A droid is considered to be destroyed when all of its details are destroyed. R2-D2 can make at most k shots. How many shots from the weapon of what type should R2-D2 make to destroy the sequence of consecutive droids of maximum length?


-----Input-----

The first line contains three integers n, m, k (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 5, 0 ≤ k ≤ 10^9) — the number of droids, the number of detail types and the number of available shots, respectively.

Next n lines follow describing the droids. Each line contains m integers a_1, a_2, ..., a_{m} (0 ≤ a_{i} ≤ 10^8), where a_{i} is the number of details of the i-th type for the respective robot.


-----Output-----

Print m space-separated integers, where the i-th number is the number of shots from the weapon of the i-th type that the robot should make to destroy the subsequence of consecutive droids of the maximum length.

If there are multiple optimal solutions, print any of them. 

It is not necessary to make exactly k shots, the number of shots can be less.


-----Examples-----
Input
5 2 4
4 0
1 2
2 1
0 2
1 3

Output
2 2

Input
3 2 4
1 2
1 3
2 2

Output
1 3



-----Note-----

In the first test the second, third and fourth droids will be destroyed. 

In the second test the first and second droids will be destroyed.
### INCORRECT PYTHON CODE
n, m, k = map(int, input().split())

# Initialize a list to store the total number of each detail type in the army
total_details = [0] * m

# Initialize a list to store the number of shots for each detail type
shots = [0] * m

# Read the input droids and update the total_details list
for _ in range(n):
    droid_details = list(map(int, input().split()))
    for i in range(m):
        total_details[i] += droid_details[i]

# Find the maximum number of consecutive droids that can be destroyed
max_destroyed = min(k, n)

# Distribute the shots among the detail types as evenly as possible
for i in range(m):
    if max_destroyed == 0:
        break
    shots[i] = min(max_destroyed, total_details[i])
    max_destroyed -= shots[i]

# Print the number of shots for each detail type
print(*shots)
The code above is wrong and contains bugs. Given input "5 2 4
4 0
1 2
2 1
0 2
1 3
" the output was "4 0
" but the expected output was "2 2
".
````

---

## Repair 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Programmer who fixes bugs in programs based on feedback given. Picture yourself receiving a detailed review of a piece of code you've written, which contains several bugs. The feedback points out exactly where the errors lie and suggests improvements. Your task is to carefully analyze the feedback, understand the identified issues and the proposed solutions. Then, you need to implement these fixes in the code. Finally, provide a Python code of your implementation.
## Expected Response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w == 2:
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
An army of n droids is lined up in one row. Each droid is described by m integers a_1, a_2, ..., a_{m}, where a_{i} is the number of details of the i-th type in this droid's mechanism. R2-D2 wants to destroy the sequence of consecutive droids of maximum length. He has m weapons, the i-th weapon can affect all the droids in the army by destroying one detail of the i-th type (if the droid doesn't have details of this type, nothing happens to it). 

A droid is considered to be destroyed when all of its details are destroyed. R2-D2 can make at most k shots. How many shots from the weapon of what type should R2-D2 make to destroy the sequence of consecutive droids of maximum length?


-----Input-----

The first line contains three integers n, m, k (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 5, 0 ≤ k ≤ 10^9) — the number of droids, the number of detail types and the number of available shots, respectively.

Next n lines follow describing the droids. Each line contains m integers a_1, a_2, ..., a_{m} (0 ≤ a_{i} ≤ 10^8), where a_{i} is the number of details of the i-th type for the respective robot.


-----Output-----

Print m space-separated integers, where the i-th number is the number of shots from the weapon of the i-th type that the robot should make to destroy the subsequence of consecutive droids of the maximum length.

If there are multiple optimal solutions, print any of them. 

It is not necessary to make exactly k shots, the number of shots can be less.


-----Examples-----
Input
5 2 4
4 0
1 2
2 1
0 2
1 3

Output
2 2

Input
3 2 4
1 2
1 3
2 2

Output
1 3



-----Note-----

In the first test the second, third and fourth droids will be destroyed. 

In the second test the first and second droids will be destroyed.
### Requirement
Use Standard Input Format (read inputs with `input()`, write results with `print()`)
### INCORRECT PYTHON CODE
#@!CODE START!@#
n, m, k = map(int, input().split())

# Initialize a list to store the total number of each detail type in the army
total_details = [0] * m

# Initialize a list to store the number of shots for each detail type
shots = [0] * m

# Read the input droids and update the total_details list
for _ in range(n):
    droid_details = list(map(int, input().split()))
    for i in range(m):
        total_details[i] += droid_details[i]

# Find the maximum number of consecutive droids that can be destroyed
max_destroyed = min(k, n)

# Distribute the shots among the detail types as evenly as possible
for i in range(m):
    if max_destroyed == 0:
        break
    shots[i] = min(max_destroyed, total_details[i])
    max_destroyed -= shots[i]

# Print the number of shots for each detail type
print(*shots)
#@!CODE END!@#
The code above is wrong and contains bugs. Given input "5 2 4
4 0
1 2
2 1
0 2
1 3
" the output was "4 0
" but the expected output was "2 2
".
The following is a detailed explanation of the issues: 
            ### BUGS IDENTIFIED

1. The code calculates the `max_destroyed` variable incorrectly. It should be the minimum between `k` and `n`, but the code assigns the value of `k` to `max_destroyed` without comparing it with `n`.

2. The code does not correctly distribute the shots among the detail types. The current approach assigns the minimum between `max_destroyed` and `total_details[i]` to `shots[i]`, which leads to incorrect results. The correct approach should be to evenly distribute the remaining shots among the detail types, while taking into account the maximum number of shots that can be made for each detail type.
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
### CORRECTED PYTHON CODE
#@!CODE START!@#
n, m, k = map(int, input().split())

# Initialize a list to store the total number of each detail type in the army
total_details = [0] * m

# Initialize a list to store the number of shots for each detail type
shots = [0] * m

# Read the input droids and update the total_details list
for _ in range(n):
    droid_details = list(map(int, input().split()))
    for i in range(m):
        total_details[i] += droid_details[i]

# Find the maximum number of consecutive droids that can be destroyed
max_destroyed = min(k, n)

# Calculate the maximum number of shots that can be made for each detail type
max_shots = min(k // max_destroyed, min(total_details))

# Distribute the shots among the detail types as evenly as possible
for i in range(m):
    if max_destroyed == 0:
        break
        
    # Calculate the number of shots for each detail type
    shots[i] = min(total_details[i], max_shots)
    max_destroyed -= shots[i]
    total_details[i] -= shots[i]

# Print the number of shots for each detail type
print(*shots)
#@!CODE END!@#
````

---

