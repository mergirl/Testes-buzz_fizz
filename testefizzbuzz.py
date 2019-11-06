import unittest
from fizz_buzz import solucao

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_fizz(self):
        self.assertEqual(solucao(3), "fizz")

    def test_fizz_buzz_buzz(self):
        self.assertEqual(solucao(5), "buzz")

    def test_fizz_buzz_fizz_buzz(self):
        self.assertEqual(solucao(15), "fizz-buzz")

unittest.main()
