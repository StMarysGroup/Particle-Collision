import pygame
import random

''' Event driven particle simulation, hard bodies (disks) bouncing off of each other and the walls
'''


class EventSystem:
	def __init__(self):
		self.particles = []
		self.candidate = None
		self.time = 0
		self.timeUntilEvent = 0
		self.timeOfEvent = 0

	def Update(self):
		self.time = self.time + 1
		#if self.time = self.timeOfEvent:
		#	self.candidate

		




class Event:
	def __init__(self, t, ParticleA, ParticleB):
		self.time = t
		self.a = ParticleA
		self.b = ParticleB
		self.CountA = 0
		self.CountB = 0
		if self.a:
			self.CountA = self.a.count()
		else:
			self.CountA = -1
		if self.b:
			self.CountB = self.b.count()
		else:
			self.CountB = -1

	def compareTimeOfEvents (self, otherEvent):
		if self.time < otherEvent.time
			return -1
		elif self.time > otherEvent.time:
			return 1
		else:
			return 0
	def isThisEventStillValid(self):
		if self.a and self.a.count() is not self.CountA:
			return False
		if self.b and self.b.count() is not self.CountB:
			return False
		return True



class Particle:
	def __init__(self, rx, ry, vx, vy, s, mass, screen):
		self.rx = rx
		self.ry = ry
		self.vx = vx
		self.vy = vy
		self.s = s
		self.mass = mass
		self.count = 0
		self.screen = screen
		self.GREEN =  (0, 255, 0)

	def Update(self):
		pygame.draw.circle(self.screen, self.GREEN, (self.rx, self.ry), self.s, 0)
		self.move(0)
		self.timeToHitWall()

	def move(self, dt):
		self.rx = self.rx + self.vx
		self.ry = self.ry + self.vy

	def count():
		return self.count

	#def timeToHit(b):

	def timeToHitWall(self):
		
		dt = (width - self.s - self.rx)/self.vx
		print(dt)
		if dt == 0:
			self.vx = self.vx * -1
			#dt = 1
			
		





print("test")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
# the width and height of the gamescreen
width = 700
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

done = False

clock = pygame.time.Clock()

particle = Particle(50, 50, 5, 1, 5, 2, screen)
eventSystem = EventSystem()
eventSystem.add(particle)


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
    

	screen.fill(BLACK)
	particle.Update()




	pygame.display.flip()
	clock.tick(60)

pygame.quit()

