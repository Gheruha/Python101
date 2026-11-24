# Functions


def positive_integer(text):
    number = int(text)
    if number < 1:
        raise ValueError("The value should be bigger than 0.")
    return number


def add_flight(flights, flight_code, duration, departure, destination):
    new_flight = {
        "flight_code": flight_code,
        "duration": duration,
        "departure": departure,
        "destination": destination,
    }
    return flights + [new_flight]


def modify_flight(words, flights):
    print("modify flight")


def reroute_flight(words, flights):
    print("reroute flight")


def show_flights(words, flights):
    print("show flights")


def change_flights(words, flights):
    command = words[0]

    if command == "add" and len(words) == 5:
        return add_flight(flights, words[1], words[2], words[3], words[4])
