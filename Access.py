from github import Github
import json

token = "fceed303e67495273a75c12b170080e7b515fcc9"


# First create a Github instance using an access token
def crawler():
    g = Github(token)
    user = g.get_user("Bloomberg")

    for repo7 in user.get_repos():
        print(repo7.name)
        print(repo7.size)
        y = repo7.get_languages()
        for x in y:
            print(x)
            print(y[x])
        con = repo7.get_contributors()
        for c in con:
            print(c)


    data = {}
    data["Contributors"] = {}
'''
    for repo in user.get_repos():
        print(repo.name)
        contributors = repo.get_stats_contributors()
        data["Contributors"][""+repo.name] = []
        for c in contributors:
            total_insertions = 0
            total_deletions = 0
            total_contribution = 0
            for week in c.weeks:
                total_insertions += week.a
                total_deletions += week.d
                total_contribution += (week.a + week.d)
            data["Contributors"][""+repo.name].append({
                "Name": c.author.login,
                "Insertions": total_insertions,
                "Deletions": total_deletions,
                "Contributions": total_contribution
            })
    with open('contributors_data.json', 'w') as outfile:
        json.dump(data, outfile)
'''

def main():
    crawler()


if __name__ == '__main__':
    main()
