from infrastructure.spot import SpotSize
from vehicle import Vehicle


class Car(Vehicle):
    '''
    Car class with predefined parking spot size

    Args:
        name: a String representing the Car's name
    '''
    def __init__(self, name):
        super(Car, self).__init__(name, SpotSize.COMPACT)
