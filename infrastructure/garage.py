from level import Level


class Garage(object):
    '''
    Main Parking Garage class to handle the insertion and removal of
        vehicles in the parking garage

    Args:
        levels: the numbers of levels the garage will have
        template: a path to a file in templates/ that contains the
            level template as a text file
    '''
    def __init__(self, levels, template='default.txt'):
        self._parked = {}
        self._levels = []

        for i in xrange(levels):
            new_level = Level(template=template)
            self._levels.append(new_level)

    '''
    Finds a parking spot in the Garage to park `vehicle`

    Args:
        vehicle: a Vehicle object

    Returns:
        a String representing the `key` to retrieve `vehicle` after
            it's parked, else None if there is nowhere to park `vehicle`
    '''
    def park(self, vehicle):
        for level in self._levels:
            key = level.park(vehicle)
            if key:
                self._set_parked_level(level, key)
                return key

    '''
    Retrieves the Vehicle that was stored in Garage using `key`

    Args:
        key: a String that was returned by Garage.park

    Returns:
        a Vehicle object, else None if there is no Vehicle stored under `key`
    '''
    def unpark(self, key):
        level = self._get_parked_level(key)

        if not level:
            return

        vehicle = level.unpark(key)

        return vehicle

    '''
    Stores level's id and a key in the Garage, returns the key of
        where it's stored
    '''
    def _set_parked_level(self, level, key):
        self._parked[key] = level

    '''
    Returns the level id and key stored under `key`, else None if it
        doesn't exist
    '''
    def _get_parked_level(self, key):
        if key not in self._parked:
            return

        level = self._parked[key]
        del self._parked[key]

        return level
