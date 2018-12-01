from github import Github
from collections import OrderedDict
import collections
import json
import operator


token = ""


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

    repo_data = []
    for repo in user.get_repos():
        repository = {}
        repository.update({"Name": repo.name})
        repository.update({"Size": repo.size})
        y = repo.get_languages()
        to = get_top_count(y, n=5)
        loc = 0
        lang = []
        for x in to:
            lang.append({
                "Language": x,
                "LinesOfCode": to[x]
            })
            loc += to[x]
        repository.update({"Languages": lang})
        repository.update({"TotalLOC": loc})
        repo_data.append(repository)
    with open('repo_data2.json', 'w') as outfile:
        json.dump(repo_data, outfile)

    c_data = []
    for repo in user.get_repos():
        if repo.name != "chromium.bb":
            print(repo.name)
            contributors = repo.get_stats_contributors()
            if isinstance(contributors, collections.Iterable):
                repository = {}
                repository.update({"Name": repo.name})
                total_commits = 0
                con = []
                for c in contributors:
                    user_total_commits = c.total
                    total_commits += c.total
                    con.append({
                        "Name": c.author.login,
                        "UserTotalCommits": user_total_commits
                    })
                repository.update({"Languages": con})
                repository.update({"TotalCommits": total_commits})
                c_data.append(repository)

    with open('contributors_data2.json', 'w') as outfile:
        json.dump(c_data, outfile)

def main():
    crawler()


if __name__ == '__main__':
    main()
