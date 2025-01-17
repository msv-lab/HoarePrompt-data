There are 2 queues of patients at the doors of two doctors. The first doctor
sees patients in the usual order of the queue — whoever arrived first will be
seen first. The second doctor does the opposite — he sees those who arrived
last first. Thus, there is a queue for the first doctor and a stack for the
second doctor. A patient can be in both the queue and the stack. Each patient
is characterized by the time their visit to the doctor will take (the time is
the same for both doctors).

When the appointments begin, the doctors will see patients in the order of the
queue and stack, respectively. As soon as a doctor finishes with one patient,
he will call the next one.

But there is one problem: if a patient is in both the queue and the stack, and
he is called to one doctor first and then to the other, while he has not yet
finished with the first one, confusion will arise. It is allowed for a patient
to go to the second doctor at the exact moment he finishes with the first
doctor.

The current configuration of the queue and stack is called good if the doctors
can see all the patients without any confusion arising.

Initially, both the queue and the stack are empty. There are three types of
queries:

  1. add patient x to the queue; 
  2. add patient x to the stack; 
  3. patient x , who was in the queue, realizes he is in the wrong place and moves to the stack; however, he moves to the position in the stack as if he had entered the stack at the moment of the query when he entered the queue. 

It is guaranteed that after each query, each patient is no more than once in
the queue and no more than once in the stack.

After each query, you need to determine if the current configuration is good.

Input

The first line contains a single integer n (1 \le n \le 10^5 ) — the number of
requests.

The second line contains n integers a_1, a_2, \dots, a_n (1 \le a_i \le 10^9 )
— for each patient, the time their visit to the doctor will take.

Each of the following n lines contains two integers t and x (1 \le t \le 3 ; 1
\le x \le n ) — the type of query and the patient's index. It is guaranteed
that:

  * if the query is of type 1 , then patient x is not in the queue yet; 
  * if the query is of type 2 , then patient x is not in the stack yet; 
  * if the query is of type 3 , then patient x is in the queue already and not in the stack yet. 

Output

After each query, print "YES", if the current configuration is good, and "NO"
otherwise.

Examples

Input

    3
    
    10 15 4
    
    1 1
    
    2 1
    
    2 2

Output

    YES
    NO
    YES
    
Input

    7
    
    2 5 1 5 5 4 8
    
    1 1
    
    2 5
    
    1 2
    
    2 3
    
    3 2
    
    1 2
    
    3 1

Output

    YES
    YES
    YES
    YES
    YES
    NO
    NO
    
Note

In the first test, there are the following configurations:

  1. queue: [1] ; stack: [] ; patient 1 is seen by the first doctor for 10 minutes, starting at minute 0 . 
  2. queue: [1] ; stack: [1] ; patient 1 is seen by the first doctor during [0; 10) and by the second during [0; 10) . Since patient 1 must be at both doctors at the same time, the answer is "NO". 
  3. queue: [1] ; stack: [1, 2] ; patient 1 is seen by the first doctor during [0; 10) , and by the second during [15; 25) ; patient 2 is seen by the second doctor during [0, 15) . Now patient 1 can make it to the second doctor after seeing the first. 

In the second test, the configuration after query 4 is as follows:

  * queue: [1, 2] ; 
  * stack: [5, 3] ; 
  * patient 1 : first doctor [0, 2) , second doctor is not seeing him; 
  * patient 2 : first doctor [2, 7) , second doctor is not seeing him; 
  * patient 3 : first doctor is not seeing him, second doctor [0, 1) ; 
  * patient 5 : first doctor is not seeing him, second doctor [1, 6) . 

After request 5 , the next configuration is:

  * queue: [1] ; 
  * stack: [5, 2, 3] ; 
  * patient 1 : first doctor [0, 2) , second doctor is not seeing him; 
  * patient 2 : first doctor is not seeing him, second doctor [1, 6) ; 
  * patient 3 : first doctor is not seeing him, second doctor [0, 1) ; 
  * patient 5 : first doctor is not seeing him, second doctor [6, 11) . 

After request 6 , the next configuration is:

  * queue: [1, 2] ; 
  * stack: [5, 2, 3] ; 
  * patient 1 : first doctor [0, 2) , second doctor is not seeing him; 
  * patient 2 : first doctor [2, 7) , second doctor [1, 6) ; 
  * patient 3 : first doctor is not seeing him, second doctor [0, 1) ; 
  * patient 5 : first doctor is not seeing him, second doctor [6, 11) . 

Patient 2 must be at both doctors at the same time.

After request 7 , the next configuration is:

  * queue: [2] ; 
  * stack: [1, 5, 2, 3] ; 
  * patient 1 : first doctor is not seeing him, second doctor [11, 13) ; 
  * patient 2 : first doctor [0, 5) , second doctor [1, 6) ; 
  * patient 3 : first doctor is not seeing him, second doctor [0, 1) ; 
  * patient 5 : first doctor is not seeing him, second doctor [6, 11) . 

Patient 2 must be at both doctors at the same time.
