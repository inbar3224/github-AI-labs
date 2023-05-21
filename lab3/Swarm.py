# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from random import randint
from Particle import *

class Swarm():
    def __init__(self, args):
        self.args = args
        self.particles = []
        self.gbest_pos = None
        self.tsize = len(self.args.GA_TARGET)
        self.gbest_fitness = float('inf')
        self.W = 0.5
        self.c1 = 0.8
        self.c2 = 0.9

    def calc_fitness(self, particle):
        str_target = [ord(char) for char in self.args.GA_TARGET]
        fitness = 0
        for i in range(self.tsize):
            fitness += (abs(particle[i] - str_target[i]))
        return fitness

    def sort_by_fitness(self, particles):
        particles.sort(key=lambda i: i.fitness)
        self.gbest_pos = particles[0].position
        self.gbest_fitness = particles[0].fitness

    def initParticles(self):#initilaize the particles array that is indeed the population or the swarm
        for i in range(self.args.GA_POPSIZE):
            velocity = []
            position = []
            for j in range(self.tsize):
                velocity.append(randint(32, 122))
                position.append(randint(32, 122))
            if self.gbest_pos is None:#initilize global best position
               self.gbest_pos = position[0:]
            elif self.calc_fitness(position) < self.calc_fitness(self.gbest_pos):
                self.gbest_pos = position
            particle = Particle(position, self.calc_fitness(position), velocity)
            self.particles.append(particle)

    def to_str(self, gbest_pos):#function to convert to type string
        str = ""
        for i in range(len(gbest_pos)):
            str += chr(gbest_pos[i])
        return str

    def myPersonalBest(self, fitness, particle):
            if(particle.pbest_fitness > fitness):
                particle.pbest_fitness = fitness
                particle.pbest_pos = particle.position

    def globalBest(self, fitness, particle):
            if(self.gbest_fitness > fitness):
                self.gbest_fitness = fitness
                self.gbest_pos = particle.position

    def update_para(self, index, size):#function to update pso parameters
        self.c1 = -3 * (index / size) + 3.5
        self.c2 = 3 * (index / size) + 0.5
        self.W = 0.4 * ((index - size)/ size ** 2) + 0.4
