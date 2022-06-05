#  Hypothetical Architecture
## Introduction
![Introduction to MARIE - MARIE-js/MARIE.js Wiki](https://marie-js.github.io/MARIE.js/images/diagrams/MARIE.png)

We have implemented the MARIE architecture in its simplest form. As a minimum, the ISA has the following instructions:

- LOAD: Loads data from MM(Main Memory) to AC
- STORE: Stores data from AC to MM
- MUL: Mul AC with data from MM (Stores result in AC)
- ADD: Adds AC with data from MM(Stores result in AC)
- INPUT: Loads data from InREG to AC
- END: Terminates the program

It is implemented on Logisim first using an 8 bit word then extending it to 16 bit

## Components In Logisim
1. RAM/ROM 
2. Wires 
3. Registers 
4. Clock 
5. Counters 
6. Multiplexer/Demultiplexer 
7. Adder/Multiplier
8. Input/Output Pins

## Procedure
1. First we selected 8 bits for our word in which 4 bits were opcode and 4 bits were operand. Later we extended it to 16 bits in which the last 12 bits were operand. 
2. We first added Registers and RAM components, tweaked them and then created a connection between them. 
3. Clock, Counter, RAM and Registers are important parts in our design as if one of them fails to function properly the rest of the components fail too.
4. We realized that the clock should be properly synced between RAM and Registers. 
5. One of the problems that we were facing was to actually implement the one Main Memory module where the code and contents will reside. Our main initial thought process was that PC and MAR would be able to access our contents from one Memory module, but the problem was they both were not able to access simultaneously, and this was increasing the complexity of our architecture.
6. Instead we opted to use two memory modules, CMB(Code Memory Buffer) and MM(Main Memory). 
7. This allowed us to first enter our code into CMB and then execute the code automatically without any interference from MAR. This also reduced the complexity of the fetch-decode-execute cycle. 
8. IR register holds our current instruction fetched from CMB and then sends the 2 instruction to be decoded. 
9. Instruction is splitted and opcode is decoded using a demultiplexer which enables the required pin necessary. 
10. Operand is sent to MAR. It then loads the content of the address to MBR if necessary. 
11. MBR loads the data into AC if LOAD instruction is called. 
12. Loading data into AC was simple to do from MBR, but storing data back to memory using MBR was increasing the complexity of our design. Instead we opted to use MBR IN, which is another register used to store data from AC to MM 
13. ALU is working as intended with a Multiplier and Adder.

## How to Use?
1. Demo 1 (8-bit):
- Load ‘Code1Image’ into CMB
- Give any input to IN REG
- Change pin to 1 on W/R
- Simulate the clock, code will start working
2. Demo 2 (8-bit):
- Load ‘Code2Image’ into CMB
- Load ‘Main2Image’ into MM
- Change pin to 1 on W/R
- Simulate the clock, code will start working

## Conclusion
We first implemented our design in 8 bits then upgraded it into 16 bits. This helped us to design an architecture close to MARIE step by step. We can further add more instructions and components into our design, if it is required.

### Screenshot
![8-bit Screenshot.PNG](https://github.com/owaisali8/uni-projects/blob/main/CAAL_Hypothetical_Architecture/8-bit%20Screenshot.PNG?raw=true)
