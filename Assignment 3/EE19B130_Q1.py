"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 3
	Q1. Class for complex numbers
"""
import math

class Complex:
	"""
	class of complex numbers
	"""
	def __init__(self, real, imag):
		self._real = real
		self._imag = imag

	def get_real(self):
		return self._real

	def get_imag(self):
		return self._imag

	def __add__(self, other):
		result = Complex(self._real, self._imag)
		result._real += other._real
		result._imag += other._imag
		return result

	def polar_form(self):
		re = self._real
		im = self._imag

		r = (re*re + im*im)**0.5

		if r > 0:
			theta = math.asin(im/r)
		else:
			theta = 0

		result = "{r:0.2f}(cos({theta:0.2f}) + i sin({theta:0.2f}))".format(r=r,theta=theta)
		return result

	def __str__(self):
		re = self._real
		im = self._imag

		if(im==1):
			result = "{self._real}+i".format(self=self)
		elif(im==-1):
			result = "{self._real}-i".format(self=self)
		elif(im<0):
			result = "{self._real}{self._imag}i".format(self=self)
		else:
			result = "{self._real}+{self._imag}i".format(self=self)

		return result


if __name__ == '__main__':
	a = Complex(3,-5)
	b = Complex(1,2)
	print("a:",a)
	print("b:",b)

	#addition
	c = a + b
	print("a+b:",c)

	#polar form
	print("Polar form of a:",a.polar_form())