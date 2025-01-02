#! /usr/bin/python

import math

def main():

	turtle = Turtle(0, 0, 0, 1)
	while True:
		input = raw_input()
		if input == '0,0':
			break

		args = input.strip().split(',')
		dist = int(args[0])
		degree = int(args[1])

		rad = 2 * math.pi * degree / 360.0

		turtle.move(dist)
		turtle.rotate(rad)

	print("%d" % (turtle.x))
	print("%d" % (turtle.y))

class Turtle:

	def __init__(self, x, y, vx, vy):
		self.x  = x
		self.y  = y
		self.vx = vx
		self.vy = vy
		self.normalize_velocity()

	def move(self, dist):
		self.x += self.vx * dist
		self.y += self.vy * dist

	def normalize_velocity(self):
		vx = self.vx
		vy = self.vy
		v = math.sqrt(vx * vx + vy * vy)
		self.vx = vx / v
		self.vy = vy / v

	def rotate(self, theta):
		vx = self.vx
		vy = self.vy

		self.vx = vx * math.cos(theta) + vy * math.sin(theta)
		self.vy = -vx * math.sin(theta) + vy * math.cos(theta)


main()