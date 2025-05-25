import unittest
from tasks import add_task, mark_completed

class TestTasks(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        add_task(tasks, "Test task", 1)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test task")
        self.assertFalse(tasks[0]["completed"])

    def test_mark_completed(self):
        tasks = [{"title": "Do homework", "completed": False, "priority": 2}]
        mark_completed(tasks, 0)
        self.assertTrue(tasks[0]["completed"])

if __name__ == "__main__":
    unittest.main()
