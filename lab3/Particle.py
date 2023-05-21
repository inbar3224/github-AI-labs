# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from random import random


class Particle:
    def __init__(self, position, fitness, velocity, problemData):
        self.pos_size = len(position)
        self.velocity = velocity
        self.position = position
        self.fitness = fitness
        self.pbest_pos = position
        self.pbest_fitness = fitness
        self.all_dist = problemData.tour_cost_veh()

    def make_round(self, position):
        for i in range(len(position)):
            position[i] = round(position[i])
        return position

    def position(self, c1, c2, W):
          gloabl_best = self.all_dist()
          i = c1 * random() * (gloabl_best - self.all_dist(self.position))
          j = c2 * random() * (gloabl_best - self.all_dist(self.position))
          self.velocity = int(self.velocity * random() * W + i + j)
          if self.velocity < 0:
              self.velocity *= -1
          self.velocity = self.velocity % len(self.position)

          for i in range(int(len(self.position)/2)):
              newhold = self.position[i]
              self.position[i] = self.position[(i+self.velocity) % len(self.position)]
              self.position[(i + self.velocity) % len(self.position)] = newhold


    def merge(self, str1, str2):#function to merge two strings
        new_string = []
        for i in range(len(str1)):
            new_string.append((str1[i]) + (str2[i]))
        return new_string

    def pso_str(self, str1, str2, para):#function to create a new string that match pso algorithm
        new_string = []
        for i in range(len(str1)):
            new_string.append((para * ((str1[i]) - (str2[i]))))
        return new_string

    def tour_cost_veh(self, tour, cities):# this function calculates the cost of the vehicle's tour
        matrix = self.Distance_mat()
        count = matrix[tour[0]][0]
        last = len(tour)
        veh_capacity = self.Capacity - self.Cities[tour[0] - 1].demand
        for i in range(last - 1):
            curr = tour[i]
            target = tour[i+1]
            if self.Cities[target-1].demand <= veh_capacity:
                count += matrix[curr][target]
                veh_capacity -= self.Cities[target-1].demand
            else:
                count += matrix[curr][0]
                veh_capacity = self.Capacity - self.Cities[target - 1].demand
                count += matrix[target][0]# new tour for new vehicle starting at target

        count += matrix[tour[last - 1]][0]
        return count
