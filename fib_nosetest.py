from nose.tools import with_setup

import fib

def setup():
    print "setting up nose test suite"

def teardown():
    print "tearing down nose test suite"

def setup_individual():
    print "setting up individual test"

def teardown_individual():
    print "tearing down individual test"

@with_setup(setup_individual, teardown_individual)
def test_fib1():
    try:
        assert None == fib.fib1(-1)
    except fib.InvalidInputError:
        pass
    assert 0 == fib.fib1(0)
    assert 1 == fib.fib1(1)
    assert 1 == fib.fib1(2)
    assert 2 == fib.fib1(3)
    assert 3 == fib.fib1(4)
    assert 5 == fib.fib1(5)
    assert 8 == fib.fib1(6)

@with_setup(setup_individual, teardown_individual)
def test_fib2():
    try:
        assert None == fib.fib2(-1)
    except fib.InvalidInputError:
        pass
    assert fib.fib1(0) == fib.fib2(0)
    assert fib.fib1(1) == fib.fib2(1)
    assert fib.fib1(2) == fib.fib2(2)
    assert fib.fib1(3) == fib.fib2(3)
    assert fib.fib1(4) == fib.fib2(4)
    assert fib.fib1(5) == fib.fib2(5)
    assert fib.fib1(6) == fib.fib2(6)
