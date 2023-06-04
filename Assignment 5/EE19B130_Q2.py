"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 5
	Q2. Ellipse area
"""	

import random
import math

def estimated_area_ellipse(total_points_generated):
	"""
	Estimate the area of the ellipse ((x^2)/4 + (y^2)/1 = 1) using random numbers.
	"""
	a = 2; b = 1 # where a,b represent semi-major and semi-minor axes of the ellipse
	area = 0
	points = []

	# Generate random points within the rectangle a*b
	for i in range(total_points_generated):
		x = random.uniform(0,a)
		y = random.uniform(0,b)
		points.append((x,y))

	# Count the number of points generated which are inside the ellipse
	interior = 0
	for i in range(total_points_generated):
		x = points[i][0]
		y = points[i][1]
		if((x*x)/(a*a) + (y*y)/(b*b) - 1 <= 0):
			interior += 1 

	# Area = 4*(Fraction of points generated within the rectangle which are inside the ellipse) * (Area of the rectangle a*b)
	# where 4 represent the four quadrants which the ellipse lie in
	area = 4*(interior/total_points_generated)*(a*b)
	return area


if __name__ == '__main__':
	total_points_generated = 100
	for i in range(4):
		calculated_area = math.pi * 2 * 1 #where area of ellipse = pi*a*b
		estimated_area = estimated_area_ellipse(total_points_generated)
		error = abs(estimated_area - calculated_area) / calculated_area * 100

		print("No. of points generated =",total_points_generated)
		print("Calculated area =",calculated_area)
		print("Estimated area =",estimated_area)
		print("Error =",error,"%\n")

		total_points_generated *= 10

	# As we increase the no. of random points generated, the estimated area becomes more accurate and thus the error decreases
	# The above output clearly proves the above point (Error decreases)