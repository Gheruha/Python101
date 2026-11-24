from tests import (test_add_flight, test_modify_flight, test_positive_integer,
                   test_reroute_flight)
from ui import main

if __name__ == "__main__":
    test_positive_integer()
    test_add_flight()
    test_modify_flight()
    test_reroute_flight()
    main()
