import unittest
import additional
import responses


class TeatFunction(unittest.TestCase):

    @responses.activate
    def test_simple(self):
        responses.add(responses.GET, 'https://api.github.com/users/DronSofiia/repos', status=404)
        res = additional.get_data('DronSofiia')
        self.assertEqual(res, 'ERROR')


if __name__ == '__main__':
    unittest.main()
