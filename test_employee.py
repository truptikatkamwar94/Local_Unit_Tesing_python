import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Runs at only starting")

    @classmethod
    def tearDownClass(clas):
        print("Runs when all test case run")

    def setUp(self):#run before any single test
        print("Setup method!Run before any single test case")
        self.emp_1 = Employee('abc', 'pqr', 1000)

    def tearDown(self):#run after any single test
        print("tearDown method!Run after any single test case")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, 'abc.pqr@email.com')

        self.emp_1.first = 'xyz'
        self.assertEqual(self.emp_1.email, 'xyz.pqr@email.com')

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.first, 'abc')

        self.emp_1.first = 'pqr'
        self.assertEqual(self.emp_1.first, 'pqr')

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 1050)

    def test_monthly_schedule_if(self):

        with patch('employee.requests.get') as mock_obj:
            mock_obj.return_value.ok = True
            mock_obj.return_value.text = "Hello"

            result = self.emp_1.monthly_schedule("April")
            self.assertEqual(result, 'Hello')
            mock_obj.assert_called_with('http://company.com/pqr/April')

    def test_monthly_schedule_else(self):

        with patch('employee.requests.get') as mock_obj:
            mock_obj.return_value.ok = False
            result = self.emp_1.monthly_schedule("June")

            self.assertEqual(result, 'Bad_Requests!')
            mock_obj.assert_called_with('http://company.com/pqr/June')