from infrastructure.spot import SpotSize
from vehicle import Vehicle


class Motorcycle(Vehicle):
    '''
    Motorcycle class with predefined parking spot size

    Args:
        name: a String representing the Motorcycle's name
    '''
    def __init__(self, name):
        super(Motorcycle, self).__init__(name, SpotSize.MOTORCYCLE)
