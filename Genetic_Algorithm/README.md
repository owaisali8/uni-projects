# 8-Queens Problem solved using Genetic Algorithm

Implementation of a program in python to solve the 8 Queens Problem using a genetic algorithm. The aim of the N-Queens Problem is to place N queens on an N x N board, in a way so that none of them can attack the other (means when any queen moves in directions vertical, horizontal and diagonal no other queen found in the path)

These are the following steps implemented:

Step 1: Initialize the population randomly.

Step 2: Compute the **_fitness_** of each individual in the population.

Step 3: Select parents using a **_parent selection procedure_**.

Step 4: Create offspring by **_crossover_** and **_mutation_** operators.

Step 5: Compute the **_fitness_** of the new offspring.

Step 6: Select members of population to die using a **_Survival selection procedure_**.

Step 7: Go to Step 2 until termination criteria are met.

- This process is repeated until an individual with required fitness level is found.
- If no such individual is found, then the process is repeated further until the overall fitness of the population or any of its individuals gets very close to the required fitness level. 
- An upper limit on the number of iterations is usually put to end the process in finite time.

The code commented out is either used for debugging or that part of code yields no result.
As we are initializing our population randomly, the result will be different.

### Screenshot:
![OutputScreenshot1.PNG](https://github.com/owaisali8/uni-projects/blob/main/Genetic_Algorithm/OutputScreenshot1.PNG?raw=true)

![OutputScreenshot2.PNG](https://github.com/owaisali8/uni-projects/blob/main/Genetic_Algorithm/OutputScreenshot2.PNG?raw=true)
