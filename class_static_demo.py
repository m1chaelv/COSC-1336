''' Demonstrate static methods '''
import locale
import sys

class Base():
    ''' Represent the base model of a car '''
    trim = 'normal'
    miles_range = 450 
    engine_liters = 1.5
    color = 'white' 
    tank_capacity = 45
    transmission='automatic'

    @staticmethod
    def miles_per_liter(miles_range, tank_capacity): 
        return miles_range / tank_capacity

    def miles_per_gallon(miles_range, tank_capacity):
        return Base.miles_per_liter(miles_range, tank_capacity) * 3.78541
    miles_per_gallon = staticmethod(miles_per_gallon) 

    def __init__(self, price, transmission='automatic', color='white'):
        self.price = price 
        self.transmission = transmission
        self.color = color

    def info (self):
        if sys.platform.startswith('win'):
            locale.setlocale(locale.LC_ALL, 'us')
        else:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        print('The price of a %s was %s.' %  
        (self,locale.currency(self.price)))

    def __str__(self):
        return '%s base model with %s transmission' % (self.color, self.transmission)


print()
print()
coop = Base(color='green', transmission='automatic', price=25000)
coop.info()
print('The %s gets %4.1f miles per gallon' % (coop, coop.miles_per_gallon(coop.miles_range, coop.tank_capacity))) 
print('The %s gets %4.1f miles per gallon' % (Base, Base.miles_per_gallon(Base.miles_range, Base.tank_capacity)))

class Sport(Base):
    ''' Represent the sport model of a car based on a base mode'''
    miles_range = 400
    engine_liters = 2.0

print()
print()
sport = Sport(color='red', transmission='manual', price=26300)
sport.info()
print('The %s gets %4.1f miles per gallon' % (sport, sport.miles_per_gallon (sport.miles_range, sport.tank_capacity)))
print('The %s gets %4.1f miles per gallon' % (Sport, Sport.miles_per_gallon (Sport.miles_range, Sport.tank_capacity)))

