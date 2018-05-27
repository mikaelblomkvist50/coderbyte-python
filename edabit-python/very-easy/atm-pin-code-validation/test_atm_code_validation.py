import unittest
import atm_pin_code_validation

class TestAtm(unittest.TestCase):
    def test_special_characters_returns_false(self):
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("a234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("%234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("`234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("@234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("#234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("$234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("*234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("^234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("(234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN(")234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("-234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("_234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("+234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("=234"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("?234"), False)

    def test_incorrect_pin_length_returns_false(self):
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("12345"), False)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN(""), False)

    def test_pin_with_no_speical_characters_and_correct_length_returns_true(self):
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("1234"), True)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("5678"), True)
        self.assertEqual(atm_pin_code_validation.is_valid_PIN("123456"), True)

if __name__ == '__main__':
    unittest.main()
