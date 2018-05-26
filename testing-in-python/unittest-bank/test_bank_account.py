import unittest

from bank_account import BankAccount, MinimumBalanceAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account_mikael = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_mikael.balance, 3000, msg='Account Balnce invalid.')

    def test_deposit(self):
        self.account_mikael.deposit(4000)
        self.assertEqual(self.account_mikael.balance, 7000, msg='Deposit method inaccurate.')

    def test_withdraw(self):
        self.account_mikael.withdraw(500)
        self.assertEqual(self.account_mikael.balance, 2500, msg='Withdraw method inaccurate.')

    def test_invalid_trasaction(self):
        self.assertEqual(self.account_mikael.withdraw(6000), 'Invalid Transaction.')

    def test_subclass(self):
        self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='Not True subclass of BankAccount.')


if __name__ == '__main__':
    unittest.main()

# $ python test_bank_account.py
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s
#
# OK
