import numpy as np
import random


def generate_population(pop_list):
    while(True):
        r = ''
        for i in range(8):
            r += str(random.randint(1,8))
        r = int(r)
        if (r not in pop_list):
            return [r]


def init_population(num = 4):
    population = []
    for i in range(num):
        population.append(generate_population(population))
    return population


def init_board():
    board = np.zeros((8,8))
    return board


def set_board(board,ind):
    ind  = [int(x) for x in str(ind)]
    for i in range(len(ind)):
        board[ind[i]-1][i] = 1
    pass


def compute_fitness(pop):
    for k in range(len(pop)):
        num = pop[k][0] #take indiviual 
        fitness = 8
        num = [int(x) for x in str(num)]
        num_bool = [False] *8
        #print(num)
        for i in range(8): #check right squares
            for j in range(i+1,8):
                if (num[i] == num[j] ) and (~num_bool[i]):
                    num_bool[i] = True
                    num_bool[j] = True
                    break
                    
        for i in range(7,-1,-1): #check left squares
            for j in range(i-1,-1,-1):
                if (num[i] == num[j]) and (~num_bool[i]):
                    num_bool[i] = True
                    num_bool[j] = True
                    break
                    
        #check upper right diagonal
        for i in range(8):
            if(num_bool[i]):
                continue
            n = num[i]
            for j in range(i+1,8):
                n -= 1
                if(n == 0):
                    break
                if(n == num[j]):
                    num_bool[i] = True
                    num_bool[j] = True
                    break
                    
        #check lower right diagonal
        for i in range(8):
            if(num_bool[i]):
                continue
            n = num[i]
            for j in range(i+1,8):
                n += 1
                if(n == 9):
                    break
                if(n == num[j]):
                    num_bool[i] = True
                    num_bool[j] = True
                    break
            
        #check upper left diagonal
        for i in range(7,-1,-1):
            if(num_bool[i]):
                continue
            n = num[i]
            for j in range(i-1,-1,-1):
                n -= 1
                if(n == 0):
                    break
                if(n == num[j]):
                    num_bool[i] = True
                    num_bool[j] = True
                    break
                    
        #check lower left diagonal
        for i in range(7,-1,-1):
            if(num_bool[i]):
                continue
            n = num[i]
            for j in range(i-1,-1,-1):
                n += 1
                if(n == 9):
                    break
                if(n == num[j]):
                    num_bool[i] = True
                    num_bool[j] = True
                    break
        
        #print(num_bool)
        pop[k].append(fitness-sum(num_bool))
    
    
def takeSecond(elem):
    return elem[1]
    
    
def parent_selection(pop):
    parents = sorted(pop,reverse=True, key = takeSecond)
    #print(parents)
    return parents
   

def crossover(parents):
    r = random.randint(0,len(parents)-1)
    r1 = random.randint(0,len(parents)-1)
    while(r1 == r):
        r = random.randint(0,len(parents)-1)
        r1 = random.randint(0,len(parents)-1)
    parent1, parent2 = parents[0][0],parents[1][0]
    
    child1 = [int(str(parent1)[0:4]+str(parent2)[4:8])]
    child2 = [int(str(parent2)[0:4]+str(parent1)[4:8])]
    return[child1,child2]

'''
def mutation(parents): #bitwise mutation
    parent1, parent2 = parents[2][0],parents[-1][0]
    #print(parent1)
    parent1, parent2 = format(parent1,'b'), format(parent2,'b')
    while(True):
        parent1, parent2 = parents[2][0],parents[3][0]
        #print(parent1)
        parent1, parent2 = format(parent1,'b'), format(parent2,'b')
        r = random.randint(1,len(parent1)-2)
        r2 = random.randint(1,len(parent2)-2)
        
        if(parent1[r] == '0'):
            l = list(parent1)
            l[r] = '1'
            parent1 = ''.join(l)
        else:
            l = list(parent1)
            l[r] = '0'
            parent1 = ''.join(l)
            
        if(parent2[r2] == '0'):
            l = list(parent2)
            l[r2] = '1'
            parent2 = ''.join(l)
        else:
            l = list(parent2)
            l[r2] = '0'
            parent2 = ''.join(l)
            
        parent1, parent2 = int(parent1,2),int(parent2,2)
        if('0' in str(parent1) and '0' in str(parent2)):
            pass
        else:
            break
    return [[parent1],[parent2]]

def mutation(parents): # swap mutation
    r = random.randint(0,len(parents)-1)
    r1 = random.randint(0,len(parents)-1)
    while(r1 == r):
        r = random.randint(0,len(parents)-1)
        r1 = random.randint(0,len(parents)-1)
    parent1, parent2 = parents[0][0],parents[1][0]
    #print(parent1)
    r = random.randint(0,7)
    r1 = random.randint(0,7)
    while(r1 == r):
        r = random.randint(0,7)
        r1 = random.randint(0,7)
    parent1 = [int(x) for x in str(parent1)]
    parent2 = [int(x) for x in str(parent2)]
    parent1[r:r1], parent1[r1:r] = parent1[r1:r], parent1[r:r1]
    parent2[r:r1], parent2[r1:r] = parent2[r1:r], parent2[r:r1]
    
    parent1 = [str(i) for i in parent1]
    parent2 = [str(i) for i in parent2]
    
    child1 = int("".join(parent1))
    child2 = int("".join(parent2))
    
    #print(child1)
    
    return [[child1],[child2]]
'''
    
def mutation(parents): #bitwise mutation 2
    parent1, parent2 = parents[0][0],parents[1][0]
    r = random.randint(1,8)
    r1 = random.randint(1,8)
    while(r1 == r):
        r = random.randint(1,8)
        r1 = random.randint(1,8)
    parent1 = [int(x) for x in str(parent1)]
    parent2 = [int(x) for x in str(parent2)]
    
    parent1[random.randint(0,7)] = r1
    parent2[random.randint(0,7)] = r
    
    r = random.randint(1,8)
    r1 = random.randint(1,8)
    
    parent1[random.randint(0,7)] = r1
    parent2[random.randint(0,7)] = r
    
    r = random.randint(1,8)
    r1 = random.randint(1,8)
    
    parent1[random.randint(0,7)] = r1
    parent2[random.randint(0,7)] = r
    
    parent1 = [str(i) for i in parent1]
    parent2 = [str(i) for i in parent2]
    
    child1 = int("".join(parent1))
    child2 = int("".join(parent2))
    
    #print(child1)
    
    return [[child1],[child2]]
    
    
def offspring(parents):
    total = []
    for i in range(1):
        children1 = crossover(parents)
        children2 = mutation(parents)
        total = children1 + children2
    return total
    
 
def survival_selection(popl):
    p = sorted(popl,reverse=True, key = takeSecond)
    #p = list(set(p))
    #print(p)
    #random.shuffle(p)
    for i in range(4):
        p.pop()
    return p
    
    
def required_fitness(population):
    for l in population:
        if(l[1] == 8):
            return True
    
    return False
    
    
def eight_queens():
    population = init_population(10)
    compute_fitness(population)
    steps = 0
    for i in range(5000):
        steps +=1
        parents = parent_selection(population)
        children = offspring(parents)
        compute_fitness(children)
        population = population+children 
        population = survival_selection(population)
        if(required_fitness(population)):
            break
    
    print(f'Indiviual:{population[0][0]}')
    print(f'Fitness:{population[0][1]}')
    print(f'Steps:{steps}')
    
    board = init_board()
    set_board(board,population[0][0])
    print("Board:")
    print(board)
    print("1 denotes Queen.")


def main():
    eight_queens()
    #compute_fitness([[26834531]])
    #compute_fitness([[46827135]])


if '__main__'==__name__:
    main()
