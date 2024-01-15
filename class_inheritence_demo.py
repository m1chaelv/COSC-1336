''' Demonstrate class inheritance '''
class Base_Model(): 
    ''' Represent the base model of a car '''
    trim = 'base normal'
    engine_liters = 1.5

    def engine_sound(self):
        return 'base putt, putt'

    def horn_sound(self):
        return 'base beep, beep'

    def __str__(self):
        return 'Base Model'

coop=Base_Model()
print()
print()
print(coop,coop.trim)
print(coop,coop.engine_liters)
print(coop,coop.horn_sound())
print(coop,coop.engine_sound())

class Sport_Model(Base_Model):
    engine_liters=2.0

    def engine_sound (self):
        return 'sport VROOM, VROOM'
    
    def horn_sound (self): 
        return 'sport BEEP, ВЕЕР'
    def __str__(self):
        return 'Sport Model'
    
coop_sport = Sport_Model()
print()
print()
print(coop_sport,coop_sport.trim)
print(coop_sport,coop_sport.engine_liters)
print(coop_sport,coop_sport.horn_sound())
print(coop_sport,coop_sport.engine_sound())

class Luxury_Model(Base_Model): 
    trim = 'luxury'

    def engine_sound(self):
        return 'luxury vroom, vroooM'
    
    def horn_sound(self):
        return 'luxury honk, honk'
    
    def __str__(self):
        return 'Luxury Model'

coop_luxury = Luxury_Model()
print()
print()
print(coop_luxury,coop_luxury.trim)
print(coop_luxury,coop_luxury.engine_liters)
print(coop_luxury,coop_luxury.horn_sound())
print(coop_luxury,coop_luxury.engine_sound())


class Luxury_Sport_Model(Luxury_Model, Sport_Model):
    def __str__(self):
        return 'Luxury Sport Model'
    
coop_luxury_sport = Luxury_Sport_Model()
print()
print()
print(coop_luxury_sport,coop_luxury_sport.trim)
print(coop_luxury_sport,coop_luxury_sport.engine_liters)
print(coop_luxury_sport,coop_luxury_sport.horn_sound())
print(coop_luxury_sport,coop_luxury_sport.engine_sound())

class Sport_Luxury_Model(Sport_Model, Luxury_Model):
    def __str__(self):
        return 'Sport Luxury Model'
    
coop_sport_luxury = Sport_Luxury_Model ()
print()
print()
print(coop_sport_luxury,coop_sport_luxury.trim)
print(coop_sport_luxury,coop_sport_luxury.engine_liters)
print(coop_sport_luxury,coop_sport_luxury.horn_sound())
print(coop_sport_luxury,coop_sport_luxury.engine_sound())

print()
print()
coop_custom = Sport_Luxury_Model()
print('%s has %s trim level.' % (coop_custom, coop_custom.trim)) 
coop_custom.trim = 'custom'
print('%s now has %s trim level.' % (coop_custom, coop_custom.trim)) 
print('The class %s still has %s trim level.' % (Sport_Luxury_Model, Sport_Luxury_Model.trim))
coop_custom.brakes = 'racing'
Base_Model.brakes = 'standard' 
print ('%s has %s brakes.' % (coop_custom, coop_custom.brakes))
print ('%s has %s brakes.' % (Sport_Luxury_Model, Sport_Luxury_Model.brakes))
