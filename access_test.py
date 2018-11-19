import unittest
from Access import *


class GithubAccessTest(unittest.TestCase):

    def testConstructor(self):
        g = Github(token)
        user = g.get_user("Bloomberg")
        self.assertEqual(user.login, u'bloomberg')
        self.assertEqual(user.name, 'Bloomberg')

        print("Repository Name: bqplot")
        repo2 = user.get_repos("Bloomberg/bde")
        for repo in repo2:
            topics = repo.get_topics()
            for c in topics:
                print(c)

        print("Contents: ")
        contents = repo.get_contents("")
        for content_file in contents:
            print(content_file)

        print("List of Branches:")
        list(repo.get_branches())

if __name__ == '__main__':
    unittest.main()
