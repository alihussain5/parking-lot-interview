class SpotSize(object):
    '''
    Enumeration class to represent the different parking spot sizes
    '''
    LARGE = 2
    COMPACT = 1
    MOTORCYCLE = 0

    ALL = set([0, 1, 2])


class Spot(object):
    '''
    The Parking Spot class that will house the parked vehicles

    Args:
        size: an Integer from the SpotSize class representing the
            size of the Parking Spot
    '''
    def __init__(self, size):
        self._vehicle = None
        self._size = size

    '''
    Checks if there is currently a vehicle parked in this Spot

    Returns:
        Boolean
    '''
    def is_empty(self):
        return self._vehicle is None

    '''
    Property method to get the size of the Parking Spot

    Returns:
        Integer in the form of the SpotSize class
    '''
    @property
    def get_size(self):
        return self._size

    '''
    Method to check if the Parking Spot can fit a given vehicle

    Class:
        vehicle: a Vehicle object

    Returns:
        Boolean
       '''
    def can_fit(self, vehicle):
        return self.is_empty() and (self.get_size >= vehicle.get_size)

    '''
    Method to try and park a vehicle in the current parking Spot

    Args:
        vehicle: a Vehicle object

    Returns:
        Boolean representing if vehicle was successfully parked
    '''
    def park(self, vehicle):
        if not self.can_fit(vehicle):
            return False

        self._vehicle = vehicle
        return True

    '''
    Method to remove the current Vehicle parked in the parking Spot

    Returns:
        a Vehicle object or None if there was no vehicle parked
    '''
    def unpark(self):
        vehicle = self._vehicle
        self._vehicle = None
        return vehicle
