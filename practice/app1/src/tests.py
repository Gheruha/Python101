from functions import add_flight, change_flights, positive_integer


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
    assert result[0]["flight_code"] == "qf10001"
    assert result[0]["duration"] == "180"
    assert result[0]["departure"] == "zurich"
    assert result[0]["destination"] == "rome"

    print("Add flights passed")
    flights = []


if __name__ == "__main__":
    test_positive_integer()
    test_add_flight()
