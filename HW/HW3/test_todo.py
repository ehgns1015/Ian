import unittest
from todo import add_task, remove_task, view_tasks
from io import StringIO
from unittest.mock import patch

class TestToDoList(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        add_task(tasks, "Buy groceries")
        self.assertIn("Buy groceries", tasks)
        self.assertEqual(len(tasks), 1)

    def test_add_multiple_tasks(self):
        tasks = []
        add_task(tasks, "Clean room")
        add_task(tasks, "Walk dog")
        self.assertEqual(tasks, ["Clean room", "Walk dog"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_remove_valid_task(self, mock_stdout):
        tasks = ["Buy groceries", "Pay bills"]
        remove_task(tasks)
        self.assertNotIn("Buy groceries", tasks)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks, ["Pay bills"])
        self.assertIn("Task 'Buy groceries' removed.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_remove_invalid_index(self, mock_stdout):
        tasks = ["Buy groceries", "Pay bills"]
        remove_task(tasks)  # Index is out of bounds
        self.assertEqual(len(tasks), 2)
        self.assertIn("Invalid task number.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_remove_from_empty_list(self, mock_stdout):
        tasks = []
        remove_task(tasks)
        self.assertEqual(len(tasks), 0)
        self.assertIn("Invalid task number.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks_with_items(self, mock_stdout):
        tasks = ["Read a book", "Exercise"]
        view_tasks(tasks)
        output = mock_stdout.getvalue()
        self.assertIn("1. Read a book", output)
        self.assertIn("2. Exercise", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks_empty(self, mock_stdout):
        tasks = []
        view_tasks(tasks)
        self.assertIn("No tasks in the list.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()