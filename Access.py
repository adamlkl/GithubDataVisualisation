from github import Github
from collections import OrderedDict
from pymongo import MongoClient
import operator
import json

token = "fceed303e67495273a75c12b170080e7b515fcc9"
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
database_name = "GithubVisualisation"


# sort the dict according to their values of their keys
def get_top_count(data, n=2, order=False):

    if n > len(data):
        n = len(data)
    top = sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:n]
    if order:
        return OrderedDict(top)
    return dict(top)


def get_top_countr(a,n):
    sorted(range(len(a)), key=lambda i: a[i], reverse=True)[:2]


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
        print(repo.name)
        contributors = repo.get_stats_contributors()
        data["ContributorsData"][""+repo.name] = []
        total_commits = repo.get_stats_participation()
        data["ContributorsData"]["" + repo.name].append({
            "TotalCommits": total_commits
        })
        for c in contributors:
            user_total_commits = c.total
            data["ContributorsData"][""+repo.name].append({
                "Name": c.author.login,
                "UserTotalCommits": user_total_commits
            })
    with open('contributors_data.json', 'w') as outfile:
        json.dump(data, outfile)


def github_visualisation_projects():
    client = MongoClient( MONGODB_HOST, MONGODB_PORT)



def main():
    crawler()


if __name__ == '__main__':
    main()
