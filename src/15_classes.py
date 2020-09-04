# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(thing, lat, lon):
        thing.lat = lat
        thing.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(thing, lat, lon, name):
        super().__init__(lat, lon)
        thing.name = name

    def printstuffs(thing):
        print(thing.name, thing.lat, thing.lon)

    def __str__(thing):
        return f'{thing.name}, {thing.lat}, {thing.lon}'


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(thing, lat, lon, name, difficult, size):
        super().__init__(lat, lon, name)
        thing.difficult = difficult
        thing.size = size
    
    def __str__(thing):
        return f'{thing.name}, diff {thing.difficult}, size {thing.size}, {thing.lat}, {thing.lon}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
Waypoint(41.70505, -121.51521, 'Catacombs').printstuffs()

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint(41.70505, -121.51521, 'Catacombs')
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, 'Newberry Views', '1.5', '2')

# Print it--also make this print more nicely
print(geocache)
