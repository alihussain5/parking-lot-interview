# Parking Garage

An object-oriented parking garage implementation.

## Additional Assumptions
 * Vehicles cannot change assigned spots
 * Vehicles will move onto the next level of the parking garage only when they
 cannot find a parking spot on the current level
 * Vehicles will look for the most optimal parking spot on their current level,
 however, they will take the next best thing if none are available. i.e. a motorcycle
 will not go to the next level to look for a motorcycle parking spot when there is a
 large parking spot available on the current level
 * Every level of the garage will have the same parking spot layout
 * The maximum rows and spots of the levels are dictated by their template file

## Implementation details

Level has two different ways of retrieving spots:
 * Vehicles that only require one parking spot will use a queue, this allows
 a more optimal way of inserting and retrieving them.
 * Bus will instead loop through every spot in the Level, retrieve the spots, 
 and remove the respective spots from the queue. This is a bit less optimal than
 inserting a single parking spot vehicle.

 The spot is responsible for being assigned to the vehicle, rather then the vehicle being
 parked in the spot.

 The level is in charge of parking the vehicle in its respective spot, the garage is reponsible
 in searching for a level to insert the vehicle into.

## Folder structure

The `infrastructure` folder includes the [Garage](#garage), [Level](#level), and
[Spot](#spot) implementations.

The `vehicle` folder includes the [Vehicle](#vehicle), [Car](#car), [Bus](#bus),
and [Motorcycle](#motorcycle) implementations.

The `templates` folder includes text templates of the layout of the Level class,
more information can be found in [Level templates](#leveltemplates).

The `tests` folder contains all the unit tests.

## Test run

run `main.py` to test out the implementation

<a name="garage"></a>

## Garage

The main parking garage class that will accept a [Vehicle](#Vehicle) object, park
it, and return a key in the form of a string to later retrieve the parked Vehicle.

* [Garage](#garage)
    * [Garage(levels, [template])](#garage+new)
    * [.park(vehicle)](#garage+park)
    * [.unpark(key)](#garage+unpark)

<a name="garage+new"></a>

### Garage(levels, [template])

| Param | Type | Description |
| --- | --- | --- |
| levels | `int` | How many levels the parking garage will have |
| [template] | `string` | the path to a text file in `templates/` that contains the Level layout |

<a name="garage+park"></a>

### Garage.park(vehicle) => `string`, `None`

| Param | Type |
| --- | --- |
| vehicle | `Vehicle` |

Returns a `string` representing the key that will be used to retrieve vehicle using [Garage.unpark(string)](#garage+unpark),
or returns `None` if no parking spots are available.

<a name="garage+unpark"></a>

### Garage.unpark(key) => `Vehicle`, `None`

| Param | Type | Description |
| --- | --- | --- |
| key | `string` | the key given by `Garage.park` |

Returns the `Vehicle` that was assigned to `key`, returns None if no `Vehicle` is assigned to that `key`.

<a name="level"></a>

## Level

Level class that will represent the levels of the parking garage, each level will have multiple rows with different
combinations of parking spots and defined in the template file.

* [Level](#level)
    * [Level(template)](#level+new)
    * [.park(vehicle)](#level+park)
    * [.unpark(key)](#level+unpark)

<a name="level+new"></a>

### Level(template)

| Param | Type | Description |
| --- | --- | --- |
| template | `string` | the path to a text file in `templates/` that contains the Level layout |

<a name="level+park"></a>

### Level.park(vehicle) => `String`, `None`

| Param | Type | Description |
| --- | --- | --- |
| vehicle | `Vehicle` | the `Vehicle` object passed from `Garage` to be stored |

Returns a `string` representing the key that will be used to retrieve vehicle using [Level.unpark(string)](#level+unpark),
or returns `None` if no parking spots are available.

<a name="level+unpark"></a>

### Level.unpark(key) => `Vehicle`, `None`

| Param | Type | Description |
| --- | --- | --- |
| key | `string` | the key given by `level.park` |

Returns the `Vehicle` that was assigned to `key`, returns None if no `Vehicle` is assigned to that `key`.

<a name="spot"></a>

## Spot

* [Spot](#spot)
    * [Spot(size)](#spot+new)
    * [.park(vehicle)](#spot+park)
    * [.unpark()](#spot+unpark)
    * [.is_empty()](#spot+empty)
    * [.get_size](#spot+size)
    * [.can_fit(vehicle)](#spot+canfit)

<a name="spot+new"></a>

### Spot(size)

| Param | Type | Description |
| --- | --- | --- |
| size | `int` | the size of the parking spot as defined in [SpotSize](#spotsize) |


<a name="spot+park"></a>

### Spot.park(vehicle) => `Boolean`

| Param | Type |
| --- | --- |
| vehicle | `Vehicle` |

Returns `Boolean` depending if vehicle was successfully parked

<a name="spot+unpark"></a>

### Spot.unpark() => `Vehicle`, `None`

Returns the `Vehicle` object stored at this Spot, else returns `None` if it's empty

<a name="spot+empty"></a>

### Spot.is_empty() => `Boolean`

<a name="spot+size"></a>

### Spot.get_size => `int`

<a name="spot+canfit"></a>

### Spot.can_fit(vehicle) => `Boolean`

| Param | Type | 
| --- | --- |
| vehicle | `Vehicle` |

Checks if the spot can fit the passed `Vehicle` object

<a name="vehicle"></a>

## Vehicle

Virtual class to represent the different types of `Vehicle` objects that will be parked
in the garage. The class that inherit from Vehicle are [Car](#car), [Bus](#bus), and [Motorcycle](#motorcycle).

* [Vehicle](#vehicle)
    * [.get_name](#vehicle+name)
    * [.get_size](#vehicle+size)

<a name="vehicle+name"></a>

### Vehicle.get_name => `string`

<a name="vehicle+size"></a>

### Vehicle.get_size => `int`

<a name="car"></a>

## Car

Inherits methods from [Vehicle](#vehicle)

 * [Car](#car)
    * [Car(name)](#car+new)

<a name="car+new"></a>

### Car(name)

| Param | Type | Description |
| --- | --- | --- |
| name | `string` | The name of the Car object |

<a name="motorcycle"></a>

## Motorcycle

Inherits methods from [Vehicle](#vehicle)

 * [Motorcycle](#Motorcycle)
    * [Motorcycle(name)](#Motorcycle+new)

<a name="Motorcycle+new"></a>

### Motorcycle(name)

| Param | Type | Description |
| --- | --- | --- |
| name | `string` | The name of the Motorcycle object |

<a name="bus"></a>

## Bus

Inherits methods from [Vehicle](#vehicle), also includes extra methods to take care
of taking up multiple spots.

 * [Bus](#Bus)
    * [Bus(name)](#Bus+new)
    * [.get_spot_count](#Bus+spots)

<a name="Bus+new"></a>

### Bus(name)

| Param | Type | Description |
| --- | --- | --- |
| name | `string` | The name of the Motorcycle object |

### Bus.get_spot_count => `int`

Returns the amount of parking spots Bus will take up

<a name="spotsize"></a>

## SpotSize

An enumerated class representing the different categories of parking spots. `SpotSize.ALL` is an `ordered set` of
all the current available parking spot types.

 * [SpotSize](#Spotsize)
    * [.LARGE](#Spotsize+large)
    * [.COMPACT](#Spotsize+compact)
    * [.MOTORCYCLE](#Spotsize+mc)
    * [.ALL](Spotsize+all)

<a name="leveltemplates"></a>

## Level Template

Level templates are in the form of a text file. Each line of the text file represents a row in the level.
Spots can be labeled with 0, 1, 2 to represent motorcycle, large, and compact parking spots respectively.
