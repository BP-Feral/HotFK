# Setup Python ----------------------------------------------- #
import pygame
import random


# CLass Block ------------------------------------------------ #
class Particle:
    def __init__(self):

        self.particles = []


# Functions -------------------------------------------------- #
    def add_particles(self):
        pos_x = random.randint(0, 1920)
        pos_y = 1085
        radius = random.randint(3,8)
        direction_x = random.randint(-3, 0)
        direction_y = random.randint(-3, 3)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


# Updates ---------------------------------------------------- #
    def emit(self, screen):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                # up-down
                particle[0][1] += particle[2][0]
                # left-right
                particle[0][0] += particle[2][1]
                # shrink
                particle[1] -= 0.01
                # draw a circle around the particle
                if particle[0][0] > 0:
                    pygame.draw.circle(screen, (29, 11, 61), particle[0], int(particle[1]+2))
                    pygame.draw.circle(screen, pygame.Color('Black'), particle[0], int(particle[1]))