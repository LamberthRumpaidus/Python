import random

N = 9
POPULATION_SIZE = 100

class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        global N
        gene = random.randint(1, N)
        return gene

    @classmethod
    def create_gnome(self):
        global N
        gnome_len = N*N
        return [self.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):    
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(self.mutated_genes())
        return Individual(child_chromosome)

    def cal_fitness(self):
        global N
        fitness = 0
        for i in range(N):
            for j in range(N):
                if i != j and self.chromosome[i] == self.chromosome[j]:
                    fitness += 1
        return fitness

def main():
    global POPULATION_SIZE
    generation = 1
    found = False
    population = []
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                population.append(Individual(gnome))
    while not found:
        population = sorted(population, key = lambda x:x.fitness)
        if population[0].fitness <= 0:
            found = True
            break
        new_generation = []
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation
        print("Generation: {}\tString: {}\tFitness: {}".
              format(generation,
              "".join(str(population[0].chromosome)),
              population[0].fitness))
        generation += 1

if __name__ == '__main__':
    main()
