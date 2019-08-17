import unittest

from days_of_power import get_days_of_power

class TestDaysOfPower(unittest.TestCase):
    def test_days_of_power_big_payment(self):
        """
        Test that the function returns the correct days of power.
        """
        result = get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
        self.assertEqual(result, 141)

    def test_days_of_power_small_payment(self):
        """
        Test that the function returns the correct days of power.
        """
        result = get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
        self.assertEqual(result, 17)

    def test_days_of_power_duplicate_dates(self):
        """
        Test that the function returns the correct days of power.
        """
        result = get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)

        self.assertEqual(result, 5)

    def test_days_of_power_one_day_balance(self):
        """
        Test that the function returns the correct days of power.
        """
        result = get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)

        self.assertEqual(result, 1)





if __name__ == '__main__':
    unittest.main()
