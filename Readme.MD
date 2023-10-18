# Warehouse Inventory Optimization Problem Statement:

You are tasked with optimizing a complex warehouse's inventory selection process:

- The warehouse has limited storage space, and there is a list of items available for storage, each with different sizes
and values. 
- Your goal is to create an advanced program that not only maximizes the total value of the
stored items while respecting space constraints but also considers additional factors like item
priorities and item dependencies.

## Requirements:

1. Input Data:
    You will receive the following input data:
    The available warehouse space, denoted as total_space (an integer representing available square
    footage). A list of items, where each item is represented as an object with the following properties:
    - name: A string representing the item's name.
    - size: An integer representing the size of the item in square footage.
    - value: An integer representing the value of the item (the higher the value, the better).
    - priority: An integer representing the priority of the item (a lower number indicates higher priority).
    - dependencies: A list of item names that this item depends on. If an item depends on others, it cannot
    be selected until its dependencies are chosen.

2. Algorithm Development:
    Develop an advanced optimization algorithm that:
    - Selects a combination of items that maximize the total value while ensuring the total size of the selected items does not exceed the available warehouse space.
    - Takes into account the priority of items, giving higher priority items precedence in selection.
    - Handles item dependencies. Items with dependencies cannot be selected until their dependencies
    have been chosen.
    - Algorithm should be highly efficient, scalable, and capable of handling
    complex dependencies.

3. Output:
    Implement the algorithm to display the selected combination of items, their total value, and any
    additional details that provide insights into the optimization process.
    
4. Documentation and Efficiency:
    Provide extensive comments and documentation in your code to explain your optimization
    algorithm's logic and how it ensures space constraints, priorities, and dependencies are met.
    Emphasize the efficiency and scalability of your solution, as the warehouse may have a large number
    of items and complex dependencies.

5. Constraints:
    The list of items may contain various items, each with different sizes, values, priorities, and
    dependencies. The available warehouse space (total_space) is an integer representing square footage and is limited.
    The optimization algorithm should efficiently handle complex scenarios, where items have
    dependencies and priorities, making it challenging to solve with a simple approach.

## Solution proposition

1. Assumptions:<br/>
   Since there is no definition of uniqueness of an item, I will assume that name is unqiue and it is identifier for individual item. Also name appears as dependency reference.
   
   No duplicates will be allowed, input with duplicates will be treated as invalid and error will be raised.
   
   Since dependencies are part of problem constraint, check for dependency cycles will be performed, dependency path has to be DAG (directed acyclic graph).If cycle is found (chicken and egg problem) input will be treated as invalid and error will be raised. Hypothetically one can find, remove cycles and find solution without those items, but, this is not implemented. Dependency cycles will be treated as invalid input.
2. Algorithm:
   - Check for duplicates and cycles, raise error if found
   - Make topological sort of items (via dependency graph), this can help to skip  unnessery steps later.
   - Process sorted items from left to right while processing remember items taken, for current item if all dependencies are not taken skip it (in toplogically sorted items dependenices are before dependents). Interesting side effect is with a lot of dependencies a lot work can be skipped, worst case appears when thera are no dependences then this becomes pure exponenital runing time algorithm.
   - Do backtracking search of solutions (PCKP variation). 
   - If there is one solution take that, if there are multiple solutions,take one one with highest priority set values.
   
3. This solution should find optimal solution with highest priority following precedence constraint.
4. Performance, since this is backtracking solution, and on every of N items there is option to take or not to take item this adds up to exponential runing time. In case of inputs with bigger N, this will have great processing time. There are a bit more efficient algorithms for this kind of problems, but for that it takes more time and I expect to be payed for that, freebie code takes you only up to here. Time based performance issues can be seen in test case #8, starts with 30+ number of items.
5. Order of importance of contraints:
   - Precedence, this prevents items to be taken, altough they might lead to optimal solution before dependecies are taken too.
   - Optimization for max value while staying in space capacity. Typical bounded knapsack problem, precedence constraint makes i a bit harder variation, one can't just choose items and solve this with 2D dynamic programming.
   - Priority, lowest importance (by the way, what this means is not clear from problem statement).
   In this solution this is used only when optimal solutions are found to pick one with best priority values combination.
6. Tests:
   - there are 8 test cases

## How to run
1. Run python code from terminal with 2 parameters, first is input json file, second is output.json file,for example:
    ```
    python Python/main.py input.json output.json
    ```
2. Run tests from terminal:
    ```
    python Python/Test.py
    ```

## Futher notice
I assume that some details I might get incorrectly and there is more then one opportunity to improve solution in preformance and correctness. This can be further develpoed with more time and effort. 