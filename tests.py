# tests.py
import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestCelsiusConversion(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        self.assertEqual(convertCelsiusToKelvin(0), 273.15)
        self.assertEqual(convertCelsiusToKelvin(100), 373.15)
        # Add more test cases

    def test_convertCelsiusToFahrenheit(self):
        self.assertEqual(convertCelsiusToFahrenheit(0), 32.0)
        self.assertEqual(convertCelsiusToFahrenheit(100), 212.0)
        # Add more test cases

if __name__ == '__main__':
    unittest.main()
