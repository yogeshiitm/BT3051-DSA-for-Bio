class Person:
	def __init__(self,name,age,health,employmentStatus):
		self._name = name
		self._age = age
		self._health = {
			"height": health['height'], # in meter
			"weight": health['weight'], # in kg
			"blood_grp": health['blood_grp']
		}
		self._employmentStatus = employmentStatus

	def years_to_retirement(self):
		if(self._employmentStatus == 'employed'):
			return 60 - self._age
		else:
			return "Unemployed!"

	def calculate_BMI(self):
		return self._health["weight"]/(self._health["height"]**2)

	## a==b
	def __eq__(self,arg):
		if(self._name == arg._name and
			self._age == arg._age and
			self._health == arg._health and
			self._employmentStatus == arg._employmentStatus):
			return True
		else:
			return False

	## a!=b
	def __ne__(self,arg):
		return not (self == arg)


a = Person("Yogesh", "21", {"height":1.73, "weight":55, "blood_grp":"A+"}, "Unemployed")
b = Person("Yogesh", "21", {"height":1.73, "weight":55, "blood_grp":"A+"}, "Unemployed")
c = Person("Aditya", "21", {"height":1.73, "weight":55, "blood_grp":"A+"}, "Unemployed")
print(a.calculate_BMI())
print(a==b) #false -> but should be true
print(a!=c) #false -> but should be true