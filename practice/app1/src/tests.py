from functions import (add_flight, change_flights, modify_flight,
                       positive_integer, reroute_flight)


def test_positive_integer():
    assert positive_integer("1") == 1

    try:
        positive_integer("0")
        assert False
    except ValueError:
        pass

    print("Positive integer test passed.")


def test_add_flight():
    flights = []
    result = add_flight(flights, "qf1000", "180", "zurich", "rome")

    assert len(result) == 1
    assert result[0]["flight_code"] == "qf1000"
    assert result[0]["duration"] == 180
    assert result[0]["departure"] == "zurich"
    assert result[0]["destination"] == "rome"

    result = []
    print("Add flights passed")


def test_modify_flight():
    flights = []
    flights = add_flight(flights, "qf1000", "180", "zurich", "rome")
    result = modify_flight(flights, "qf1000", "100")

    assert len(result) == 1
    assert result[0]["duration"] == 100

    result = []
    print("Modify flights passed")


def test_reroute_flight():
    flights = []
    flights = add_flight(flights, "qf1000", "180", "zurich", "rome")
    flights = add_flight(flights, "qf1002", "180", "zurich", "rome")

    result = []
    result = reroute_flight(flights, "rome", "bucharest")
    assert len(result) == 2
    for res in result:
        assert res["destination"] == "bucharest"

    result = []
    print("Reroute flights passed")
