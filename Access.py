from github import Github
import unittest

token = "36d351745b0d1930d39ea54ac6c61d8adc9a2889"


class GithubAccessTest(unittest.TestCase):

    def testConstructor(self):
        g = Github(token)
        user = g.get_user("Bloomberg")
        self.assertEqual(user.login, u'bloomberg')
        self.assertEqual(user.name, 'Bloomberg')


# First create a Github instance using an access token
def main():
    g = Github(token)
    user = g.get_user("Bloomberg")

    for repo in user.get_repos():
        print(repo.name)

    repositories = g.search_repositories(query='language:c++')
    for repo in repositories:
        print(repo)

    print("Repository Name: bqplot")
    repo = user.get_repos("Bloomberg/bqplot")
    print("Stars: "+repo.get_topics())

    print("Contents: ")
    contents = repo.get_contents("")
    for content_file in contents:
        print(content_file)

    print("List of Branches:")
    list(repo.get_branches())

    print("Contributors:")
    contributors = repo.get_contributors()
    for contributor in contributors:
        print(contributor.login)


if __name__ == '__main__':
    unittest.main()
