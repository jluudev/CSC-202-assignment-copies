# CPE 202 Location Class, Lab 1

# represents a location using name, latitude and longitude
class Location:
    def __init__(self, name: str, lat: float, lon: float):
        self.name = name  # string for name of location
        self.lat = lat  # latitude in degrees (-90.0 to 90.0)
        self.lon = lon  # longitude in degrees (-180.0 to 180.0)

    # ADD BOILERPLATE HERE (__eq__ and __repr__ functions)
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Location):
            return self.name == other.name and self.lat == other.lat and self.lon == other.lon
        else:
            return False

    def __repr__(self) -> str:
        return "Location({!r}, {!r}, {!r})".format(self.name, self.lat, self.lon)


def main() -> None:  # pragma: no cover
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:", loc1)
    print("Location 2:", loc2)
    print("Location 3:", loc3)
    print("Location 4:", loc4)

    print("\nLocation 1 equals Location 2:", loc1 == loc2)
    print("Location 1 equals Location 3:", loc1 == loc3)
    print("Location 1 equals Location 4:", loc1 == loc4)

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)


if __name__ == "__main__":  # pragma: no cover
    main()
