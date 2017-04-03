import uuid

from spot import Spot, SpotSize
from vehicle.bus import Bus


class Level(object):
    '''
    Parking level class that'll control assigning and unassigning
        vehicles to parking spots

    Args:
        template: a path to a file in templates/ that contains the
            level template as a text file
    '''
    def __init__(self, template):
        self._rows = []
        self._parked = {}
        self._queue = [[] for i in SpotSize.ALL]

        self._initialize_template(template)

    '''
    Finds parking spots for `vehicle` in the current Level and parks
        them if possible

    Args:
        vehicle: Vehicle object

    Returns:
        a String representing the `key` to retrieve `vehicle` from
            its parking spots if a parking spot is found, else returns None
    '''
    def park(self, vehicle):
        if isinstance(vehicle, Bus):
            spots = self._get_consecutive_spots(vehicle)
        else:
            spots = self._get_single_spot(vehicle)

        if spots is None:
            return

        for spot in spots:
            spot.park(vehicle)

        key = self._set_parked_spot(spots)
        return key

    '''
    Retrieves the Vehicle that was stored in this Level using `key`

    Args:
        key: a String that was returned by Level.park

    Returns:
        a Vehicle object, else returns None if there was no vehicle
            parked under `key`
    '''
    def unpark(self, key):
        spots = self._get_parked_spot(key)

        if spots is None:
            return

        for spot in spots:
            vehicle = spot.unpark()
            self._readd_spot(spot)

        return vehicle

    '''
    Helper function to initialize the Level's rows using a passed
        template file, this is called from __init__
    '''
    def _initialize_template(self, template):
        template_file = open('templates/{}'.format(template))
        template_arr = [row_template.split() for row_template in template_file]

        for i in xrange(len(template_arr)):
            new_row = []

            for j in xrange(len(template_arr[i])):
                spot_size = int(template_arr[i][j])

                new_spot = Spot(size=spot_size)
                new_row.append(new_spot)

                self._queue[spot_size].append(new_spot)

            self._rows.append(new_row)

    '''
    Helper function to look through the available parking spots to
        return a list of consecutive parking spots that can fit `vehicle`
    '''
    def _get_consecutive_spots(self, vehicle):
        n = vehicle.get_spot_count

        for i in xrange(len(self._rows)):
            count = 0
            for j in xrange(len(self._rows[i])):
                spot = self._rows[i][j]

                if spot.can_fit(vehicle):
                    count += 1
                else:
                    count = 0

                if count == n:
                    spots = self._rows[i][(j - n + 1):(j + 1)]
                    self._remove_spots_from_queue(spots)
                    return spots

    '''
    Helper function used by _get_consecutive_spots to remove the retrieved
        spots from the queueonce they've been found.

    This is needed because we can't use the queue to retrieve consecutive
        spots, so when a set of consecutive spots is picked from the Level,
        it needs to be removed from the queue
    '''
    def _remove_spots_from_queue(self, spots):
        spots_set = set(spots)
        spot_size = spots[0].get_size

        old_queue = self._queue[spot_size]

        new_queue = [spot for spot in old_queue if spot not in spots_set]

        self._queue[spot_size] = new_queue

    '''
    Helper function to return the smallest available parking spot that will fit
        vehicle, returns a list of Spot
    '''
    def _get_single_spot(self, vehicle):
        for i in SpotSize.ALL:
            if self._queue[i] and self._queue[i][0].can_fit(vehicle):
                return [self._queue[i].pop()]

    '''
    Keeps a record of the used parking spot to later be retrieved by
        _get_parked_spot. Returns a String to represent the key
    '''
    def _set_parked_spot(self, spots):
        key = self._gen_key()
        self._parked[key] = spots
        return key

    '''
    Returns the parking spots stored under `key` or None if none exist
    '''
    def _get_parked_spot(self, key):
        if key not in self._parked:
            return

        spots = self._parked[key]
        del self._parked[key]

        return spots

    '''
    Helper to add a recently freed parking spot back into the queue
    '''
    def _readd_spot(self, spot):
        spot_size = spot.get_size
        self._queue[spot_size].append(spot)

    '''
    Generates a random hexadecimal UUID4 String
    '''
    @classmethod
    def _gen_key(cls):
        return uuid.uuid4().hex
