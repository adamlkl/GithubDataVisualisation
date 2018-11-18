from github import Github

token = "fceed303e67495273a75c12b170080e7b515fcc9"


# First create a Github instance using an access token
def crawler():
    g = Github(token)
    user = g.get_user("Bloomberg")

    for repo in user.get_repos():
        print(repo.name)

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

    print("Contributors:")
    contributors = repo.get_contributors()
    for contributor in contributors:
        print(contributor.login)


def main():
    crawler()


if __name__ == '__main__':
    main()
