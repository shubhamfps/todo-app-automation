def pytest_addoption(parser):
    parser.addoption(
        "--ipaddress",
        action="store",
        default="localhost:3000",
        help="IP address for tests"
    )
