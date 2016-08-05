import unittest

from Application import create_app
from config import get_config


# Simple End To End Tests
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_obj=get_config())
        self.app.config['TESTING'] = True
        self.app = self.app.test_client()

    def test_running(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        assert "OK" in rv.data.decode('UTF-8')


if __name__ == '__main__':
    unittest.main()
