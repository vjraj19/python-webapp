import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Welcome all!')

    def test_hello_route(self):
        response = self.app.get('/how are you')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'I am very good, how about you?')

    def test_code_route(self):
        response = self.app.get('/code')
        self.assertEqual(response.status_code, 200)
        self.assertIn("```python", response.data.decode('utf-8'))
        self.assertIn("def greet(name):", response.data.decode('utf-8'))

    def test_code2_route(self):
        response = self.app.get('/code2')
        self.assertEqual(response.status_code, 200)
        self.assertIn("```python", response.data.decode('utf-8'))
        self.assertIn("def add(x, y):", response.data.decode('utf-8'))

    def test_code3_route(self):
        response = self.app.get('/code3')
        self.assertEqual(response.status_code, 200)
        self.assertIn("```python", response.data.decode('utf-8'))
        self.assertIn("def multiply(x, y):", response.data.decode('utf-8'))

    def test_non_existent_route(self):
        response = self.app.get('/non-existent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()