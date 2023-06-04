"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 3
	Q3. Object Oriented Biology!
"""

class Sars:
    '''
    This is a basic implementation of a class called Sars. 
    It can create a virus, find the average virulence of two viruses, and print the state of the virus based on its environment and virulence.
    >>> print(Sars(1,0.7))
    <1,0.7,Lytic>
    >>> print(Sars(1,0.7)+Sars(2,0.3))
    0.5
    >>> print(Sars(1,0.7).state(0.6))
    Lytic
    >>> a = Sars(3,0.8)
    >>> print(a._age)
    3
    >>> print(a.state(0.2))
    Lysogenic
    >>> print(a._age)
    4
    '''
    def __init__(self, age = 1,virulence = 0.5):
        '''Add your code here'''
        self._age = age
        self._virulence = virulence
        
    def __add__(self, other):
        '''Return the average virulence of the two viruses present in the system'''
        result = (self._virulence + other._virulence)/2
        return result
    
    def state(self, environment=0.5):
        '''Returns the state of the virus.
        If environment is favorable(environment>=0.5) and virus is virulent(virulence>=0.5): lytic state (the function returns "Lytic"); make the age 1
        Else, lysogenic state (the function returns "Lysogenic"); increment the age of the virus by 1'''
        if (environment>=0.5) and (self._virulence>=0.5):
        	self._age = 1
        	return "Lytic"
        else:
        	self._age += 1
        	return "Lysogenic"
    
    def __str__(self):
        '''Write a function that prints the virus’ state as: <age, virulence, state>'''
        state = self.state()
        result = "<{self._age},{self._virulence},{state}>".format(self=self,state=state)
        return result
        
import doctest
print(doctest.testmod())