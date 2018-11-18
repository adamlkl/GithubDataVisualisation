import unittest
from Access import *


class GithubAccessTest(unittest.TestCase):

    def testConstructor(self):
        g = Github(token)
        user = g.get_user("Bloomberg")
        self.assertEqual(user.login, u'bloomberg')
        self.assertEqual(user.name, 'Bloomberg')


if __name__ == '__main__':
    unittest.main()
