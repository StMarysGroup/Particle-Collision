import pygame
import random
import Queue

''' Event driven particle simulation, hard bodies (disks) bouncing off of each other and the walls
'''



class EventSystem:
	def __init__(self, particles):
		self.particles = particles
		self.time = 0
		self.hz = 0.5
		self.timeUntilEvent = 0
		self.timeOfEvent = 0
		self.pq = Queue.PriorityQueue()

	def Update(self):
		self.time = self.time + 1

		#if self.time = self.timeOfEvent:
		#	self.candidate

	# update the pq with new events for particle a
	def predict(self, a, limit):
		if a is None:
			return 

		# particle - particle collisions
		for particle in self.particles:
			dt = a.timeToHitParticle(particle)
			if (dt + self.time <= limit):
				# pq.put (time of event(dt + t), event(time of event (dt + t), particle, particle))
				# scratch that, updated comparator for the events, now i should only have to put in a single thing (the particle)
				# update 9/9: this works, see priorityQueue.py
				self.pq.put(Event(dt + self.time, a, particle))

		#particle - wall collisions
		dtX = a.timeToHitVerticalWall()
		dtY = a.timeToHitHorizontalWall()
		if (t + dtX <= limit):
			self.pq.put(new Event(t + dtX, a, None))
		if (t + dtY <= limit):
			self.pq.put(new Event(t + dtY, None, a))

		# redraw the particles (not sure if i want to do it like how they say to)
			# actually maybe it is ok, they draw all the particles and then make a new empty event for some reason

	def simulate(self, limit):
		self.pq = Queue.PriorityQueue()
		for particle in self.particles:
			predict(particle, limit)

		self.pq.put(Event(0, None, None))

		while (not self.pq.Empty()):
			# get impending event, discard if invalid
			e = pq.get()
			if (not e.isThisEventStillValid()):
				continue
			a = e.a
			b = e.b

			# collision, update positions and clock
			for particle in self.particles:
				particle.move(e.time - t)

			self.time = e.time

			# process event
			if (a != None and b != None):
				a.bounceOffOfOtherParticle(b)
				



		




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
		if self.time < otherEvent.time:
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

	def __cmp__(self, otherEvent):
		return self.compareTimeOfEvents(otherEvent)



class Particle:
	def __init__(self, rx, ry, vx, vy, s, mass, screen):
		# position
		self.rx = rx
		self.ry = ry
		# velocity
		self.vx = vx
		self.vy = vy
		# radius
		self.s = s
		# mass
		self.mass = mass
		# number of collisions so far, pygame screen, color
		self.count = 0
		self.screen = screen
		self.GREEN =  (0, 255, 0)


	def Update(self):
		self.draw()
		self.move(0)
		self.timeToHitWall()

	def move(self, dt):
		self.rx += self.vx * dt
		self.ry += self.vy * dt

	def draw(self):
		pygame.draw.circle(self.screen, self.GREEN, (self.rx, self.ry), self.s, 0)

	def count():
		return self.count

	def timeToHitParticle(self, ParticleB):
		# he makes a copy for some reason, idk why.
		if self is ParticleB:
			return INFINITY
		# diff in x, y
		dx = ParticleB.rx - self.rx
		dy = ParticleB.ry - self.ry
		# diff in velocity
		dvx = ParticleB.vx - self.vx
		dvy = ParticleB.vy - self.vy
		# the 
		dvdr = dx*dvx + dy*dvy
		if dvdr > 0:
			return INFINITY
		# diff in velocity squared
		dvdv = dvx*dvx + dvy*dvy
		# diff in position squared
		drdr = dx*dx + dy*dy
		# the distance between the centers of the particles at collision
		sigma = self.radius + ParticleB.radius
		d = (dvdr*dvdr) - dvdv * (drdr - sigma*sigma)
		# overlap if drdr < sigma*sigma
		if d < 0 return INFINITY
		# return the time that it will be when the particles hit
		return -(dvdr + math.sqrt(d)) / dvdv


	'''def timeToHitWall(self):
		
		dt = (width - self.s - self.rx)/self.vx
		print(dt)
		if dt == 0:
			self.vx = self.vx * -1
			#dt = 1
	'''


	# NOTE: might have height/width backwards in some places!!! should be easy to tell!
	def timeToHitVerticalWall(self):
		if self.vx > 0:
			return (height - self.rx - self.radius) / self.vx
		elif self.vx < 0:
			return (self.radius - self.rx) / self.vx
		else:
			return INFINITY

	def timeToHitHorizontalWall(self):
		if self.vy > 0:
			return (self.height - self.ry - self.radius) / self.vy
		elif self.vx < 0:
			return (self.radius - self.ry) / self.vy
		else:
			return INFINITY	
		
	def bounceOffOfOtherParticle(self, other):
		dx = other.rx - self.rx
		dy = other.ry - self.ry
		dvx = other.vx - self.vx
		dvy = other.vy - self.vy
		dvdr = dx*dvx + dy*dvy # dv dot dr
		dist = self.radius + other.radius

		# normal force, split into directions
		F = 2 * self.mass * other.mass * dvdr / ((self.mass + other.mass) * dist)
		fx = F*dx/dist
		fy = F*dy/dist

		# update velocities 
		self.vx += fx/self.mass
		self.vy += fy/self.mass
		other.vx -= fx/self.mass
		other.vy -= fy/self.mass

		# update counts of collisions
		self.count += 1
		other.count += 1

	def bounceOffOfVerticalWall(self):
		self.vx = -self.vx
		self.count += 1

	def bounceOffOfHorizontalWall(self):
		self.vy = -self.vy
		self.count += 1

	def getKineticEnergy(self):
		return 0.5 * self.mass * (self.vx*self.vx + self.vy*self.vy)







print("test")


INFINITY = float("inf")

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

