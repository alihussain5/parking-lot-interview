from infrastructure.garage import Garage
from vehicle.bus import Bus
from vehicle.car import Car
from vehicle.motorcycle import Motorcycle


levels = raw_input('How many levels: ')
levels = int(levels)
template = raw_input('Template file, leave empty for default: ')

if template != '':
    garage = Garage(levels, template)
else:
    garage = Garage(levels)

print 'Enter exit to exit at any time'
print 'Type `park <car/motorcycle/bus>` or `unpark <key>`'

list_of_keys = []

while 1:
    text = raw_input('Command: ')

    if text == 'exit':
        break

    text = text.split(' ')

    if len(text) != 2:
        continue

    (command1, command2) = text

    if command1 == 'park':
        if command2 == 'car':
            vehicle = Car('test car')
        elif command2 == 'motorcycle':
            vehicle = Motorcycle('test motorcycle')
        elif command2 == 'bus':
            vehicle = Bus('test bus')
        else:
            continue

        key = garage.park(vehicle)

        if key is None:
            print 'There is no more room'
        else:
            print 'Your key: {}'.format(key)
            list_of_keys.append(key)

    elif command1 == 'unpark':
        vehicle = garage.unpark(command2)

        if vehicle is None:
            print 'That vehicle does not exist'
        else:
            print 'You just retrieved a {}'.format(vehicle.get_name)
