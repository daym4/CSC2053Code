# Madison Day
# Practice for Python Exam

# Car class has the tester file called car_tester.py
'''
Create a class called Car in a file called car.py
The class Car should have the following instance variables:
• color- this is the color of the car
• engine_type -this is the type of engine the car has
• gas_tank - keeps track of how many gallons of gas are in the tank
• odometer - keeps track of the car mileage


The Car class should have the following class methods:
__init__ - the init method should have the color, engine_type, gas_tank, and odometer as parameters to initialize the car.
'''
class Car:
    def __init__(self, color, engine_type, gas_tank, odometer):
        self.color = color
        self.engine_type =engine_type
        self.gas_tank = gas_tank
        self.odometer = odometer
# __str__ method- the str method should return the color of the car 
# concatenated with the engine type of the car.
    def __str__(self):
        return 'Color: ' + self.color + '.  Engine type: ' + self.engine_type
    '''
    drive method - if the engine type is “4_cylinder” 
    then drive should reduce the gas_tank by 3 gallons 
    and increase the odometer value by 90 miles. 
    If the engine type is “V8” then the drive method should 
    reduce the gas_tank by 4 gallons and increase the odometer by 50 miles.
    '''
    def drive(self):
        if self.engine_type == '4_cylinder':
            self.gas_tank -= 3
            self.odometer += 90
        elif self.engine_type == 'V8':
            self.gas_tank -= 4
            self.odometer += 50
    # get_gas_tank method – returns the number of gallons of gas left in the car.
    # when concatenating gas_tank- cast it as a str so gas_tank stays an integer
    def get_gas_tank(self):
        return 'Number of gallons of gas left in the tank: ' + str(self.gas_tank)
    # get_odomoter method – returns the mileage of the car
    def get_odometer(self):
        return 'Mileage of the car (from odometer): ' + str(self.odometer)
