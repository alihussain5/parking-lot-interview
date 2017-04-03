from infrastructure.spot import SpotSize
from vehicle import Vehicle


class Bus(Vehicle):
    '''
    Bus class with predefined parking spot sizes

    Args:
        name: a String to represent the Bus's name
    '''
    def __init__(self, name):
        super(Bus, self).__init__(name, SpotSize.LARGE)

        self._consecutive_spots = 5

    '''
    Property to represent how many parking spots a
        Bus will take up
    '''
    @property
    def get_spot_count(self):
        return self._consecutive_spots
