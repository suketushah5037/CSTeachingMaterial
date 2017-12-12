import math

class Decorators:
    cirrad = 44
    #self can't be defined here
    #self.myname = "Shlok"

    #to group all directly written code to a class
    @staticmethod
    def area(r):
        print("cannot access, class or instance - to specify namespace methods")
        return r**2*math.pi

    @classmethod
    def myname(cls):
        return cls

    @classmethod
    def yourname(cls):
        return cls
    
    #can modify only the class's state and not the instance's state
    #cls is just a convention, can be "self" or anything else too
    #class is also an object
    #clas or cls or self, needs to be the first parameter
    @classmethod
    def sum(cls, a):
            print("can modify only the class's state and not the instance's state")
            return a+a, cls, Decorators.cirrad #, self.myname
    #defeating the self convention
    #can modify instance state and class state
    def normalmethod(myown):
        print("can modify instance state and class state")
        return 'instance called', myown.__class__, myown

    def __init__(self, radius):
        self.r = radius
        self.myname = "Shlok"
    #circle area will not modify the radius here
    def circlearea(self):
        #return self.r**2*math.pi
        return (self.area(self.r))
    def __str__(self):
        return 'Decorator object'
    #property
    #class variable
    CIRAREA = property(circlearea)
    
    
print("static method")
print(Decorators.area(4))
print("\n")
print("class method")
print(Decorators.sum(3))
print(Decorators.myname())
print(Decorators.yourname())
print("\n")

deco = Decorators(6)
print("instance method")
print(deco.normalmethod())
print("instance method through class and passing object")
print(Decorators.normalmethod(deco))
print("\n")
#static and class methods belong to class's and instances namespace
print("calling static method and class method using the object")
print(deco.area(10))
print(deco.sum(10))

print("\n\n")       
print("circle area using property")
print(deco.CIRAREA)
print("\n\n")
#cannot be done - since it calls a member function
#print(Decorators.ciracrea)
#class variable can be called directly
print(Decorators.cirrad)

#calling __str__
print("__str__")
print(deco)

class Empty:
    """hello"""
    pass

print("Empty class - location")
print(id(Empty))
emptyobj = Empty()
print("Empty instance - location")
print(id(emptyobj))

Empty.name = "Shlok"
print(Empty.name)

#instantiating class Empty
myempty = Empty()
print(myempty.__class__)
print(myempty.__doc__)
#__init__ is not the constructor
#class is also an object
#instance and class variables can be created on the fly- at any point of time

print("\n\n")
#Write your own decorator - to know how long the function takes to execute
print("DECORATORS")
import time
def timing(any_function):
    def wrapper():
        print("calculating start time")
        t1 = time.time()
        any_function()
        t2 = time.time()
        print("calculating end time")
        return "time taken = " + str(t2-t1) + "\n"
    return wrapper

@timing
def my_function():
    count=0;
    for i in range(1000000):
        count+=1
    print(count)


#calling my_function with the decorator
#same as my_function = timing(my_function)
#my_function()
print(my_function())
print("\n\n")


print("ANOTHER EXAMPLE")
import time
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

s = Spam()

s.instance_method(100000000)
Spam.class_method(100000000)
Spam.static_method(100000000)

