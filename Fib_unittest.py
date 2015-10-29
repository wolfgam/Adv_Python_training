import unittest

import fib


class TestFibonacci(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "setting up test suite"

    @classmethod
    def tearDownClass(cls):
        print "tearing down after test suite"

    def setUp(self):
        print "setting up for unit test"

    def tearDown(self):
        print "tearing down after unit test"

    def test_fib1(self):
        with self.assertRaises(fib.InvalidInputError): fib.fib1(-100)
        with self.assertRaises(fib.InvalidInputError): fib.fib1(-1)
        self.assertEqual(0, fib.fib1(0))
        self.assertEqual(1, fib.fib1(1))
        self.assertEqual(1, fib.fib1(2))
        self.assertEqual(2, fib.fib1(3))
        self.assertEqual(3, fib.fib1(4))
        self.assertEqual(5, fib.fib1(5))
        self.assertEqual(8, fib.fib1(6))

    def test_fib2(self):
        with self.assertRaises(fib.InvalidInputError): fib.fib2(-100)
        with self.assertRaises(fib.InvalidInputError): fib.fib2(-1)
        self.assertEqual(fib.fib1(0), fib.fib2(0))
        self.assertEqual(fib.fib1(1), fib.fib2(1))
        self.assertEqual(fib.fib1(2), fib.fib2(2))
        self.assertEqual(fib.fib1(3), fib.fib2(3))
        self.assertEqual(fib.fib1(4), fib.fib2(4))
        self.assertEqual(fib.fib1(5), fib.fib2(5))
        self.assertEqual(fib.fib1(6), fib.fib2(6))

    def test_fib3(self):
        with self.assertRaises(fib.InvalidInputError): fib.fib3(-100)
        with self.assertRaises(fib.InvalidInputError): fib.fib3(-1)
        self.assertEqual(fib.fib3(0), fib.fib2(0))
        self.assertEqual(fib.fib3(1), fib.fib2(1))
        self.assertEqual(fib.fib3(2), fib.fib2(2))
        self.assertEqual(fib.fib3(3), fib.fib2(3))
        self.assertEqual(fib.fib3(4), fib.fib2(4))
        self.assertEqual(fib.fib3(5), fib.fib2(5))
        self.assertEqual(fib.fib3(6), fib.fib2(6))


if __name__ == "__main__":
    unittest.main()
