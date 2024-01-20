import pytest
from create_flight_license import FlightLicense
from datetime import datetime
@pytest.mark.fourteen
def test_1():
    assert FlightLicense('John', 'Doe', datetime(1977,12,25)).create() == 'DOE99-7127.j'

@pytest.mark.fourteen
def test_2():
    assert FlightLicense('Hal', 'Jordan', datetime(1995,9,2)).create() == 'JORDA-9095.h'

@pytest.mark.fourteen
def test_3():
    assert FlightLicense('Carol', 'Danvers', datetime(1968,8,17)).create() == 'DANVE-6088.c'

@pytest.mark.fourteen
def test_4():
    assert FlightLicense('Poe', 'Dameron', datetime(1979,3,9)).create() == 'DAMER-7039.p'
