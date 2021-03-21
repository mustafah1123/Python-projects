#Importing math and time modules
import math
import time
import random

#Creating a class for each number set
class Reals():
    def __init__(self):
        self.dict_reals = {}

'''Transcendentals class is created as a subclass of Reals
as all transcendental numbers are real numbers too so they inherit the properties'''
class Transcendentals(Reals):
    
    def __init__(self):
        self.dict_trans = {}
    
    def add_element(self,d,x):
        self.dict_trans[d] = x

'''Algebraic class is created as a subclass of Reals as all
algebraic numbers - numbers that are a solution to a polynomial of N degree
with integers coefficients - are also real numbers.  Note that they are
NOT a subclass of Transcendentals as algebraic and transcendentals
are mutually exclusive sets'''
class Algebraic(Reals):

    '''Constructing a list of algebraic numbers can be challenging even to do a small interval
    from -100 to 100.  You can take the nth root of any number in that range '''
    def __init__(self):
        pass

    def add_element(self):
        pass

'''Rationals are created as a subclass of Algebraic class as all rationals are also algebraic numbers.
In fact all rationals are solutions to a polynomial of degree 1'''
class Rationals(Algebraic):

    #Create all rationals from -100 to 100
    def __init__(self):
        self.lst_ratio = ['0/1']
        for n in range(-pow(10,2),pow(10,2)+1):
            if n!= 0:
                for m in range(1,pow(10,2)):
                    if str(n)+'/'+str(m) not in self.lst_ratio:
                        self.lst_ratio.append(str(n)+'/'+str(m))

'''Integers is a subclass of rationals as all integers are rational numbers
with a denominator of 1'''
class Integers(Rationals):

    #Use the list of rationals lst_ratio to build out the integers list lst_int
    def __init__(self):
        '''The super function allows the Integers class to inherit the list of rationals
        that were constructed from the super class'''
        super().__init__()
        self.lst_int = []
        for n in self.lst_ratio:
            self.__n = int(n[0:n.find('/')])
            self.__m = int(n[n.find('/')+1:])
            if self.__n%self.__m == 0:
                if self.__n/self.__m not in self.lst_int:
                    self.lst_int.append(round(self.__n/self.__m))
        self.lst_int.sort()

'''Naturals is a subclass of Integers as all naturals numbers are nonnegative integers'''
class Naturals(Integers):
    
    def __init__(self):
        '''The super function allows the Naturals to inherit the list of integers
        that were constructed from its super class'''
        super().__init__()
        self.lst_nat = []
        for n in self.lst_int:
            if n>=0:
                self.lst_nat.append(n)
'''Primes class is a subclass of Naturals as all prime numbers are natural numbers
that have no factor other than 1 and itself'''
class Primes(Naturals):

    def __init__(self):
        '''The super function allows the Primes to inherit the list of naturals
        that were constructed from its super class'''
        super().__init__()
        self.lst_primes = [2,3,5,7]
        for p in self.lst_nat:
            if p > 10 and p%10 in [1,3,7,9]:
                j=0
                for i in range(3,int(pow(p,0.5))+1,2):
                    if p%i==0:
                        break
                    j+=1
                if j==len(range(3,int(pow(p,0.5))+1,2)):
                    self.lst_primes.append(p)

#Creating an object as an instance of class Transcendentals
t = Transcendentals()

#Creating Euler's number e using its factorial definition e= sum 0->inf 1/n!
e=0
for x in range(0,10000):
    e += 1/math.factorial(x)

#Creating Pi/4 using its factorial definition
pi= 0
k = 0
for x in range(1,10000000,2):
    k += 1
    if k %2 == 1:
        pi += 1/x
    else:
        pi -= 1/x

'''Adding e and Pi to the object t that is an instance of class Transcendentals
using a method called add_element'''
t.add_element('e',e)
t.add_element(chr(960),4*pi)

#Output the two elements added to the object t - Euler's number and Pi
for x,y in t.dict_trans.items():
    print(x,' = ',y)

'''Creating an object p as an instance of class Primes.  The list of primes will be built
automatically.  The reason is becase the constructor of the Primes class inherits the
constructor from its superclass Naturals that already includes the list of naturals'''
p = Primes()

#Output the rationals
print('Sample of rationals: ',random.sample(p.lst_ratio,200),end='\n')

#Output the integers
print('Integers:',p.lst_int, end= '\n')

#Output the naturals
print('Naturals:',p.lst_nat,end='\n')

#Out the primes
print('Primes:',p.lst_primes)
