from vector2 import Vector2
from random import *

import pygame
import math
import sys

# -------------------------------------------------------------------------------

class Planet:
	def __init__(self, pos, vel, r, pull, mass):
		self.positoin = Vector2(arr=pos)
		self.velocity = Vector2(arr=vel)
		self.velocity.mult(4)
		self.radius = r
		self.pull = pull
		self.mass = mass


	def movement(self):
		self.velocity.limit(4)
		self.positoin.Vadd(self.velocity)

		if self.positoin.x < -self.radius: self.positoin.x = WIDTH + self.radius
		if self.positoin.y < -self.radius: self.positoin.y = HEIGHT + self.radius
		if self.positoin.x > WIDTH + self.radius: self.positoin.x = -self.radius
		if self.positoin.y > HEIGHT + self.radius: self.positoin.y = -self.radius


	def get_collision(self, planet):
		distance = math.sqrt( (planet.positoin.x - self.positoin.x)**2 + (planet.positoin.y - self.positoin.y)**2 )
		if distance <= planet.radius + self.radius:
			return True
		else:
			return False


	def reflection(self, planet):
		v = Vector2(arr=self.velocity.Tget())
		u = Vector2(arr=planet.velocity.Tget())

		self.velocity.Vset(u)
		planet.velocity.Vset(v)


	def attraction(self, list_planets, skipping):
		if list_planets != None:
			force = Vector2()
			for planet in list_planets:
				if planet != skipping:
					if self.get_collision(planet):
						self.reflection(planet)
				if self.pull:
					force_x = ( planet.mass*GRAVITY*(planet.positoin.x - self.positoin.x) )
					force_y = ( planet.mass*GRAVITY*(planet.positoin.y - self.positoin.y) )
					force.set( force_x, force_y )
					self.velocity.set( self.velocity.x + force.Xget(), self.velocity.y + force.Yget() )


	def update(self, list_planets=None, skipping=None):
		self.movement()
		self.attraction(list_planets, skipping)


	def draw(self, surface):
		pygame.draw.circle(surface, (255, 255, 255), (self.positoin.x, self.positoin.y), self.radius, self.mass)

# -------------------------------------------------------------------------------

WIDTH, HEIGHT = 520, 520
FRAMERATE = 60
GRAVITY = 0.00001

# -------------------------------------------------------------------------------

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

alpha_sur = pygame.Surface((WIDTH, HEIGHT))
alpha_sur.set_alpha(120)

# -------------------------------------------------------------------------------

list_planets = []
for _ in range(8):
	list_planets.append(
		Planet((randint(0, WIDTH), randint(0, HEIGHT)), (uniform(-1, 1), uniform(-1, 1)), randint(8, 16), True, randint(2, 4))
	)


# -------------------------------------------------------------------------------

running = True
while running:
	# screen.fill((0, 0, 0))
	screen.blit( alpha_sur, (0, 0) )

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = not running

	for planet in list_planets:
		planet.update(list_planets, planet)
		planet.draw(screen)

	pygame.display.update()
	clock.tick(FRAMERATE)

else:
	pygame.quit()
	sys.exit()