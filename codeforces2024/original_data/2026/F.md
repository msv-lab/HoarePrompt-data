In the Bermart chain of stores, a variety of ice cream is sold. Each type of
ice cream has two parameters: price and tastiness.

Initially, there is one store numbered 1 , which sells nothing. You have to
process q queries of the following types:

  * 1~x — a new store opens, that sells the same types of ice cream as store x . It receives the minimum available positive index. The order of the types of ice cream in the new store is the same as in store x . 
  * 2~x~p~t — a type of ice cream with price p and tastiness t becomes available in store x . 
  * 3~x — a type of ice cream that was available the longest (appeared the earliest) in store x is removed. 
  * 4~x~p — for store x , find the maximum total tastiness of a subset of types of ice cream that are sold there, such that the total price does not exceed p (each type can be used in the subset no more than once). 

Input

The first line contains a single integer q (1 \le q \le 3 \cdot 10^4 ) — the
number of queries.

Each of the following q lines contains a query in the format described in the
statement:

  * 1~x ; 
  * 2~x~p~t (1 \le p, t \le 2000 ); 
  * 3~x ; 
  * 4~x~p (1 \le p \le 2000 ). 

Additional constraints on the input data:

  * x in each query does not exceed the current number of stores (that is, 1 plus the number of type 1 queries); 
  * query type 3 is not applied to a store that has no types of ice cream; 
  * there is at least one query of type 4 . 

Output

For each query of type 4 , output a single integer — for store x , find the
maximum total tastiness of a subset of types of ice cream that are sold there,
such that the total price does not exceed p (each type can be used in the
subset no more than once).

Example

Input

    12
    
    2 1 5 7
    
    2 1 3 4
    
    4 1 4
    
    4 1 8
    
    4 1 2
    
    1 1
    
    2 2 4 10
    
    4 1 9
    
    4 2 9
    
    3 1
    
    4 1 9
    
    4 2 9

Output

    4
    11
    0
    11
    17
    4
    17
    