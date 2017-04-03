class Vehicle(object):
    '''
    Vehicle virtual class template for the vehicles that'll be
        parking in the garage

    Args:
        name: a String representing the name of the car
        size: the size of the car as an integer, predefined sizes
            can be found in infrastructure.spot.SpotSize
    '''
    def __init__(self, name, size):
        self._name = name
        self._size = size

    '''
    Property to get the Vehicle's name

    Returns:
        a String representing the Vehicle's name
    '''
    @property
    def get_name(self):
        return self._name

    '''
    Property to get the Vehicle's size

    Returns:
        an Int representing the Vehicle's size. Look in
            infrastructure.spot.SpotSize for different vehicle sizes
    '''
    @property
    def get_size(self):
        return self._size
