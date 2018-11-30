from github import Github
from collections import OrderedDict
import collections
import json
import operator


token = "fceed303e67495273a75c12b170080e7b515fcc9"


# sort the dict according to their values of their keys
def get_top_count(data, n=2, order=False):

    if n > len(data):
        n = len(data)
    top = sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:n]
    if order:
        return OrderedDict(top)
    return dict(top)

# First create a Github instance using an access token
def crawler():
    g = Github(token)
    user = g.get_user("Bloomberg")

    repo_data = dict()
    repo_data["RepositoryData"] = {}
    for repo in user.get_repos():
        repo_data["RepositoryData"]["" + repo.name] = []
        repo_data["RepositoryData"]["" + repo.name].append({
            "Size": repo.size
        })
        y = repo.get_languages()
        to = get_top_count(y, n=5)
        loc = 0
        for x in to:
            repo_data["RepositoryData"]["" + repo.name].append({
                "Language": x,
                "LinesOfCode": to[x]
            })
            loc += to[x]
        repo_data["RepositoryData"]["" + repo.name].append({
            "TotalLOC": loc
        })
    with open('repo_data.json', 'w') as outfile:
        json.dump(repo_data, outfile)
    data = dict()
    data["ContributorsData"] = {}

    for repo in user.get_repos():
        if repo.name != "chromium.bb":
            print(repo.name)
            contributors = repo.get_stats_contributors()
            if isinstance(contributors, collections.Iterable):
                data["ContributorsData"][""+repo.name] = []
                total_commits = 0
                for c in contributors:
                    user_total_commits = c.total
                    total_commits += c.total
                    data["ContributorsData"][""+repo.name].append({
                        "Name": c.author.login,
                        "UserTotalCommits": user_total_commits
                    })
                data["ContributorsData"]["" + repo.name].append({
                    "TotalCommits": total_commits
                })

    with open('contributors_data.json', 'w') as outfile:
        json.dump(data, outfile)


def main():
    crawler()


if __name__ == '__main__':
    main()
