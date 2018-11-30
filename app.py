from pymongo import MongoClient
from flask import Flask
from flask import render_template
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DATABASE_NAME = 'bloombergdata'
COLLECTION_NAME = 'repo_data'
FIELDS = {"RepositoryData":True, "_id":0}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bloombergdata/repo_data")
def github_visualisation_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DATABASE_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = {}
    json_projects["RepositoryData"] = {}
    for project in projects:
        for projectss in project:
            json_projects.append(projectss)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(debug=True)