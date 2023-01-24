from random import * 
import pygame
import math
import sys

# -------------------------------------------------------------------------------

class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def Vset(self, vec):
		self.x = vec.x
		self.y = vec.y

	def set(self, x, y):
		self.x = x
		self.y = y

	def Vadd(self, vec):
		self.x += vec.x
		self.y += vec.y

	def Vsub(self, vec):
		self.x -= vec.x
		self.y -= vec.y

	def Vmult(self, vec):
		self.x *= vec.x
		self.y *= vec.y

	def mult(self, n):
		self.x *= n
		self.y *= n

	def Vdiv(self, vec):
		self.x /= vec.x
		self.y /= vec.y

	def div(self, n):
		self.x /= n
		self.y /= n

	def mag(self):
		return math.sqrt( self.x**2 + self.y**2 )

	def magSq(self):
		return (self.x**2 + self.y**2)

	def normalize(self):
		m = self.mag()
		if (m != 0 and m != 1):
			self.div(m)

	def limit(self, m):
		if (self.magSq() > m**2):
			self.normalize()
			self.mult(m)


class Ball:
	def __init__(self, pos, vel, r, move, mass):
		self.positoin = Vector2(pos[0], pos[1])
		self.velocity = Vector2(vel[0], vel[1])
		self.radius = r
		self.move = move
		self.mass = mass

	def update(self, planets: None):
		self.velocity.limit(8)
		self.positoin.Vadd(self.velocity)

		if self.positoin.x < -self.radius: self.positoin.x = WIDTH + self.radius
		if self.positoin.y < -self.radius: self.positoin.y = HEIGHT + self.radius
		if self.positoin.x > WIDTH + self.radius: self.positoin.x = -self.radius
		if self.positoin.y > HEIGHT + self.radius: self.positoin.y = -self.radius

		if self.move and planets != None:
			force_x = 0
			force_y = 0
			force = Vector2( force_x, force_y )
			for planet in planets: 
				force_x = ( planet.mass*0.00001*(planet.positoin.x - self.positoin.x) )
				force_y = ( planet.mass*0.00001*(planet.positoin.y - self.positoin.y) )
				self.velocity.set( self.velocity.x + force_x, self.velocity.y + force_y )

	def draw(self, surface):
		pygame.draw.circle(surface, (255, 255, 255), (self.positoin.x, self.positoin.y), self.radius)

# -------------------------------------------------------------------------------

WIDTH, HEIGHT = 680, 620
FRAMERATE = 60

# -------------------------------------------------------------------------------

pygame.init()
pygame.display.set_caption("Test")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

alpha_sur = pygame.Surface((WIDTH, HEIGHT))
alpha_sur.set_alpha(120)

# -------------------------------------------------------------------------------

all_objects = []

for _ in range(3):
	all_objects.append( Ball((randrange(WIDTH), randrange(HEIGHT)), (randint(-8, 8), randint(-8, 8)), randint(2, 8), True, randint(4, 16)) )

# -------------------------------------------------------------------------------

running = True
while running:
	# screen.fill((0, 0, 0))
	screen.blit( alpha_sur, (0, 0) )

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = not running

	for object_ in all_objects:
		object_.update(all_objects)
		object_.draw(screen)

	pygame.display.update()
	clock.tick(FRAMERATE)

else:
	pygame.quit()
	sys.exit()