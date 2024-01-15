''' Demonstrate class properties '''
class Grader():
    ''' Represent a grade as a numeric score '''
    def __init__(self, score=0): 
        self.score = score

math = Grader(90)
print()
print()
print ('The math score was %s.' % math.score)
math.score = 101
print ('The math score was changed to %s.' % math.score)

class Grades():
    ''' Represent a grade as a numeric score with a property '''
    def __init__(self, score=0):
        self._score = score
    @property 
    def score(self):
        return self._score

    @score.setter
    def score (self, value): 
        if value > 100 or value < 0:
            raise ValueError('Invalid score')
        self._score = value

math = Grades(90)
print()
print()
print('The math score was %s.' % math.score)
try:
    math.score = 101
except ValueError:
    print('That score is not allowed')

class ReadOnly():
    ''' Demonstrate a read only property '''
    @property
    def constant (self):
        return 24
    
only_read = ReadOnly()
print()
print()
print('The constant has the value:', only_read.constant)

try:
    only_read. constant = 25
except AttributeError:
    print('Properties cannot be changed without a setter')

class HardWay():
    ''' Demonstrate property function '''
    def __init__(self, value=True):
        self.hardset(value)

    harddoc = 'Properties can have a getter, setter, deleter, and doc string'
    def hardset (self, value):
        if value:
            self.way = True
        else:
            self.way = False
    def hardget(self):
        return self.way
    def harddel(self):
        self.way = None
    hard = property(fget=hardget, fset=hardset, fdel=harddel, doc=harddoc)

not_decorated=HardWay()
not_decorated.hard='test' 
print()
print()
print('The value of not decorated. hard is', not_decorated.hard) 
del not_decorated.hard
print()
print()
print('The value of not _decorated hard is', not_decorated.hard)
print (HardWay.hard.__doc__ )
