#Create a new class called Point. This class will have a “x” and “y” attribute.
#write a function called distance_between_points that takes two Points as arguments and returns the distance between them.
#Test you function by instantiating two instances and assigning them x and y attributes of type Int

import math


class point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def distance_between_points(self):
		distance= math.sqrt(pow(self.x,2)+pow(self.y,2))
		return distance


p=point(3,4)
print(p.distance_between_points())





