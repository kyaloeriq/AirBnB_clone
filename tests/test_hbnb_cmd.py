import unittest
from unittest.mock import patch
from io import StringIO
from hbnb_cmd import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        self.cmd = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user(self, mock_stdout):
        self.cmd.onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output.isalnum())  # Check if the output is an alphanumeric string (ID)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user(self, mock_stdout):
        with patch('sys.stdin', return_value='show User 123\n'):
            self.cmd.onecmd("show User 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_user(self, mock_stdout):
        with patch('sys.stdin', return_value='update User 123 name "John"\n'):
            self.cmd.onecmd("update User 123 name 'John'")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_user(self, mock_stdout):
        with patch('sys.stdin', return_value='destroy User 123\n'):
            self.cmd.onecmd("destroy User 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

if __name__ == '__main__':
    unittest.main()
