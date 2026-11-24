# Functions


def positive_integer(text):
    number = int(text)
    if number < 1:
        raise ValueError("The value should be bigger than 0.")
    return number


def add_flight(flights, flight_code, duration, departure, destination):
    duration = int(duration)

    if (
        len(flight_code) < 3
        or duration < 20
        or len(departure) < 3
        or len(destination) < 3
    ):
        raise ValueError("Check the menu again, one of the values has a wrong value")

    new_flight = {
        "flight_code": flight_code,
        "duration": duration,
        "departure": departure,
        "destination": destination,
    }
    return flights + [new_flight]


def modify_flight(flights, flight_code, duration):
    duration = int(duration)
    if duration < 20:
        raise ValueError("Check the menu again, one of the values has a wrong value")
    else:
        for flight in flights:
            if flight["flight_code"] == flight_code:
                flight["duration"] = duration
            return flights
    raise ValueError("Flight code not found")


def reroute_flight(flights, destination, new_destination):
    if len(destination) < 3 or len(new_destination) < 3:
        raise ValueError("Check the menu again, one of the values has a wrong value")

    found = False
    for flight in flights:
        if flight["destination"] == destination:
            flight["destination"] = new_destination
            found = True
    if not found:
        raise ValueError("There is no " + destination + " destination.")

    return flights


def show_flights(words, flights):
    print("show flights")


def change_flights(words, flights):
    command = words[0]

    if command == "add" and len(words) == 5:
        return add_flight(flights, words[1], words[2], words[3], words[4])
    elif command == "modify" and len(words) == 3:
        return modify_flight(flights, words[1], words[2])
    elif command == "reroute":
        return reroute_flight(flights, words[1], words[2])

    raise ValueError("Invalid command")
